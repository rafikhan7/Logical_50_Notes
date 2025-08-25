import os
from typing import List, Tuple

TEN_MB = 10 * 1024 *1024 # 1o megabytes

def check_morethen_tenmb(folder_path, min_size_bytes:int=TEN_MB):
    file_path =""
    large_files:List[str]=[]
    for root, _dirs, files in os.walk(folder_path):
        for name in files:
            try:
                size= os.path.getsize(path)
            except:
                continue
            if size>min_size_bytes:
               large_files.append(path)
               
    return len(large_files), large_files
    
count, files =check_morethen_tenmb("path/file")
print("file>10 MB", count)
# print file name
for f in files:
    print(f)

