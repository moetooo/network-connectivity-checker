import platform
import shutil
import subprocess
import sys

IS_WINDOWS = platform.system().lower() == "windows"


def run_and_stream(cmd, title):
    """Prints a section header and streams command output live in real time."""
    separator = "=" * 60
    print(f"\n{separator}\n {title.upper()}\n{separator}")
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        for line in process.stdout:
            print(line, end="", flush=True)
        process.wait()
    except FileNotFoundError:
        print(f"Command not found: '{cmd[0]}'. Please ensure it is installed and in your PATH.")
    except Exception as e:
        print(f"Error executing command: {e}")


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <host>")
        print("Example: python main.py google.com")
        sys.exit(1)

    host = sys.argv[1]
    print(f"Starting network diagnostics for '{host}'...")

    # 1. Ping test
    ping_param = "-n" if IS_WINDOWS else "-c"
    run_and_stream(["ping", ping_param, "4", host], f"Ping Test ({host})")

    # 2. Traceroute test (using -d / -n to avoid slow reverse DNS lookups on intermediate hops)
    if IS_WINDOWS:
        trace_cmd = ["tracert", "-d", "-h", "20", host]
    else:
        tool = "traceroute" if shutil.which("traceroute") else "tracepath"
        trace_cmd = [tool, "-n", "-m", "20", host] if tool == "traceroute" else [tool, "-m", "20", host]
    run_and_stream(trace_cmd, f"Traceroute ({host})")

    # 3. Network interface information
    if IS_WINDOWS:
        net_cmd = ["ipconfig", "/all"]
    else:
        net_cmd = ["ip", "addr"] if shutil.which("ip") else ["ifconfig"]
    run_and_stream(net_cmd, "Network Interface Diagnostic")

    print("\nDiagnostics complete.")


if __name__ == "__main__":
    main()
