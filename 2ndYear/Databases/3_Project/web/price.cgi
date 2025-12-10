#!/usr/bin/python3
import cgi

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Products and Suppliers</title>
    <style>
        body {
            background-color: #111111;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .container {
            background-color: #222222;
            padding: 30px;
            border-radius: 5px;
        }
        h3 {
            text-align: center;
            color: #ffffff;
            margin-top: 0;
        }
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 30px;
        }
        p {
            text-align: center;
            margin-bottom: 10px;
            color: #ffffff;
        }
        input[type="text"] {
            padding: 10px;
            width: 200px;
            border: none;
            border-radius: 5px;
            background-color: #ffffff;
            color: #222222;
        }
        input[type="submit"] {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: #ffffff;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .button-link {
            text-align: center;
            margin-top: 20px;
        }
        .button-link a {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 4px;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
        }
        .button-link a:hover {
            background-color: #0056b3;
        }
    </style>
    </head>
    <body>
    <div class="container">
""")

form = cgi.FieldStorage()
SKU = form.getvalue('SKU')

# The string has the {}, the variables inside format() will replace the {}
print('<h3>Change price for product {}</h3>'.format(SKU))
# The form will send the info needed for the SQL query
print('<form action="updatePrice.cgi" method="post">')
print('<p><input type="hidden" name="SKU" value="{}"/></p>'.format(SKU))
print('<p style="color: #ffffff;">New price: <input type="text" name="price" style="background-color: #ffffff; color: #222222;"/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')
print('<div class="button-link">')
print('<a href="changePriceDescription.cgi">Back</a>')
print('</div>')
print('</div>')
print('</body>')
print('</html>')
