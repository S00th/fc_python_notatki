import json

person1 = {
    "imie": "Danusia",
    "nazwisko": "Kowalska",
    "wiek": 35,
    "zawod": "HR",
    "adres": {
        "ulica": "Czekoladowa",
        "nr_budynku": "12a",
        "kod_pocztowy": "50-500",
        "miasto": "Wrocław"
    },
    "hobby": {
        "nazwa": "Siatkówka",
        "ile_h_per_tydzien": 5,
        "zespol": ["Kamila", "Dawin", "Kasia"]
    },
    "partner": {
        "imie": "Tomek",
        "wiek": 40,
        "Płeć": "M",
        "czy_ma_auto": False
    },
}

json_data = json.dumps(person1)
print(json_data)
print(type(json_data))