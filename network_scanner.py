import os

def menu():
    print("\n=== Unified Network Scanner ===")
    print("1. Ping Scanner")
    print("2. ARP Scanner")
    print("3. Nmap Scanner")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        os.system("python3 ping_scanner.py")

    elif choice == "2":
        os.system("python3 arp_scanner.py")

    elif choice == "3":
        os.system("python3 nmap_scanner.py")

    elif choice == "4":
        print("Exiting...")
        exit()

    else:
        print("Invalid choice")

while True:
    menu()
