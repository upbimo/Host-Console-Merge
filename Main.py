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
            print(f"Console of {host} is not reachable.")
    except Exception as e:
        # Handle any errors that may occur during console ping
        print(f"An error occurred while pinging console of {host}. Error: {e}")

if __name__ == "__main__":
    # Prompt the user to enter domains
    domains_input = input("Enter domains separated by space: ")
    domains = domains_input.split()

    # Ping the provided domains or hostnames
    for domain in domains:
        ping_domain(domain)

        # Create the console host by appending "-con"
        console_host = f"{domain.split('.')[0]}-con.{domain.split('.', 1)[1]}"
        ping_console_host(console_host)
