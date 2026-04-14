# 🚀 SDN Path Tracing Tool (Mininet + Ryu + OpenFlow)

## 📌 Project Overview

The **SDN Path Tracing Tool** is a Software Defined Networking (SDN) based application designed to **identify, track, and display the path taken by packets** across a network.

The project uses:

* **Mininet** → to simulate network topology
* **Ryu Controller** → to control network behavior
* **OpenFlow Protocol** → to install and manage flow rules

This tool provides **visibility into packet forwarding decisions**, which is not possible in traditional networks.

---

## 🎯 Problem Statement

To design and implement a system that:

* Tracks packet flow in an SDN network
* Identifies forwarding paths dynamically
* Displays the route taken by packets
* Validates behavior using test scenarios

---

## 🧠 Key Concepts Used

* Software Defined Networking (SDN)
* OpenFlow (match-action flow rules)
* Packet_in / Packet_out handling
* Flow table management
* Network topology simulation

---

## 🏗️ Architecture

### Components:

1. **Hosts (H1, H2, H3)**

   * Generate and receive traffic

2. **Switches (S1, S2, S3)**

   * Forward packets based on flow rules

3. **Ryu Controller**

   * Acts as the brain of the network
   * Installs flow rules dynamically

4. **Path Tracer Module**

   * Tracks and displays packet path

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

### Step 1: Packet Generation

A host sends a packet (e.g., `h1 ping h2`)

### Step 2: Packet-In Event

* Switch does not have a rule
* Sends **packet_in** request to controller

### Step 3: Controller Decision

* Ryu controller analyzes packet
* Determines correct forwarding path

### Step 4: Flow Rule Installation

Controller installs rule:

```
Match: src IP, dst IP
Action: forward to specific port
```

### Step 5: Packet Forwarding

* Switch forwards packet using installed rules
* Future packets follow same path directly

### Step 6: Path Tracing

* Path tracer extracts flow rules
* Displays full route:

```
10.0.0.1 → s1 → s2 → 10.0.0.2
```

---

## ✨ Features

* ✅ Dynamic path tracing
* ✅ Flow rule monitoring
* ✅ Real-time route display
* ✅ Firewall functionality (blocking hosts)
* ✅ Test scenario validation
* ✅ SDN-based intelligent routing

---

## 🛠️ Setup Instructions

### 1. Install Mininet

```bash
sudo apt update
sudo apt install mininet -y
```

### 2. Setup Python Environment (Recommended)

```bash
python3.8 -m venv ryu-env
source ryu-env/bin/activate
```

### 3. Install Ryu

```bash
pip install setuptools==58.0.4
pip install wheel
pip install ryu
```

---

## ▶️ How to Run the Project

---

### 🔹 Scenario 1: Normal Forwarding + Path Tracing

#### Terminal 1 (Controller)

```bash
ryu-manager controller.py
```

#### Terminal 2 (Topology)

```bash
sudo python3 topology.py
```

#### Mininet CLI

```bash
pingall
```

#### Terminal 3 (Path Tracer)

```bash
sudo python3 path_tracer.py 10.0.0.1 10.0.0.2
```

---

### 🔹 Scenario 2: Firewall (Blocking H3)

#### Terminal 1

```bash
ryu-manager firewall.py
```

#### Terminal 2

```bash
sudo python3 topology.py
```

#### Mininet CLI

```bash
h1 ping h3   # Expected: FAIL
h1 ping h2   # Expected: SUCCESS
```

---

## 📊 Expected Output

### ✅ Path Tracing Output

```
Packet Path:
10.0.0.1 → s1 → s2 → 10.0.0.2
```

### ✅ Firewall Output

```
Ping to H3: FAILED
Ping to H2: SUCCESS
```

---

## 📈 Performance Validation

* **Ping Test** → Measures latency
* **Iperf Test** → Measures throughput
* **Flow Table Inspection** → Using:

```bash
ovs-ofctl dump-flows s1
```

---

## 🔍 How It Works (Simple Explanation)

* The **controller acts like a brain**
* Switches ask controller what to do
* Controller installs rules
* Path tracer reads those rules
* Displays how packets travel

👉 Similar to **Google Maps tracking route of a car**

---

## 📁 Project Structure

```
├── topology.py        # Network topology
├── controller.py      # Ryu controller logic
├── firewall.py        # Firewall implementation
├── path_tracer.py     # Path tracing logic
├── README.md
```

---

## 🎓 Viva Preparation (Important Questions)

* What is SDN?
* What is packet_in?
* How are flow rules installed?
* Difference between match and action?
* What happens without controller?
* How does your path tracing work?

---

## 📚 References

* https://mininet.org
* https://ryu.readthedocs.io

---

## 🧾 Conclusion

This project demonstrates how SDN enables:

* Centralized control
* Dynamic routing
* Better network visibility

The Path Tracing Tool enhances understanding of **internal network behavior** and provides a practical implementation of SDN concepts.

---

## 👨‍💻 Author

Manoj Gaonkar

---
