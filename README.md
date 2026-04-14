# SDN Path Tracing Tool

## Problem Statement
A path tracing tool built using SDN (Mininet + Ryu + OpenFlow).
Identifies and displays the path taken by packets through the network
by tracking flow rules installed by the controller.

## Topology
H1 (10.0.0.1) — S1 — S2 — S3 — H3 (10.0.0.3)
                       |
                      H2 (10.0.0.2)

## Setup
1. Install Mininet: `sudo apt install mininet -y`
2. Install Ryu: `pip3 install ryu --break-system-packages`

## How to Run

### Scenario 1 — Normal forwarding + path trace
Terminal 1: `ryu-manager controller.py`
Terminal 2: `sudo python3 topology.py`
In Mininet: `pingall`
Terminal 3: `sudo python3 path_tracer.py 10.0.0.1 10.0.0.2`

### Scenario 2 — Firewall (H3 blocked)
Terminal 1: `ryu-manager firewall.py`
Terminal 2: `sudo python3 topology.py`
In Mininet: `h1 ping h3`  (should FAIL)
            `h1 ping h2`  (should PASS)

## Expected Output
Path tracer shows: 10.0.0.1 → s1 → s2 → 10.0.0.2
Firewall shows: ping to H3 fails, ping to H2 succeeds

## References
- https://mininet.org
- https://ryu.readthedocs.io