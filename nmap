import subprocess
import shutil

def check_nmap():
    if shutil.which("nmap") is None:
        print("Nmap is not installed.")
        return False
    else:
        print("Nmap is installed.")
        return True

def run_scan(target, scan_type):
    if scan_type == "1":
        command = ["nmap", "-sn", target]
    elif scan_type == "2":
        command = ["nmap", target]
    elif scan_type == "3":
        ports = input("Enter custom port range (example 20-100): ")
        command = ["nmap", "-p", ports, target]
    elif scan_type == "4":
        command = ["nmap", "-sV", target]
    elif scan_type == "5":
        command = ["sudo", "nmap", "-O", target]
    else:
        print("Invalid choice")
        return None

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=120
        )
        return result.stdout

    except subprocess.TimeoutExpired:
        print("Scan timed out.")
        return None

def save_results(data):
    choice = input("Save results to file? (y/n): ")
    if choice.lower() == "y":
        with open("nmap_results.txt", "w") as f:
            f.write(data)
        print("Results saved to nmap_results.txt")

if __name__ == "__main__":
    print("=== Nmap Scanner ===")

    if check_nmap():
        target = input("Enter target IP / hostname: ")

        print("\nSelect Scan Type")
        print("1. Host Discovery (-sn)")
        print("2. Port Scan (default)")
        print("3. Custom Port Scan")
        print("4. Service Version Detection (-sV)")
        print("5. OS Detection (-O)")

        choice = input("Enter choice (1-5): ")

        print("\nScanning... please wait\n")

        output = run_scan(target, choice)

        if output:
            print(output)
            save_results(output)
