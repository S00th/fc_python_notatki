####### Konwersja typu danych / Rzutowanie typów (Type casting)
# Jest to proces zamiany wartości z jednego typu danych (np. tekstu) na inny (np. liczbę całkowitą)


# Konwersja int na str
my_int = 123
int_to_str = str(my_int)
print(my_int, type(my_int), int_to_str, type(int_to_str))


# Konwersja str na int
my_str = '54321'
from_str_to_int = int(my_str)
print(my_str, type(my_str), from_str_to_int, type(from_str_to_int))


# Konwersja int na float
my_int2 = 4312
from_int2_to_float = float(my_int2)
print(my_int2, type(my_int2), from_int2_to_float, type(from_int2_to_float))

# Jeśli chcemy zamienić str = '123.45' na int, to najpierw musimy go zamienić na float, a następnie na int (str -> float -> int)


# Konwersja float na int
float_to_int = int(from_int2_to_float)
print(my_int2, type(my_int2), float_to_int, type(float_to_int))


# Konwersja float na str
float_like = 543.21
float_to_str = int(float_like)
print(float_like, type(float_like), float_to_str, type(float_to_str))


# Konwersja str na float
str_like = '123.45' # Jeśli chcesz zamienić TEKST na float, to musi się on składać wyłącznie z CYFR lub może zawierać KROPKĘ
str_to_float = float(str_like)
print(str_like, type(str_like), str_to_float, type(str_to_float))

invalid_int_like = '123a' # Jeśli chcesz zamienić TEKST na LICZBĘ, to musi się on składać wyłącznie z CYFR. W innym wypadku wyświetli się błąd.
from_invalid_str = int(invalid_int_like)
print(from_invalid_str, type(from_invalid_str))

float_like_str = '123.12' # Jeśli chcesz zamienić TEKST na float, to musi się on składać wyłącznie z CYFR i nie może zawierać KROPKI.
from_float_like = int(float_like_str)
print(from_float_like, type(from_float_like))



### ZADANIE
# Popraw poniższy kod

age = input('Ile masz lat? ')

if age >= 18:
    print('Możesz starać się o prawo jazdy.')
else:
    print('Nie możesz jeszcze starać się o prawo jazdy.')


# FUNKCJA "input" zawsze zwraca STRING, dlatego trzeba dokonać konwersji na "int" lub "float" (w tym przypadku "int").
# Możesz to zrobić w dwóch miejscach.

# Rozwiązanie 1

age = input('Ile masz lat? ')

if int(age) >= 18: # Konwersja na "int"
    print('Możesz starać się o prawo jazdy.')
else:
    print('Nie możesz jeszcze starać się o prawo jazdy.')

# Rozwiązanie 2

age = int(input('Ile masz lat? ')) # Konwersja na "int"

if age >= 18:
    print('Możesz starać się o prawo jazdy.')
else:
    print('Nie możesz jeszcze starać się o prawo jazdy.')


