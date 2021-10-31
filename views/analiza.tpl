% rebase('osnova.tpl')

<form class="box" action='/analiza/' method='POST'>

  <div class="field">
    <label class="label">Ime</label>
    <div class="control">
      <input class="input" type="text" name="ime">
    </div>
  </div>

  <button class="button is-primary" type="submit">Analiziraj</button>

</form>

% if indikator:
<section class="section">
  <p class="subtitle">
    {{ime}} je bil-a prisoten-a na {{st_prisotnosti}} od {{st_dogodkov}} dogodkov.
  </p>
</section>

% end