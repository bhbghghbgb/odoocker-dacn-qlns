# Read the first word of each line from dacn-auto-install.txt into a Python array
from ast import literal_eval
from pprint import pformat

# Read the first word of each line from dacn-auto-install.txt
with open("dacn-auto-install.txt", "r") as f:
    dependencies = set(line.split()[0] for line in f if line.strip())

# Path to the manifest file
manifest_base_file = "./custom-addons/dacn-auto-install/__manifest__.base.py"
manifest_dest_file = "./custom-addons/dacn-auto-install/__manifest__.py"

# Read and parse the manifest file
with open(manifest_base_file, "r") as f:
    manifest_content = f.read()
    manifest_data = literal_eval(manifest_content)

# Update the "depends" key with the new dependencies
if "depends" in manifest_data:
    manifest_data["depends"] = list(dependencies)

# Save the updated manifest file
with open(manifest_dest_file, "w") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write(pformat(manifest_data, indent=4))
    f.write("\n")
