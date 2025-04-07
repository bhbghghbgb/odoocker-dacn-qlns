# Read the first word of each line from dacn-auto-install.txt into a Python array
from pprint import pformat

# Read the first word of each line from dacn-auto-install.txt
with open("dacn-auto-install.txt", "r") as f:
    dependencies = set(line.split()[0] for line in f if line.strip())

# Path to the manifest file
manifest_dest_file = "./custom-addons/dacn-auto-install/__manifest__.py"

manifest_data = {
    "application": False,
    "author": "DACN QLNS SGU",
    "auto_install": False,
    "category": "Customizations",
    "company": "DACN QLNS SGU",
    "data": [],
    "demo": [],
    "depends": ["base"],
    "description": "Module nay dung de tu dong cai cac module can thiet khi "
    "tao database cho do an chuyen nganh quan ly nhan su Odoo.",
    "images": ["static/description/cover.svg"],
    "installable": True,
    "license": "Other OSI approved licence",
    "live_test_url": "",
    "maintainer": "DACN QLNS SGU",
    "name": "DACN QLNS SGU auto-install",
    "summary": "Auto install modules for DACN QLNS SGU",
    "version": "17.0.1.0.0",
    "website": "https://github.com/bhbghghbgb/odoocker-dacn-qlns",
}

# Update the "depends" key with the new dependencies
manifest_data["depends"] += sorted(dependencies)

# Save the updated manifest file
with open(manifest_dest_file, "w") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write(pformat(manifest_data, indent=4))
    f.write("\n")
