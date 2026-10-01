# Network Diagnostics Tool

A lightweight, zero-dependency Python utility for quick cross-platform network troubleshooting. It tests host reachability, traces packet routing, and collects system network interface details in a single run.

---

## Features

- **Cross-Platform**: Automatically adapts commands for **Windows** (`tracert`, `ipconfig`) and **Linux / macOS** (`ping`, `traceroute`/`tracepath`, `ip`/`ifconfig`).
- **Zero External Dependencies**: Built entirely using Python's standard library (`subprocess`, `platform`, `shutil`).
- **All-in-One Report**: Runs reachability, routing, and interface checks sequentially and displays them in clean, readable sections.
- **Error Handling**: Gracefully reports command timeouts, missing system utilities, and failed lookups without crashing.

---

## Included Tests

| Test | Tool Used (Windows / Linux) | Purpose |
| :--- | :--- | :--- |
| **Ping** | `ping -n 4` / `ping -c 4` | Verifies host reachability, round-trip latency, and packet loss |
| **Traceroute** | `tracert` / `traceroute` or `tracepath` | Identifies network hops and path latency to the target |
| **Network Interfaces** | `ipconfig /all` / `ip addr` or `ifconfig` | Inspects local IP addresses, gateways, DNS, and adapters |

---

## Requirements

- **Python 3.7+**
- Standard OS network utilities (`ping`, `tracert`/`traceroute`, `ipconfig`/`ip`)

---

## Quick Start

### 1. Clone or Download the Repository
```bash
git clone https://github.com/yourusername/diagnose-network.git
cd diagnose-network
```

### 2. Run Diagnostics
Run `main.py` with a domain name or IP address as the argument:

```bash
# Using a domain name
python main.py google.com

# Using an IP address
python main.py 1.1.1.1
```

*(On Linux / macOS, use `python3 main.py <host>`)*

---

## Sample Output

```text
Running network diagnostics for 'google.com'...

============================================================
 PING TEST (google.com)
============================================================
Pinging google.com [142.250.190.46] with 32 bytes of data:
Reply from 142.250.190.46: bytes=32 time=14ms TTL=117
...
Ping statistics for 142.250.190.46:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)

============================================================
 TRACEROUTE (google.com)
============================================================
Tracing route to google.com [142.250.190.46] over a maximum of 30 hops:
  1    <1 ms    <1 ms    <1 ms  192.168.1.1
  2    12 ms    11 ms    13 ms  142.250.190.46
Trace complete.

============================================================
 NETWORK INTERFACE DIAGNOSTIC
============================================================
Windows IP Configuration / IP Address Details...
```

---

## Troubleshooting

- **Command Not Found**: Ensure standard networking tools are installed on Linux (`sudo apt install iputils-ping traceroute iproute2` on Debian/Ubuntu).
- **Traceroute Slow or Blocked**: Some intermediate routers or firewalls drop ICMP/UDP traceroute packets, which may result in asterisks (`*`) or timeouts. This is normal network behavior.
- **Administrative Privileges**: Certain diagnostic flags on Linux may require elevated permissions (`sudo python3 main.py <host>`).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
