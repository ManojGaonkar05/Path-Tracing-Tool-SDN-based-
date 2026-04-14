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

1. Host sends packet (`ping`)
2. Switch sends **packet_in** to controller
3. Controller decides path
4. Flow rules are installed
5. Packets are forwarded
6. Path tracer displays route

---

## ✨ Features

* Dynamic path tracing
* Flow rule monitoring
* Real-time route display
* Firewall implementation
* Multiple test scenarios
* SDN-based intelligent routing

---

## 🛠️ Setup Instructions

### Install Mininet

```bash
sudo apt update
sudo apt install mininet -y
```

### Create Virtual Environment

```bash
python3.8 -m venv ryu-env
source ryu-env/bin/activate
```

### Install Ryu

```bash
pip install setuptools==58.0.4
pip install wheel
pip install ryu
```

---

## 🧹 Cleanup Before Running (Important)

```bash
sudo mn -c
```

### 💡 Why?

Removes old Mininet interfaces and prevents:

```
RTNETLINK answers: File exists
```

---

# ▶️ How to Run the Project

---

## 🔹 Scenario 1: Normal Forwarding + Path Tracing

### 🖥 Terminal 1 → Start Controller

```bash
ryu-manager controller.py
```

---

### 🖥 Terminal 2 → Run Topology

```bash
sudo mn -c
sudo python3 topology.py
```

Inside Mininet:

```bash
pingall
```

---

### 🖥 Terminal 3 → Run Path Tracer

```bash
sudo python3 path_tracer.py 10.0.0.1 10.0.0.2
```

---

## 🔹 Scenario 2: Firewall (Blocking H3)

### 🖥 Terminal 1 → Firewall Controller

```bash
ryu-manager firewall.py
```

---

### 🖥 Terminal 2 → Run Topology

```bash
sudo mn -c
sudo python3 topology.py
```

---

### 🖥 Terminal 2 (Mininet CLI) → Test

```bash
h1 ping h3   # FAIL
h1 ping h2   # SUCCESS
```

---

## 📊 Expected Output

### Path Tracing

```
10.0.0.1 → s1 → s2 → 10.0.0.2
```

### Firewall

```
Ping to H3: FAILED
Ping to H2: SUCCESS
```

---

## 📈 Performance Validation

```bash
ovs-ofctl dump-flows s1
```

---

## 🔍 How It Works

* Controller = brain
* Switch = forwarder
* Flow rules control traffic
* Path tracer reads flow tables

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
* Match vs Action?
* Role of controller?
* How path tracing works?

---

## 📚 References

* https://mininet.org
* https://ryu.readthedocs.io

---

## 🧾 Conclusion

This project demonstrates:

* Centralized control
* Dynamic routing
* Network visibility

---

## 👨‍💻 Author

Manoj Gaonkar

---
