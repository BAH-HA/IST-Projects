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
            font-family: Arial, sans-serif;
            color: #ffffff;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
        }
        h2 {
            color: #ffffff;
            margin-bottom: 20px;
        }
        p {
            color: #ffffff;
            margin-bottom: 20px;
        }
        table {
            width: 80%;
            margin-top: 20px;
            margin-bottom: 40px;
            border-collapse: collapse;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 0 8px rgba(0, 0, 0, 0.3);
        }
        table tr:first-child {
            background-color: #222222;
            color: #ffffff;
            font-weight: bold;
        }
        table tr:nth-child(even) {
            background-color: #333333;
        }
        table td {
            padding: 10px;
            text-align: center;
            border: none;
        }
        .button-container {
            margin-top: 20px;
        }
        .button-container button {
            padding: 8px 16px;
            margin: 0 10px;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            color: #ffffff;
            font-size: 14px;
            text-decoration: none;
            cursor: pointer;
        }
        .button-container button:hover {
            background-color: #0056b3;
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

    # Product
    print('<h2>Product</h2>')
    sqlProduct = 'SELECT * FROM product'

    # Get and display product info
    cursor.execute(sqlProduct)
    productInfo = cursor.fetchall()

    print('<table>')
    print('<tr><th>SKU</th><th>Name</th><th>Description</th><th>Price</th><th>EAN</th></tr>')
    for i, row in enumerate(productInfo):
        if i % 2 == 0:
            print('<tr class="even">')
        else:
            print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')

    # Add or Remove Product buttons
    print("""
    <div class="button-container">
        <button onclick="window.location.href='addProductForm.cgi'">Add Product</button>
        <button onclick="window.location.href='removeProductForm.cgi'">Remove Product</button>
    </div>
    """)

    # Supplier
    print('<h2>Supplier</h2>')
    sqlSupplier = 'SELECT * FROM supplier'

    # Get and display supplier info
    cursor.execute(sqlSupplier)
    supplierInfo = cursor.fetchall()

    print('<table>')
    print('<tr><th>TIN</th><th>Name</th><th>Address</th><th>SKU</th><th>Date</th></tr>')
    for i, row in enumerate(supplierInfo):
        if i % 2 == 0:
            print('<tr class="even">')
        else:
            print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')
    
    # Add or Remove Supplier buttons
    print("""
    <div class="button-container">
        <button onclick="window.location.href='addSupplierForm.cgi'">Add Supplier</button>
        <button onclick="window.location.href='removeSupplierForm.cgi'">Remove Supplier</button>
    </div>
    """)

    # Closing connection
    cursor.close()

except Exception as e:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))

finally:
    if connection is not None:
        connection.close()

print("""
    </div>
    </body>
    </html>
""")
