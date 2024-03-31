# Import hashlib library (md5 method is part of it)
import hashlib

# File to check
file_name = '/home/jaemin/crypto_python/gitToken'

# Correct original md5 goes here
original_md5 = 'fab30931d7a177605d0bf1f4f331c3c2'  

# Open,close, read file and calculate MD5 on its contents 
with open(file_name, 'rb') as file_to_check:
    # read contents of the file
    data = file_to_check.read()    
    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()

# Finally compare original MD5 with freshly calculated
if original_md5 == md5_returned:
    print("MD5 verified.")
else:
    print("MD5 verification failed!.")