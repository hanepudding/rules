import json

# Function to convert input rules from a text file to a structured JSON format
def convert_rules(input_file, output_file):
    # Open the input file in read mode
    with open(input_file, 'r') as f:
        lines = f.readlines()  # Read all lines from the file into a list

    domain_suffixes = []  # Initialize an empty list to store domain suffixes
    ip_cidrs = []  # Initialize an empty list to store IP CIDR rules

    for line in lines:
        line = line.strip()
        # Check if the line starts with "DOMAIN-SUFFIX"
        if line.startswith("DOMAIN-SUFFIX"):
            # Split the line by the first comma, and extract the domain part
            parts = line.split(',', 1)
            if len(parts) == 2:
                domain = parts[1]
                # Append the extracted domain to the domain_suffixes list
                domain_suffixes.append(domain)
        # Check if the line starts with "IP-CIDR" or "IP-CIDR6"
        elif line.startswith("IP-CIDR") or line.startswith("IP-CIDR6"):
            # Split the line by the first comma, and extract the CIDR part
            parts = line.split(',', 1)
            if len(parts) >= 2:
                ip_cidr = parts[1].split(',')[0]  # Extract the CIDR part before any additional options
                # Append the extracted CIDR to the ip_cidrs list
                ip_cidrs.append(ip_cidr)

    # Create the rules dictionary with the required JSON structure
    rules = {
        "version": 1,  # Version number for the JSON output (can be modified if needed)
        "rules": []
    }

    # Add domain_suffix rules if there are any
    if domain_suffixes:
        rules["rules"].append({
            "domain_suffix": domain_suffixes
        })

    # Add ip_cidr rules if there are any
    if ip_cidrs:
        rules["rules"].append({
            "ip_cidr": ip_cidrs
        })

    # Open the output file in write mode and write the JSON data to it
    with open(output_file, 'w') as f:
        json.dump(rules, f, indent=2)  # Dump the JSON data with an indentation of 2 spaces for readability

def main():
    import os
    for file in os.listdir('./list'):
        if file.endswith('.list'):
            convert_rules(f'./list/{file}', f'./json/{file.replace(".list", ".json")}')

if __name__ == '__main__':
    main()