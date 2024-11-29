# VLAN Testing Project (Based on W5500)

![W5500 Test](path/to/cover-image.png)

This project tests VLAN tagging and handling in **MACRAW mode** using the W5500 (Ethernet chip). It employs Python for data processing, Wireshark for packet capture

---

## 📋 Table of Contents

- [VLAN Testing Project (Based on W5500)](#vlan-testing-project-based-on-w5500)
  - [📋 Table of Contents](#-table-of-contents)
  - [🌟 Introduction](#-introduction)
  - [📂 Project Overview](#-project-overview)
  - [🛠️ Setup](#️-setup)
  - [🚀 How to Use](#-how-to-use)
  - [📊 Results](#-results)


---

## 🌟 Introduction

This project demonstrates how to send and receive VLAN-tagged Ethernet frames using the W5500 Ethernet chip in **MACRAW mode**. The workflow involves:

- Sending and receiving Ethernet frames with VLAN tags.
- Analyzing network traffic with Wireshark.
- Capturing and reviewing hardware signals using an oscilloscope.

---

## 📂 Project Overview

The project includes the following materials:

1. **Wireshark Capture Files**:
   - `.png` files for analyzing network traffic.
   - Example file: `data/vlan_test_capture.png`.

2. **Python Scripts**:
   - Scripts for generating data frames and controlling the W5500.
   - Example script: `./script/vlan.py`.


---

## 🛠️ Setup

Follow these steps to set up the project:

1. **Install Python**:
   - Python 3.7 or later is required.
   - Install the required packages:
     ```bash
     pip install pyserial scapy
     ```

2. **Install Wireshark**:
   - Download and install Wireshark from the [official website](https://www.wireshark.org/).

---

## 🚀 How to Use

1. **Run the Python Script**:
   - Generate VLAN-tagged frames and send them using the W5500:
     ```bash
     python ./script/vlan.py
     ```

2. **Analyze with Wireshark**:
   - Open Wireshark and capture packets from your network interface.
   - Apply a VLAN filter (`0x8100`) to isolate VLAN-tagged packets:
     ```
     vlan
     ```

---

## 📊 Results

1. **Wireshark Capture**:
   - Below is an example of VLAN-tagged packets captured with Wireshark:
     ![Wireshark VLAN Capture](images/wireshark_capture.png)



