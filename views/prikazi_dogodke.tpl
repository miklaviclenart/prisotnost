% rebase('osnova.tpl')
<h1>Udeleženci</h1>
<ul>
    % for dogodek in dogodki:
    <li>
        <b> {{dogodek['datum']}} </b> <br>
        <ul>
            % for udelezenec in dogodek['udelezenci']:
            <li>{{udelezenec['ime'] + ' ' + udelezenec['priimek']}}, </li>
            % end
        </ul>
    </li>
    <br>
    % end
</ul>
