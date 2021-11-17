import json


def preberi_seznam(ime_datoteke):
    """Iz .json datoteke poskusi prebrati seznam. Če datoteka ne obstaja, vrne prazen seznam."""
    try:
        with open(ime_datoteke, 'r', encoding='utf-8') as dat:
            return json.load(dat)
    except FileNotFoundError:
        return []


class Udelezenec:
    def __init__(self, ime, priimek) -> None:
        self.ime = ime
        self.priimek = priimek
    
    def v_seznam(self):
        udelezenci = preberi_seznam('udelezenci.json')
        
        udelezenci.append(self.__dict__)

        with open('udelezenci.json', 'w', encoding='utf-8') as dat:
            json.dump(udelezenci, dat, ensure_ascii=False, indent=4)
    
    def prisoten(self, datum):
        return self.__dict__ in preberi_seznam('dogodki.json')[datum]

    def stevilo_prisotnosti(self):
        prisotnost = 0

        for dogodek in preberi_seznam('dogodki.json'):
            if self.__dict__ in dogodek['udelezenci']:
                prisotnost += 1

        return prisotnost



class Dogodek:
    def __init__(self, datum: str, udelezenci: list) -> None:
        self.datum = datum
        self.udelezenci = udelezenci

    def v_seznam(self):
        dogodki = preberi_seznam('dogodki.json')
        
        dogodki.append(self)

        with open('dogodki.json', 'w', encoding='utf-8') as dat:
            json.dump(dogodki, dat, ensure_ascii=False, indent=4)


# def v_seznam(objekt, ime_datoteke) -> None:
#     """"Objekt 'udeleženec' zapiše v seznam v JSON datoteki."""

# # Ali datoteka s seznamom že obstaja?

#     try:
#         with open(ime_datoteke, 'r', encoding='utf-8') as dat:
#             seznam = json.load(dat)

#         seznam.append(objekt.__dict__)

#         with open(ime_datoteke, 'w', encoding='utf-8') as dat:
#             json.dump(seznam, dat, ensure_ascii=False, indent=4)

# # Če ne obstaja, odpri novo in objekt dodaj v prazen seznam.

#     except FileNotFoundError:
#         with open(ime_datoteke, 'a', encoding='utf-8') as dat:
#             seznam = []
#             seznam.append(objekt.__dict__)
#             json.dump(seznam, dat, ensure_ascii=False, indent=4)


def prisotni(manjkajoci) -> list:
    """Vrne seznam vseh prosotnih, t.j. vseh v 'seznam.json' datoteki, ki jih ne navedemo v seznamu 'manjkajoci'."""
    udelezenci = preberi_seznam('udelezenci.json')

    prisotni = []
    for udelezenec in udelezenci:
        if udelezenec not in manjkajoci:
            prisotni.append(udelezenec)

    return prisotni


# def prisotnost(udelezenec, datum) -> bool:
#     """Vrne 'True', če je bil udeleženec na dogodku prisoten. Če dogodek ne obstaja, program krešne."""
#     with open('dogodki.json', 'r', encoding='utf-8') as dat:
#         dogodki = json.load(dat)

#     for dogodek in dogodki:
#         if dogodek['datum'] == datum:
#             pravi = dogodek

#     seznam_prisotnih = pravi['udelezenci']

#     for prisoten in seznam_prisotnih:
#         return udelezenec == prisoten['ime']


# def st_prisotnosti(udelezenec):
#     """Vrne število dogodkov, na katerih je bil udeleženec prisoten."""
#     with open('dogodki.json', 'r', encoding='utf-8') as dat:
#         dogodki = json.load(dat)

#     stevilo = 0
#     for dogodek in dogodki:
#         for udelezenci in dogodek['udelezenci']:
#             if udelezenec == udelezenci['ime']:
#                 stevilo += 1
#                 break

#     return stevilo


def stevilo_v_seznamu(ime_datoteke):
    with open(ime_datoteke, 'r', encoding='utf-8') as dat:
        seznam = json.load(dat)

    return len(seznam)
