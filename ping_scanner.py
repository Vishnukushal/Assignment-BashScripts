import subprocess
import platform
import re

def ping_host(host):
    os_name = platform.system().lower()

    if os_name == "windows":
        param = "-n"
    else:
        param = "-c"

    try:
        result = subprocess.run(
            ["ping", param, "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        output = result.stdout

        if result.returncode == 0:
            avg_time = extract_avg_time(output, os_name)
            print(f"\nHost: {host}")
            print("Status: Reachable")
            if avg_time:
                print("Average Time:", avg_time)
        else:
            print(f"\nHost: {host}")
            print("Status: Unreachable")

    except subprocess.TimeoutExpired:
        print(f"\nHost: {host}")
        print("Error: Request Timed Out")

def extract_avg_time(output, os_name):
    try:
        if os_name == "windows":
            match = re.search(r"Average = (\d+)ms", output)
        else:
            match = re.search(r"avg\/.*? = .*?\/(.*?)\/", output)

        if match:
            return match.group(1) + " ms"
    except:
        return None

def multiple_scan():
    hosts = input("Enter multiple IP/hostnames (comma separated): ")
    host_list = hosts.split(",")

    for host in host_list:
        ping_host(host.strip())

if __name__ == "__main__":
    print("=== Ping Scanner ===")

    choice = input("Ping single host? (y/n): ")

    if choice.lower() == "y":
        host = input("Enter hostname or IP: ")
        ping_host(host)
    else:
        multiple_scan()
