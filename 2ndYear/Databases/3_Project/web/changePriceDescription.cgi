#!/usr/bin/python3
import psycopg2
import login

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
        }
        h2 {
            text-align: center;
            color: #ffffff;
            margin-top: 30px;
        }
        table {
            margin: 30px auto;
            border-collapse: collapse;
            border-radius: 5px;
            overflow: hidden;
            width: 80%;
            max-width: 800px;
            background-color: #222222;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #333333;
            color: #ffffff;
        }
        th {
            background-color: #333333;
        }
        td a {
            color: #007bff;
            text-decoration: none;
        }
        td a:hover {
            text-decoration: underline;
        }
        .return-button {
            position: absolute;
            top: 10px;
            left: 10px;
            padding: 8px 16px;
            margin: 0 10px;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            color: #ffffff;
            font-size: 14px;
            text-decoration: none;
            cursor: pointer;
            display: inline-block;
            transition: transform 0.3s ease;
        }

        .return-button::before {
            content: '';
            display: inline-block;
            width: 8px;
            height: 8px;
            border-top: 2px solid #ffffff;
            border-left: 2px solid #ffffff;
            transform: rotate(-45deg);
            margin-right: 8px;
        }

        .return-button:hover {
            transform: translateX(-4px);
        }
    </style>
    </head>
    <body>
""")

print("""
    <div class="container">
    <button class="return-button" onclick="window.location.href='mainMenu.cgi'">Return to Menu</button>
""")

connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    
    
    print('<h2>Products</h2>')
    sqlProduct = 'SELECT * FROM product ORDER BY SKU'
    
    cursor.execute(sqlProduct)
    result = cursor.fetchall()
    
    # Displaying results
    print('<table>')
    print('<tr><th>SKU</th><th>Name</th><th>Description</th><th>Price</th><th>EAN</th><th></th><th></th></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            # The string has the {}, the variables inside format() will replace the {}
            print('<td>{}</td>'.format(value))
        print('<td><a href="price.cgi?SKU={}">Change Price</a></td>'.format(row[0]))
        print('<td><a href="description.cgi?SKU={}">Change Description</a></td>'.format(row[0]))

        print('</tr>')
    print('</table>')
    # Closing connection
    cursor.close()
except Exception as e:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close()
print('</body>')
print('</html>')

(addCostumerForm; addOrderForm; addProductForm; addSupplierForm; removeCostumerForm; removeProductForm; removeSupplierForm)