####### ŚRODOWISKO WIRTUALNE
#
# W PyCharm mogę wybrać środowisko wirtualne (.venv)
# PyCharm narzuca nam tworzenie osobnego środowiska wirtualnego dla każdego projektu. Jest to dobra praktyka.
# W danym momencie możemy mieć na danym środowisku tylko jedną bibliotekę.
# Każdy projekty ma po to osobne środowisko wirtualne, aby odizolować się od innych.
#
# Sprawdź, jakiego Pythona aktualnie używasz.
# W wierszu poleceń wpisz:
python
# a następnie
>>> import sys
>>> sys.executable

# W zależności od tego, czy będziemy w środowisku wirtualnym, czy globalnym wyświetli:
# Y:\\Py\\projekt2\\my_venv2\\Scripts\\python.exe # dla środowiska wirtualnego
# lub
# C:\\Users\\szymo\\AppData\\Local\\Programs\\Python\\Python314\\python.exe # dla Global ENV

# Pakiet to zbiór skryptów, modułów, które zawierają kod i definicję funkcji.
# Pakiety (biblioteki) różnią się wersjami.
# np. dla:
# – project_1,.venv1 – mamy: pandas 2.3, numpy 2.1. requests 2.22
# – project_2,.venv1 – mamy: opencv-python 4.1, numpy 2.1. fastapi 0.1
# Jeżeli będę chciał uruchomić projekt_1 pythonem z projektu_2, to mogę otrzymać błąd.
# Właśnie dlatego wydzielamy oddzielne wirtualne środowiska / "pokoje" dla każdego projektu.
# Środowiska wirtualne dla danego projektu, są właśnie takimi oddzielnymi pokojami.
# Jest pokój, który jest częścią wspólną, ale każdy ma też wydzielony swój oddzielny pokój, w którym pracuje.
# Izolujemy środowiska od siebie, aby nei było konfliktu w bibliotekach.
# Proces wydzielania środowiska wirtualnego od środowiska globalnego nie stanowi ubytku dla środowiska globalnego.

# Środowisko wirtualne będzie za nas robił PyCharm, ale nie będziemy do końca świadomi, co się dzieje.
# Pozostał w informacje o tym, ja tworzyć środowisko wirtualne w pliku: 0_notes.txt



####### ZADANIE
#
# Przejdź do katalogu projektu.
# – Utwórz środowisko wirtualne o nazwie
# – Aktywuj środowisko.
# Sprawdź:
# – wersję Pythona
# – lokalizację interpretera za pomocą programu
# – Utwórz plik main.py
# – W pliku main wypisz wersje biblioteki oraz wyświetl w konsoli informacje "to jest projekt A"
# – Uruchom program
# Aby wyświetlić wersję biblioteki (requests) wpisz:

import requests
print(requests.__version__)
print('To jest projekt 1.')


# Utwórz nowy katalog projekt2 Utwórz w nim nowe środowisko:
# – Aktywuj środowisko.
# – Sprawdź wersje pythona i lokalizację środowiska
# – Zainstaluj pakiet scikit-learn
# – Utwórz plik main.py
# – W pliku main wypisz wersje biblioteki oraz wyświetl w konsoli informacje "to jest projekt A"
# – Uruchom program
# Aby wyświetlić wersję biblioteki (requests) wpisz:

import requests
print(requests.__version__)
print('To jest projekt 2.')

# Importowanie z biblioteki sci-kit z modulu metrics funkcjonalnosc accuracy_score
from sklearn.metrics import accuracy_score

y_true = [0, 1, 0, 0, 1]
y_pred = [0, 0, 0, 1, 1]
print(accuracy_score(y_true, y_pred))
print(sklearn.__version__)
print('To jest projekt 2.')

# Etykiety prawdziwe
# Etykiety

# Jeżeli będe chciał uruchomić program znajdujący się w katalogu projekt1, mając aktywne środowisko projekt2,
# to pojawi się błąd.