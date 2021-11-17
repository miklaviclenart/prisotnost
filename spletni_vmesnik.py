import bottle
import model


@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovni_zaslon.tpl')


@bottle.get('/udelezenci/')
def prikazi_udelezence():
    udelezenci = model.preberi_seznam('udelezenci.json')

    if udelezenci != []:
        return bottle.template('prikazi_udelezence.tpl', udelezenci=udelezenci)
    else:
        bottle.redirect('/udelezenci_opozorilo/')


@bottle.get('/udelezenci_opozorilo/')
def udelezenci_opozorilo():
    return bottle.template('udelezenci_opozorilo.tpl')


@bottle.get('/dogodki/')
def prikazi_dogodke():
    dogodki = model.preberi_seznam('dogodki.json')

    if dogodki != []:
        return bottle.template('prikazi_dogodke.tpl', dogodki=dogodki)
    else:
        bottle.redirect('/dogodki_opozorilo/')


@bottle.get('/dogodki_opozorilo/')
def dogodki_opozorilo():
    return bottle.template('dogodki_opozorilo.tpl')


@bottle.get('/dodaj_udelezenca/')
def dodaj_udelezenca_get():
    return bottle.template('dodaj_udelezenca.tpl', ze_obstaja=False, napaka=False, dodan=False)


@bottle.post('/dodaj_udelezenca/')
def dodaj_udelezenca():
    ime = bottle.request.forms.getunicode('ime')
    priimek = bottle.request.forms.getunicode('priimek')
    udelezenci = model.preberi_seznam('udelezenci.json')
    ze_obstaja = False

    for udelezenec in udelezenci:
        if ime == udelezenec['ime'] and priimek == udelezenec['priimek']:
            ze_obstaja = True

    if ze_obstaja:
        return bottle.template('dodaj_udelezenca.tpl', ze_obstaja=True, napaka=False, dodan=False)
    elif ime and priimek:       
        udelezenec = model.Udelezenec(ime, priimek)
        udelezenec.v_seznam()
        return bottle.template('dodaj_udelezenca.tpl', ze_obstaja=False, napaka=False, dodan=True)
    else:
        return bottle.template('dodaj_udelezenca.tpl', ze_obstaja=False, napaka=True, dodan=False)


@bottle.get('/dodaj_dogodek/')
def dodaj_dogodek_get():
    udelezenci = model.preberi_seznam('udelezenci.json')
    if udelezenci != []:
        return bottle.template('dodaj_dogodek.tpl', udelezenci=udelezenci)
    else:
        bottle.redirect('/udelezenci_opozorilo/')


@bottle.post('/dodaj_dogodek/')
def dodaj_dogodek():
    datum = bottle.request.forms.getunicode('datum')
    manjkajoci = bottle.request.forms.getall('udelezenec')
    print(manjkajoci)
    prisotni = model.prisotni(manjkajoci)
    if datum:
        dogodek = model.Dogodek(datum, prisotni)
        dogodek.v_seznam()
        bottle.redirect('/')
    else:
        return 'Vnesite datum!'


@bottle.get('/analiza/')
def analiza():
    return bottle.template('analiza.tpl', indikator=False)


@bottle.post('/analiza/')
def analiziraj():
    try:
        ime = bottle.request.forms.getunicode('ime')
        st_prisotnosti = model.st_prisotnosti(ime)
        st_dogodkov = model.stevilo_v_seznamu('dogodki.json')

        return bottle.template('analiza.tpl', indikator=True, ime=ime, st_prisotnosti=st_prisotnosti, st_dogodkov=st_dogodkov)
    except FileNotFoundError:
        bottle.redirect('/dogodki_opozorilo/')


bottle.run(debug=True, reloader=True)
