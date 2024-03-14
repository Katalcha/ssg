import os
import shutil
from copy_recursive import copy_recursive
from generate_page import generate_page

dir_static = "./static"
dir_public = "./public"
dir_content = "./content"
template = "./template.html"

def main():
    print("delete public dir")
    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)
    print("copy files from static to public dir")
    copy_recursive(dir_static, dir_public)
    print("generate page")
    generate_from = os.path.join(dir_content, "index.md")
    generate_to = os.path.join(dir_public, "index.html")
    generate_page(generate_from, template, generate_to)
    print("done")
    
main()
