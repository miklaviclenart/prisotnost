import bottle
import json
import model


@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovni_zaslon.tpl')


@bottle.get('/udelezenci/')
def prikazi_udelezence():
    with open('udelezenci.json', 'r', encoding='utf-8') as dat:
        udelezenci = json.load(dat)
    return bottle.template('prikazi_udelezence.tpl', udelezenci=udelezenci)


@bottle.get('/dogodki/')
def prikazi_dogodke():
    with open('dogodki.json', 'r', encoding='utf-8') as dat:
        dogodki = json.load(dat)
    return bottle.template('prikazi_dogodke.tpl', dogodki=dogodki)


@bottle.get('/dodaj_udelezenca/')
def dodaj_udelezenca_get():
    return bottle.template('dodaj_udelezenca.tpl')


@bottle.post('/dodaj_udelezenca/')
def dodaj_udelezenca():
    ime = bottle.request.forms.getunicode('ime')
    priimek = bottle.request.forms.getunicode('priimek')
    if ime and priimek:
        udelezenec = model.Udelezenec(ime, priimek)
        model.v_seznam(udelezenec, 'udelezenci.json')
        bottle.redirect('/')
    else:
        return 'Vnesite ime in priimek!'


@bottle.get('/dodaj_dogodek/')
def dodaj_dogodek_get():
    with open('udelezenci.json', 'r', encoding='utf-8') as dat:
        udelezenci = json.load(dat)
    return bottle.template('dodaj_dogodek.tpl', udelezenci=udelezenci)


@bottle.post('/dodaj_dogodek/')
def dodaj_udelezenca():
    datum = bottle.request.forms.getunicode('datum')
    manjkajoci = bottle.request.forms.getall('manjkajoci')
    print(manjkajoci)
    prisotni = model.prisotni(manjkajoci)
    if datum:
        dogodek = model.Dogodek(datum, prisotni)
        model.v_seznam(dogodek, 'dogodki.json')
        bottle.redirect('/')
    else:
        return 'Vnesite datum!'


@bottle.get('/analiza/')
def analiza_get():
    return bottle.template('analiza.tpl', indikator=False)


@bottle.post('/analiza/')
def analiziraj():
    ime = bottle.request.forms.getunicode('ime')
    st_prisotnosti = model.st_prisotnosti(ime)
    st_dogodkov = model.stevilo_v_seznamu('dogodki.json')

    return bottle.template('analiza.tpl', indikator=True, ime=ime, st_prisotnosti=st_prisotnosti, st_dogodkov=st_dogodkov)


bottle.run(debug=True, reloader=True)
