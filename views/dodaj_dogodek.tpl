% rebase('osnova.tpl')

<form class="box" action='/dodaj_dogodek/' method='POST'>

  <div class="field">
    <label class="label">Datum</label>
    <div class="control">
      <input class="input" type="text" name="datum" placeholder="dd.mm.llll">
    </div>
  </div>

  <p class="label">Manjkajoči:</p>
  % for udelezenec in udelezenci:
  <input type="checkbox" value="udelezenec" name="manjkajoci">
  {{udelezenec['ime']}} {{udelezenec['priimek']}} <br>
  % end

  <button class="button is-primary" type="submit">Dodaj</button>

</form>