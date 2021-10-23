import model


###########################################################
# Pomožne funkcije za prikaz
###########################################################


def krepko(niz):
    return f"\033[1m{niz}\033[0m"


def dobro(niz):
    return f"\033[1;94m{niz}\033[0m"


def slabo(niz):
    return f"\033[1;91m{niz}\033[0m"


###########################################################
# Pomožne funkcije za vnos
###########################################################


def vnesi_stevilo(pozdrav):
    """S standardnega vhoda prebere naravno število."""
    while True:
        try:
            stevilo = input(pozdrav)
            return int(stevilo)
        except ValueError:
            print(slabo("Prosim, da vnesete število!"))


def izberi(seznam):
    """
    Uporabniku omogoči interaktivno izbiro elementa iz seznama.
    Funkcija sprejme seznam parov (oznaka, element), prikaže seznam
    oznak ter vrne element, ki ustreza vpisani oznaki.
    >>> izberi([('deset', 10), ('trideset', 30)])
    1) deset
    2) trideset
    > 2
    30
    """
    if len(seznam) == 1:
        opis, element = seznam[0]
        print(f"Na voljo je samo možnost {opis}, zato sem jo izbral.")
        return element
    for indeks, (oznaka, _) in enumerate(seznam, 1):
        print(f"{indeks}) {oznaka}")
    while True:
        izbira = vnesi_stevilo("> ")
        if 1 <= izbira <= len(seznam):
            _, element = seznam[izbira - 1]
            return element
        else:
            print(slabo(f"Izberi število med 1 in {len(seznam)}"))


###########################################################
# Tekstovni vmesnik
###########################################################


def tekstovni_vmesnik():
    uvodni_pozdrav()
    while True:
        try:
            print(80 * "=")
            print()
            print(krepko("Kaj bi hoteli narediti?"))
            moznosti = [
                ("dodaj novega udeleženca", dodaj_udelezenca),
                ("dodaj nov dogodek", dodaj_dogodek)
            ]
            izbira = izberi(moznosti)
            print(80 * "=")
            izbira()
            print()

        except KeyboardInterrupt:
            print()
            print("Nasvidanje")
            return


def uvodni_pozdrav():
    print(krepko("Pozdravljeni!"))
    print("Za izhod pritisnite Ctrl-C.")


def dodaj_udelezenca():
    ime = input("Ime udeleženca: ")
    priimek = input("Priimek udeleženca: ")

    udelezenec = model.Udelezenec(ime, priimek)
    model.v_seznam(udelezenec, 'udelezenci.json')

    print()
    print(krepko("Udeleženec uspešno dodan!"))
    print()
    print("Ali bi želeli dodati novega udeleženca?")
    print()
    izbira = input("da/ne... ")
    if izbira == "da":
        dodaj_udelezenca()


def dodaj_dogodek():
    datum = input("Datum dogodka: ")
    print()

    manjkajoci = []
    while True:
        manjkajoc = input(
            "Kdo manjka? Če ne manjka nihče pritisnite Enter... ")
        if manjkajoc != "":
            manjkajoci.append(manjkajoc)
            print()
            print(manjkajoci)
            print()
        else:
            prisotni = model.prisotni(manjkajoci)
            dogodek = model.Dogodek(datum, prisotni)
            model.v_seznam(dogodek, 'dogodki.json')
            print(krepko("Dogodek uspešno dodan!"))
            break
    print()
    print("Ali bi želeli dodati nov dogodek?")
    izbira = input("da/ne... ")
    if izbira == "da":
        dodaj_dogodek()


tekstovni_vmesnik()
