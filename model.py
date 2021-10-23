import json

class Udelezenec:
    def __init__(self, ime, priimek) -> None:
        self.ime = ime
        self.priimek = priimek


def v_seznam(udelezenec):
    """"Objekt 'udeleženec' zapiše v seznam v JSON datoteki."""
    with open('seznam.json', 'r') as dat:
        seznam = json.load(dat)
    
    seznam.append(json.dumps(udelezenec.__dict__))

    with open('seznam.json', 'w') as dat:
        json.dump(seznam, dat, indent=4)
