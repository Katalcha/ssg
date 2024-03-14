import os
import shutil
from copy_recursive import copy_recursive

dir_static = "./static"
dir_public = "./public"

def main():
    print("deleting public dir")
    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)
        print("done deleting")
    print("copy static files to public dir")
    copy_recursive(dir_static, dir_public)
    
main()
