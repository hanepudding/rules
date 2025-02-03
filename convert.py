import os
from pathlib import Path
def convert_list_to_yaml(list_file, yaml_file):
    with open(list_file, 'r') as f:
        domains = f.readlines()

    with open(yaml_file, 'w') as f:
        f.write("payload:\n")
        for domain in domains:
            f.write(f"  - {domain.strip()}\n")

def main():
    list_dir = Path('D:/Workspace/git-repos/rules/list')
    yaml_dir = Path('D:/Workspace/git-repos/rules/yaml')

    if not os.path.exists(yaml_dir):
        os.makedirs(yaml_dir)

    for file_name in os.listdir(list_dir):
        if file_name.endswith('.list'):
            list_file_path = os.path.join(list_dir, file_name)
            yaml_file_path = os.path.join(yaml_dir, file_name.replace('.list', '.yaml'))
            convert_list_to_yaml(list_file_path, yaml_file_path)
            print(f"Converted {list_file_path} to {yaml_file_path}")

if __name__ == '__main__':
    main()
