import os

root = 'data'
data_dir = os.listdir(root)
file_paths = [f'{root}/{filename}' for filename in data_dir]
files_content = []

for file_path in file_paths:
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
        files_content.append(content)

# print(files_content)
print(files_content[0]) #
