import json
import os.path


class Udelezenec:
    def __init__(self, ime, priimek) -> None:
        self.ime = ime
        self.priimek = priimek


class Dogodek:
    def __init__(self, datum, udelezenci) -> None:
        self.datum = datum
        self.udelezenci = udelezenci


def v_seznam(objekt):
    """"Objekt 'udeleženec' zapiše v seznam v JSON datoteki."""

# Ali datoteka s seznamom že obstaja? 

    if os.path.isfile('seznam.json'):
        with open('seznam.json', 'r', encoding='utf-8') as dat:
            seznam = json.load(dat)

        seznam.append(objekt.__dict__)

        with open('seznam.json', 'w', encoding='utf-8') as dat:
            json.dump(seznam, dat, ensure_ascii=False, indent=4)

# Če ne obstaja, odpri novo in objekt dodaj v prazen seznam.

    else:
        with open('seznam.json', 'a', encoding='utf-8') as dat:
            seznam = []
            seznam.append(objekt.__dict__)
            json.dump(seznam, dat, ensure_ascii=False, indent=4)


def iz_seznama_v_dogodek(ime):
    """Iz seznama udeležencev v dogodek zapiše udeleženca, ki je bil prisoten."""

# Najprej v seznamu udeležencev poišče tistega, ki mu pripada ime. (Kaj pa če jih je več z istim imenom?)

    pass
