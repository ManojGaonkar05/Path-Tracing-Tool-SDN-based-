# 🚀 SDN Path Tracing Tool (Mininet + Ryu + OpenFlow)

## 📌 Project Overview

The **SDN Path Tracing Tool** is a Software Defined Networking (SDN) application that identifies and displays the path taken by packets in a network.

It leverages:

* **Mininet** for network simulation
* **Ryu Controller** for centralized control
* **OpenFlow** for flow rule management

This project provides **deep visibility into packet forwarding behavior**, which is not available in traditional networks.

---

## 🎯 Problem Statement

To design a system that:

* Tracks packet flow dynamically
* Identifies forwarding paths
* Displays routes taken by packets
* Validates behavior using test scenarios

---

## 🧠 Key Concepts Used

* Software Defined Networking (SDN)
* OpenFlow (Match–Action rules)
* Packet_in / Packet_out mechanism
* Flow table management
* Network virtualization using Mininet

---

## 🏗️ Architecture

### Components:

* **Hosts (H1, H2, H3)** → Generate traffic
* **Switches (S1, S2, S3)** → Forward packets
* **Ryu Controller** → Makes decisions and installs flow rules
* **Path Tracer Module** → Tracks and displays path

---

## 🌐 Network Topology

```
H1 (10.0.0.1)
     |
     S1 —— S2 —— S3 —— H3 (10.0.0.3)
              |
             H2 (10.0.0.2)
```

---

## ⚙️ Working Flow

### 1. Packet Generation

A host sends a packet (e.g., `h1 ping h2`)

### 2. Packet-In Event

Switch sends request to controller when no rule exists

### 3. Controller Decision

Controller determines path based on logic

### 4. Flow Rule Installation

Controller installs rule:

```
Match: src IP, dst IP
Action: forward to specific port
```

### 5. Packet Forwarding

Switch forwards packets using installed rules

### 6. Path Tracing

Path tracer extracts and displays route:

```
10.0.0.1 → s1 → s2 → 10.0.0.2
```

---

## ✨ Features

* Dynamic path tracing
* Flow rule monitoring
* Real-time route display
* Firewall implementation (blocking specific host)
* Multiple test scenarios
* SDN-based intelligent routing

---

## 🛠️ Setup Instructions

### 1. Install Mininet

```bash
sudo apt update
sudo apt install mininet -y
```

### 2. Create Virtual Environment

```bash
python3.8 -m venv ryu-env
source ryu-env/bin/activate
```

### 3. Install Ryu Controller

```bash
pip install setuptools==58.0.4
pip install wheel
pip install ryu
```

---

## 🧹 Cleanup Before Running (Important)

Before running the project, always execute:

```bash
sudo mn -c
```

### 💡 Why this is required?

Mininet creates virtual interfaces (e.g., `s1-eth1`, `s2-eth2`).
If not cleaned properly, they remain in the system and cause errors like:

```
RTNETLINK answers: File exists
```

### ✅ What this command does:

* Removes stale interfaces
* Clears old topology
* Resets Open vSwitch

### ⚠️ Best Practice:

Run this before every execution to avoid conflicts.

---

## ▶️ How to Run the Project

---

### 🔹 Scenario 1: Normal Forwarding + Path Tracing

#### Step 1: Cleanup

```bash
sudo mn -c
```

#### Step 2: Start Controller

```bash
ryu-manager controller.py
```

#### Step 3: Run Topology

```bash
sudo python3 topology.py
```

#### Step 4: Test Network

Inside Mininet:

```bash
pingall
```

#### Step 5: Run Path Tracer

```bash
sudo python3 path_tracer.py 10.0.0.1 10.0.0.2
```

---

### 🔹 Scenario 2: Firewall (Blocking H3)

#### Step 1: Cleanup

```bash
sudo mn -c
```

#### Step 2: Run Firewall Controller

```bash
ryu-manager firewall.py
```

#### Step 3: Run Topology

```bash
sudo python3 topology.py
```

#### Step 4: Test

```bash
h1 ping h3   # Expected: FAIL
h1 ping h2   # Expected: SUCCESS
```

---

## 📊 Expected Output

### Path Tracing Output

```
Packet Path:
10.0.0.1 → s1 → s2 → 10.0.0.2
```

### Firewall Output

```
Ping to H3: FAILED
Ping to H2: SUCCESS
```

---

## 📈 Performance Validation

* Latency using `ping`
* Throughput using `iperf`
* Flow rules using:

```bash
ovs-ofctl dump-flows s1
```

---

## 🔍 How It Works (Simple Explanation)

* Controller acts as the brain
* Switches forward packets based on rules
* Controller installs rules dynamically
* Path tracer reads flow rules
* Displays route taken by packets

👉 Similar to Google Maps tracking a route

---

## 📁 Project Structure

```
├── topology.py
├── controller.py
├── firewall.py
├── path_tracer.py
├── README.md
```

---

## 🎓 Viva Questions

* What is SDN?
* What is packet_in?
* What is a flow rule?
* Difference between match and action?
* What happens without controller?
* How does path tracing work?

---

## 📚 References

* https://mininet.org
* https://ryu.readthedocs.io

---

## 🧾 Conclusion

This project demonstrates how SDN enables:

* Centralized control
* Dynamic routing
* Enhanced network visibility

The Path Tracing Tool helps in understanding **how packets actually move inside a network**, making it a powerful learning and debugging tool.

---

## 👨‍💻 Author

Manoj Gaonkar

---
