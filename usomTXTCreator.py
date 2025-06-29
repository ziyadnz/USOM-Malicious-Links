import requests
import re

# URL of the text file
url = 'https://www.usom.gov.tr/url-list.txt'

# Function to fetch the content from the URL
def fetch_url_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Function to separate IP addresses and domain names
def separate_ip_and_domain(lines):
    ip_pattern = re.compile(r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)')
    ip_addresses = []
    domains = []

    for line in lines:
        line = line.strip()
        if ip_pattern.match(line):
            ip_addresses.append(line)
        else:
            domains.append(line)

    return ip_addresses, domains

# Function to write to files
def write_to_files(ip_addresses, domains):
    with open('ipv4.txt', 'w') as ip_file:
        for ip in ip_addresses:
            ip_file.write(ip.split('/')[0] + '\n')

    with open('domain.txt', 'w') as domain_file:
        domain_file.write("type=string"+'\n')
        for domain in domains:
            domain_file.write(domain.split('/')[0] + '\n')


    with open('domainforFW.txt', 'w') as domain_file:
        for domain in domains:
            domain_file.write(domain.split('/')[0] + '\n')

# Main function
def main():
    content = fetch_url_content(url)
    lines = content.splitlines()


    
    # Get the first 5000 lines
    latest_lines = lines[:5000:]
    
    # Separate IPs and Domains
    ip_addresses, domains = separate_ip_and_domain(latest_lines)
    
    # Write to files
    write_to_files(ip_addresses, domains)
    
    print("IP Addresses and Domains have been written to ipv4.txt and domain.txt respectively.")

if __name__ == "__main__":
    main()
