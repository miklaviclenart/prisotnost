import json

class Udelezenec:
    def __init__(self, ime, priimek) -> None:
        self.ime = ime
        self.priimek = priimek


class Dogodek:
    def __init__(self, datum, udelezenci) -> None:
        self.datum = datum
        self.udelezenci = udelezenci


def v_seznam(objekt, ime_datoteke):
    """"Objekt 'udeleženec' zapiše v seznam v JSON datoteki."""

# Ali datoteka s seznamom že obstaja? 

    try:
        with open(ime_datoteke, 'r', encoding='utf-8') as dat:
            seznam = json.load(dat)

        seznam.append(objekt.__dict__)

        with open(ime_datoteke, 'w', encoding='utf-8') as dat:
            json.dump(seznam, dat, ensure_ascii=False, indent=4)

# Če ne obstaja, odpri novo in objekt dodaj v prazen seznam.

    except FileNotFoundError:
        with open(ime_datoteke, 'a', encoding='utf-8') as dat:
            seznam = []
            seznam.append(objekt.__dict__)
            json.dump(seznam, dat, ensure_ascii=False, indent=4)


def prisotni(manjkajoci):
    """Vrne seznam vseh prosotnih, t.j. vseh v 'seznam.json' datoteki, ki jih ne navedemo v seznamu 'manjkajoci'."""
    with open('seznam.json', 'r', encoding='utf-8') as dat:
        udelezenci = json.load(dat)
    
    prisotni = []
    for udelezenec in udelezenci:
        if udelezenec['ime'] not in manjkajoci:
            prisotni.append(udelezenec)
    
    return prisotni
