import requests
import re
from urllib.parse import urlparse

# URL of the text file
url = 'https://www.usom.gov.tr/url-list.txt'

# Function to fetch the content from the URL
def fetch_url_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Function to extract domain or IP from URL
def extract_host(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Function to separate IP addresses and domain names
def separate_ip_and_domain(lines):
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    ip_addresses = set()  # Use a set to avoid duplicates
    domains = set()  # Use a set to avoid duplicates

    for line in lines:
        line = line.strip()
        host = extract_host(line)
        if ip_pattern.match(host):
            ip_addresses.add(host)
        else:
            domains.add(host)

    return list(ip_addresses), list(domains)

# Function to write to files
def write_to_files(ip_addresses, domains):
    with open('ipv4.txt', 'w') as ip_file:
        for ip in ip_addresses:
            ip_file.write(ip + '\n')

    with open('domain.txt', 'w') as domain_file:
        for domain in domains:
            domain_file.write(domain + '\n')

# Main function
def main():
    content = fetch_url_content(url)
    lines = content.splitlines()
    
    # Get the latest 100 lines
    latest_lines = lines[-100:]
    
    # Separate IPs and Domains
    ip_addresses, domains = separate_ip_and_domain(latest_lines)
    
    # Write to files
    write_to_files(ip_addresses, domains)
    
    print("IP Addresses and Domains have been written to ipv4.txt and domain.txt respectively.")

if __name__ == "__main__":
    main()
