from os.path import join
import os
import shutil

current_dir = os.getcwd()

for f in os.listdir(current_dir):
    
    file_name, file_ext = os.path.splitext(f)
    #print(file_name, file_ext)

    try:
        if not file_ext:
            pass
        elif file_ext in (".pdf"):
            # print(file_name, file_ext)
            v = os.path.join(current_dir, f'{file_name}{file_ext}')
            w = os.path.join(current_dir, 'Pdf Files', f'{file_name}{file_ext}')
            
            dest = shutil.move(v, w)
            print(dest)



    except (FileNotFoundError, PermissionError):
        pass
