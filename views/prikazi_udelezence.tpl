% rebase('osnova.tpl')

<h1 class='title is-3'>Udeleženci</h1>
<table class='table'>
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
