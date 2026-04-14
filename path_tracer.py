import subprocess
import sys

SWITCHES = ['s1', 's2', 's3']

def get_flows(switch):
    result = subprocess.run(
        ['ovs-ofctl', '-O', 'OpenFlow13', 'dump-flows', switch],
        capture_output=True, text=True
    )
    return result.stdout

def parse_path(src_ip, dst_ip):
    print(f"\n{'='*50}")
    print(f" PATH TRACE: {src_ip}  -->  {dst_ip}")
    print(f"{'='*50}")

    path = []
    for sw in SWITCHES:
        flows = get_flows(sw)
        lines = flows.strip().split('\n')
        has_rule = False
        for line in lines:
            # Look for any forwarding rule (not table-miss rule priority=0)
            if 'actions=output' in line and 'priority=0' not in line:
                port = line.split('output:')[-1].strip().split()[0].rstrip(',')
                print(f"  [HIT] Switch {sw}  -->  out port {port}")
                path.append(sw)
                has_rule = True
                break
        if not has_rule:
            print(f"  [---] Switch {sw}  -->  no matching rule")

    print()
    if path:
        print(f"  ROUTE:  {src_ip}  -->  {'  -->  '.join(path)}  -->  {dst_ip}")
    else:
        print(f"  No path found. Run 'pingall' in Mininet first.")
    print()

if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else '10.0.0.1'
    dst = sys.argv[2] if len(sys.argv) > 2 else '10.0.0.2'
    parse_path(src, dst)