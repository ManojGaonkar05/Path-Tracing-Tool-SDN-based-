from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet, ipv4

class PathTracingController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mac_to_port = {}   # {switch_id: {mac: port}}

    # Called when a switch connects — send it a "table-miss" rule
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        dp = ev.msg.datapath
        ofp = dp.ofproto
        parser = dp.ofproto_parser
        # Rule: if no other rule matches, send packet to controller
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofp.OFPP_CONTROLLER, ofp.OFPCML_NO_BUFFER)]
        self._add_flow(dp, priority=0, match=match, actions=actions)
        self.logger.info("Switch %s connected", dp.id)

    # Called every time a switch doesn't know where to send a packet
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        dp = msg.datapath
        ofp = dp.ofproto
        parser = dp.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)
        eth_pkt = pkt.get_protocol(ethernet.ethernet)
        if eth_pkt is None:
            return

        dst_mac = eth_pkt.dst
        src_mac = eth_pkt.src
        dpid = dp.id

        # Learn: src_mac came in on in_port of this switch
        self.mac_to_port.setdefault(dpid, {})
        self.mac_to_port[dpid][src_mac] = in_port
        self.logger.info("LEARN  sw=%s  mac=%s  port=%s", dpid, src_mac, in_port)

        if dst_mac in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst_mac]
            # Install a flow rule so future packets skip the controller
            match = parser.OFPMatch(in_port=in_port, eth_dst=dst_mac)
            actions = [parser.OFPActionOutput(out_port)]
            self._add_flow(dp, priority=1, match=match, actions=actions)
            self.logger.info("FLOW   sw=%s  dst=%s  --> port %s", dpid, dst_mac, out_port)
        else:
            out_port = ofp.OFPP_FLOOD   # don't know yet — broadcast

        actions = [parser.OFPActionOutput(out_port)]
        out = parser.OFPPacketOut(
            datapath=dp, buffer_id=msg.buffer_id,
            in_port=in_port, actions=actions,
            data=msg.data
        )
        dp.send_msg(out)

    def _add_flow(self, dp, priority, match, actions, idle=0, hard=0):
        ofp = dp.ofproto
        parser = dp.ofproto_parser
        inst = [parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, actions)]
        mod = parser.OFPFlowMod(
            datapath=dp, priority=priority,
            idle_timeout=idle, hard_timeout=hard,
            match=match, instructions=inst
        )
        dp.send_msg(mod)