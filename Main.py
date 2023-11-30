import os
import socket
import argparse

# Function to ping a domain
def ping_domain(domain):
    try:
        # Resolve the IP address of the domain
        ip_address = socket.gethostbyname(domain)
        # Print the result
        print(f"{domain} is reachable. IP address: {ip_address}")
    except socket.error as e:
        # Handle the case when the domain cannot be resolved
        print(f"Unable to resolve {domain}. Error: {e}")

# Function to ping the console of a host
def ping_console_host(host):
    try:
        # Use the 'ping' command to check the reachability of the console
        response = os.system(f"ping {host}")
        if response == 0:
            print(f"Console of {host} is reachable.")
        else:
            print(f"Unable to reach the console of {host}.")
    except Exception as e:
        # Handle any errors that may occur during console ping
        print(f"An error occurred while pinging console of {host}. Error: {e}")

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Ping a domain and optionally the console of a host.")
    # Define command-line arguments
    parser.add_argument("domain", nargs='?', help="Domain to ping")
    parser.add_argument("-con", "--console", help="Ping the console of the specified host", metavar="host")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if neither domain nor console is provided
    if not args.domain and not args.console:
        # Prompt the user to enter a domain
        domain_to_ping = input("Enter the domain to ping: ")
        # Ping the entered domain
        ping_domain(domain_to_ping)
    else:
        # Use the provided domain or console argument
        domain_to_ping = args.domain
        # Ping the domain
        ping_domain(domain_to_ping)

    # Check if the console argument is provided
    if args.console:
        # Use the provided console argument
        console_host = args.console
        # Ping the console of the specified host
        ping_console_host(console_host)
