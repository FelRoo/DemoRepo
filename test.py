import os

file_name = 'index.html'

if os.path.isfile(file_name):

    if file_name.endswith('.html'):
        print(f"'{file_name}' exists and ends with '.html'.")
    else:
        print(f"'{file_name}' exists but does not end with '.html'.")
else:
    print(f"'{file_name}' does not exist.")