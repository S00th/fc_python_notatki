####### ŚRODOWISKO WIRTUALNE
#
# W PyCharm mogę wybrać środowisko wirtualne (.venv)
# PyCharm narzuca nam tworzenie osobnego środowiska wirtualnego dla każdego projektu. Jest to dobra praktyka.
# W danym momencie możemy mieć na danym środowisku tylko jedną bibliotekę.
# Każdy projekty ma po to osobne środowisko wirtualne, aby odizolować się od innych.
#
# Python Global ENV jest zapisany
import sys
sys.executable # aby sprawdzić, gdzie jest zainstalowany "globalny" Python.

# Pakiety (biblioteki) różnią się wersjami.
# np. dla:
# projest_1, .venv1 – mamy: pandas 2.3, numby 2.1. request 2.22
# projest_2, .venv1 – mamy: opencv-python 4.1, numby 2.1. fastapi 1.1
# Jeżeli będę chciał uruchomić projekt_1 w środowisku??? z projektu_2, to wyświetli błąd.
# W takiej sytuacji wydzielamy "pokoje" dla każdego.
# Te środowiska wirtualne dla danego projektu, są właśnie takimi oddzielnymi pokojami.
# Izolujemy środowiska dla każdego pakietu, ....
# Proces wydzielania środowiska jest ...

# Środowisko wirtualne będzie za nas robił PyCharm, ale nie będziemy do końca świadomi, co się dzieje.
#