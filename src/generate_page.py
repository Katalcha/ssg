import os
from pathlib import Path
from md_to_md_blocks import markdown_to_html_node

def extract_title(md):
    md_lines = md.split("\n")
    for line in md_lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("Please add a valid h1 title to input markdown")

def generate_page(from_path, template_path, dest_path):
    print(f" using {from_path} and {template_path} to generate page in {dest_path}")
    from_file = open(from_path, "r")
    md_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(md_content)
    html = node.to_html()

    title = extract_title(md_content)
    template = template.replace("{{ title }}", title)
    template = template.replace("{{ content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path, template_path, dest_path):
    for file in os.listdir(dir_path):
        from_path = os.path.join(dir_path, file)
        to_path = os.path.join(dest_path, file)
        if os.path.isfile(from_path):
            to_path = Path(to_path).with_suffix(".html")
            generate_page(from_path, template_path, to_path)
        else: generate_pages_recursive(from_path, template_path, to_path)
