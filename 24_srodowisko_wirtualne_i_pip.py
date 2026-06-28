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