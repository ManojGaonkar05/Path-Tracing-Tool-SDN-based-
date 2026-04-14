from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

class PathTracerTopo(Topo):
    def build(self):
        # 3 switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # 3 hosts with fixed IPs
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')

        # Links
        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s2, h2)
        self.addLink(s3, h3)

if __name__ == '__main__':
    setLogLevel('info')
    topo = PathTracerTopo()
    net = Mininet(
        topo=topo,
        controller=RemoteController,   # Ryu runs separately
        switch=OVSSwitch
    )
    net.start()
    CLI(net)     # gives you the mininet> prompt
    net.stop()