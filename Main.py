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

# Function to add the "-con" prefix after the numbers in the middle of a host
def add_console_prefix_in_middle(host):
    # Split the host into parts based on numbers
    parts = ["".join(g) for k, g in groupby(host, str.isdigit)]

    if len(parts) > 1:
        # Insert "-con" after the numbers in the middle
        middle_index = len(parts) // 2
        parts[middle_index] = f"{parts[middle_index]}-con"
        return '.'.join(parts)
    else:
        # Check if there are numbers at the end, and insert "-con" before the dot
        index_dot = host.rfind('.')
        if index_dot != -1 and host[index_dot+1:].isdigit():
            return f"{host[:index_dot]}-con{host[index_dot:]}"
        else:
            return f"{host}-con"

# Import groupby from itertools
from itertools import groupby

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
        # Add the "-con" prefix after the numbers in the middle of the console host
        console_host_with_prefix = add_console_prefix_in_middle(console_host)
        # Ping the console of the specified host
        ping_console_host(console_host_with_prefix)
