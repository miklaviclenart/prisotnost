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