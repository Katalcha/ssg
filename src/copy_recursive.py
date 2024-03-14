import os
import shutil

def copy_recursive(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        print(f"dest not existent, create folder")
        os.mkdir(dest_dir)

    for file in os.listdir(src_dir):
        print(f"copy from: {os.path.join(src_dir, file)} to: {os.path.join(dest_dir, file)}")
        
        if os.path.isfile(os.path.join(src_dir, file)):
            shutil.copy(os.path.join(src_dir, file), os.path.join(dest_dir, file))
        else:
            copy_recursive(os.path.join(src_dir, file), os.path.join(dest_dir, file))
