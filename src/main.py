import os
import shutil
from copy_recursive import copy_recursive
from generate_page import generate_pages_recursive

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
    generate_pages_recursive(dir_content, template, dir_public)
    print("done")
    
main()
