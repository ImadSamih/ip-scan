import sys
import socket
from ipwhois import IPWhois
from pprint import pprint

def get_ip_info(ip_address):
    # Get whois information
    try:
        obj = IPWhois(ip_address)
        whois_result = obj.lookup_rdap(depth=1)
        pprint(whois_result)
    except Exception as e:
        print(f"Failed to get WHOIS information: {e}")

    # Get DNS resolution
    try:
        host, aliases, addresses = socket.gethostbyaddr(ip_address)
        print(f"Hostname: {host}")
        print(f"Aliases: {aliases}")
        print(f"Addresses: {addresses}")
    except socket.herror:
        print("Failed to resolve IP address to a DNS name.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <ip_address>")
        sys.exit(1)

    ip = sys.argv[1]
    get_ip_info(ip)