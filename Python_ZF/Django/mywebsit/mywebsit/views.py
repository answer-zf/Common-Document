from django.http import HttpResponse

def social(request):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    
    <body>
        <form action="/social" method="POST">
            <label for="">
                pl. input money:
                <input type="text" name="money">
            </label>
            <select name="address">
                <option value="0">country</option>
                <option value="1">city</option>
            </select>
            <input type="submit">
        </form>
    
        <hr>
    
        <table border="1">
            <tr>
                <th>项目</th>
                <th>个人缴纳</th>
                <th>单位缴纳</th>
            </tr>
            <tr>
                <td>养老</td>
                <td>%s元</td>
                <td>%s元</td>
            </tr>
            <tr>
                <td>事业</td>
                <td>%s元</td>
                <td>%s元</td>
            </tr>
            <tr>
                <td>工伤</td>
                <td>%s元</td>
                <td>%s元</td>
            </tr>
            <tr>
                <td>生育</td>
                <td>%s元</td>
                <td>%s元</td>
            </tr>
            <tr>
                <td>医疗</td>
                <td>%s元</td>
                <td>%s元</td>
            </tr>
            <tr>
                <td>公积金</td>
                <td>%s元</td>
                <td>%s元</td>
            </tr>
            <tr>
                <td>个人总和</td>
                <td>%s元</td>
            </tr>
            <tr>
                <td>单位总和</td>
                <td>%s元</td>
    
            </tr>
            <tr>
                <td>纳税</td>
                <td>%s元</td>
            </tr>
        </table>
    </body>
    
    </html>

    '''