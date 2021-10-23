import json
import os.path

class Udelezenec:
    def __init__(self, ime, priimek) -> None:
        self.ime = ime
        self.priimek = priimek


def v_seznam(udelezenec):
    """"Objekt 'udeleženec' zapiše v seznam v JSON datoteki."""

# Ali datoteka s seznamom že obstaja? 

    if os.path.isfile('seznam.json'):
        with open('seznam.json', 'r') as dat:
            seznam = json.load(dat)

        seznam.append(udelezenec.__dict__)

        with open('seznam.json', 'w') as dat:
            json.dump(seznam, dat, indent=4)

# Če ne obstaja, odpri novo in 'udelezenca' dodaj v prazen seznam.

    else:
        with open('seznam.json', 'a') as dat:
            seznam = []
            seznam.append(udelezenec.__dict__)
            json.dump(seznam, dat, indent=4)
