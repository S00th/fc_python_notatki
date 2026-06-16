# Praca na WIELU plikach
#
# Mając kolekcję ścieżek, trzeba będzie przeiterować się przez wszystkie pliki.
# Nie ważne, na jakich plikach pracujemy (txt, csv, exel itp.)
# Możemy to zrobić na 2 sposoby.

import os

root = 'data2'
data_dir = os.listdir(root)
file_paths = [f'{root}/{filename}' for filename in data_dir] # Gdzie filename to nazwa każdego pliku


files_content = []
for file_path in file_paths:
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
        files_content.append(content)

print(files_content)