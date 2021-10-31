% rebase('osnova.tpl')

<section class='section'>
	<div class='block'>
		<h1 class='title is-3'>Dogodki</h1>
	</div>

	<ul class=>
		% for dogodek in dogodki:
			<li>
				<b> {{dogodek['datum']}} </b> <br>

				<div class='content is-small'>
					<ul>
						% for udelezenec in dogodek['udelezenci']:
							<li>{{udelezenec['ime'] + ' ' + udelezenec['priimek']}}</li>
						% end
					</ul>
				</div>
					
			</li>
			<br>
		% end
	</ul>
</section>
