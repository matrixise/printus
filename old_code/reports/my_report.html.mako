<!DOCTYPE html>
<html>
    <body>
        <h1>${report['uuid']}</h1>
        <h1>${report['data']['name']}</h1>

        <h2>${report['data']['date']}</h2>
        <h3>${report['data']['time']}</h3> 

        <table>
            <tr>
                <th>Number</th>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>login</th>
            </tr>

        % for i in range(0, 1000):
            % for row in report['data']['lines']:
            <tr>
                <td>${i}</td>
                <td>${row['firstname']}</td>
                <td>${row['lastname']}</td>
                <td>${row['login']}</td>
            </tr>
            % endfor
        % endfor
        </table>
    </body>
</html>
