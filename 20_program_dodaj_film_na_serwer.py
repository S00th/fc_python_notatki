# Napisz program, który symuluje dodawanie filmów do serwera.
# Każdy film ma podany rozmiar w MB.
#
# Po uruchomieniu programu:
#   1) Program pyta: "Ile filmów chcesz dodać?"
#   2) Następnie wczytuje rozmiar każdego filmu (w MB).
#
# ZASADY:
# - Rozmiar filmu musi być w zakresie od 100 MB do 3000 MB.
# - Jeśli użytkownik poda rozmiar < 100 lub > 3000 MB,
#     → program NATYCHMIAST przerywa wczytywanie
#     → i przechodzi do podsumowania.
#
# - Serwer zapisuje filmy do tzw. SLOTÓW o pojemności 10 000 MB.
# - Filmy dodawane są kolejno:
#       → jeśli kolejny film się mieści — dodaj go
#       → jeśli NIE mieści się — obecny slot zostaje zamknięty,
#         a film trafia do nowego slotu
#
# PODSUMOWANIE, które ma wypisać program:
#   1) Ile slotów utworzono.
#   2) Ile MB łącznie zapisano.
#   3) Ile łącznie było "pustej przestrzeni":
#        pustka = liczba_slotów * 10000 - suma_MB
#   4) Który slot miał najwięcej pustego miejsca oraz ile to było MB.

# DANE WEJŚCIOWE: ilość filmów, rozmiar każdego filmu w MB
# DANE WYJŚCIOWE:
#   1) Ile slotów utworzono.
#   2) Ile MB łącznie zapisano.
#   3) Ile łącznie było "pustej przestrzeni":
#       pustka = liczba_slotów * 10000 - suma_MB
#   4) Który slot miał najwięcej pustego miejsca oraz ile to było MB.


