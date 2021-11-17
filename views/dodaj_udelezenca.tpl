% rebase('osnova.tpl')

<form class="box" action='/dodaj_udelezenca/' method='POST'>

  <div class="field">
    <label class="label">Ime</label>
    <div class="control">
      <input class="input" type="text" name="ime">
    </div>
  </div>

  <div class="field">
    <label class="label">Priimek</label>
    <div class="control">
      <input class="input" type="text" name="priimek">
    </div>
  </div>

  <button class="button is-primary" type="submit">Dodaj</button>

</form>

% if dodan:
<section class="hero is-success">
  <div class="hero-body">
    <p class="title">
      Jupi!
    </p>
    <p class="subtitle">
      Nov udeleženec je uspešno dodan. <br>
  </p>
  </div>
</section>

% end

% if ze_obstaja:
<section class="hero is-danger">
  <div class="hero-body">
    <p class="title">
      Napaka
    </p>
    <p class="subtitle">
      Ta udeleženec že obstaja. <br>
  </p>
  </div>
</section>

% end

% if napaka:
<section class="hero is-danger">
  <div class="hero-body">
    <p class="title">
      Napaka
    </p>
    <p class="subtitle">
      Vnesite ime in priimek. <br>
  </p>
  </div>
</section>

% end