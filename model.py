import json

class Udelezenec:
    def __init__(self, ime, priimek) -> None:
        self.ime = ime
        self.priimek = priimek


def v_seznam(udelezenec):
    """"Objekt 'udeleženec' zapiše v seznam v JSON datoteki."""
    with open('seznam.json', 'a') as dat:
        dat.write(json.dumps(udelezenec.__dict__))
