import subprocess
import re
import platform

def get_arp_table():
    os_name = platform.system().lower()

    try:
        if os_name == "windows":
            command = ["arp", "-a"]
        else:
            command = ["arp", "-a"]

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        return result.stdout

    except subprocess.TimeoutExpired:
        print("Error: ARP command timed out")
        return None

def parse_arp_output(output):
    pattern = r"\((\d+\.\d+\.\d+\.\d+)\)\s+at\s+([0-9a-fA-F:]{17})"
    matches = re.findall(pattern, output)

    return matches

def display_results(entries):
    print("\nIP Address\t\tMAC Address")
    print("---------------------------------------------")

    for ip, mac in entries:
        print(f"{ip}\t\t{mac}")

    print("\nTotal entries:", len(entries))

def save_to_file(entries):
    choice = input("Save results to file? (y/n): ")

    if choice.lower() == "y":
        with open("arp_results.txt", "w") as f:
            for ip, mac in entries:
                f.write(f"{ip}\t{mac}\n")
        print("Results saved to arp_results.txt")

if __name__ == "__main__":
    print("=== ARP Scanner ===")
    print("Scanning ARP table...")

    output = get_arp_table()

    if output:
        entries = parse_arp_output(output)
        display_results(entries)
        save_to_file(entries)
    else:
        print("Failed to retrieve ARP table")
