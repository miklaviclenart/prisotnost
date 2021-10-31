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
  <progress class="progress is-primary" value="{{100 * (st_prisotnosti / st_dogodkov)}}" max="100">
    {{100 * (st_prisotnosti / st_dogodkov)}}%
  </progress>
</section>

% end