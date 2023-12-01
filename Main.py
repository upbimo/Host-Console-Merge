import os
import socket

# Function to ping a domain
def ping_domain(domain):
    try:
        # Use the 'ping' command to check the reachability of the domain
        response = os.system(f"ping {domain}")
        print(f"Pinging {domain} with 32 bytes of data:")
        print(response)
        return response == 0  # Return True if the host is reachable, False otherwise
    except Exception as e:
        # Handle any errors that may occur during domain ping
        print(f"An error occurred while pinging {domain}. Error: {e}")
        return False

# Function to ping the console of a host
def ping_console_host(host):
    try:
        # Use the 'ping' command to check the reachability of the console
        response = os.system(f"ping {host}")
        print(f"Pinging {host} with 32 bytes of data:")
        print(response)
        return response == 0  # Return True if the console is reachable, False otherwise
    except Exception as e:
        # Handle any errors that may occur during console ping
        print(f"An error occurred while pinging console of {host}. Error: {e}")
        return False

if __name__ == "__main__":
    # Prompt the user to enter domains
    domains_input = input("Enter domains separated by space: ")
    domains = domains_input.split()

    # Initialize lists to track failed pings
    failed_host_pings = []
    failed_console_pings = []

    # Iterate over each domain and ping the host first, then the console
    for domain in domains:
        # Ping the host
        host_reachable = ping_domain(domain)
        if not host_reachable:
            failed_host_pings.append((domain, "host"))

        # Create the console host by appending "-con"
        console_host = f"{domain.split('.')[0]}-con.{domain.split('.', 1)[1]}"

        # Ping the console host
        console_reachable = ping_console_host(console_host)
        if not console_reachable:
            failed_console_pings.append((console_host, "console"))

        # Add a newline for better readability between each set of pings
        print()

    # Print overall reachability summary
    if not failed_host_pings:
        print("All hosts are reachable.")
    else:
        print("Failed to reach the following hosts:")
        for host, _ in failed_host_pings:
            print(f"{host} (host)")

    if not failed_console_pings:
        print("All consoles are reachable.")
    else:
        print("Failed to reach the following consoles:")
        for console, _ in failed_console_pings:
            print(f"{console} (console)")
