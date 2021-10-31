% rebase('osnova.tpl')

<section class="section">
	<div class='block'>
		<h1 class='title is-3'>Udeleženci</h1>
	</div>

  <table class='table is-fullwidth'>
      <thead>
        <th>Ime</th>
        <th>Priimek</th>
      </thead>
      % for udelezenec in udelezenci:
      <tr>
          <td>{{udelezenec['ime']}}</td>
          <td>{{udelezenec['priimek']}}</td>
      </tr>
      % end
  </table>
</section>

