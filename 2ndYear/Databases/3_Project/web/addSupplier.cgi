#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()

# Retrieve the form field values
tin = form.getvalue('tin')
name = form.getvalue('name')
address = form.getvalue('address')
sku = form.getvalue('sku')
date = form.getvalue('date')

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Adding Supplier</title>
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
        .box {
            width: 400px;
            padding: 20px;
            background-color: #222222;
            border-radius: 8px;
        }
        h2 {
            color: #ffffff;
            margin-bottom: 20px;
        }
        p {
            color: #ffffff;
            margin-bottom: 10px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            color: #ffffff;
            font-size: 14px;
            text-decoration: none;
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
        <div class="box">
""")

connection = None
try:
    # Establishing connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Insert into Supplier Table
    query = "INSERT INTO supplier (tin, name, address, sku, date) VALUES (%s, %s, %s, %s, %s);"
    values = (tin, name, address, sku, date)
    cursor.execute(query, values)
    connection.commit()

    print("<h2>Supplier Added Successfully</h2>")
    print("<p>TIN: {}</p>".format(tin))
    print("<p>Name: {}</p>".format(name))
    print("<p>Address: {}</p>".format(address))
    print("<p>SKU: {}</p>".format(sku))
    print("<p>Date: {}</p>".format(date))

    print("""
    <form action="registerProductSupplier.cgi" method="post">
        <input type="submit" value="Back">
    </form>
    """)


except (Exception, psycopg2.Error) as error:
    print("<h2>Error Adding Supplier</h2>")
    print("<p>{}</p>".format(str(error)))
    print("""
    <form action="registerProductSupplier.cgi" method="post">
        <input type="submit" value="Voltar">
    </form>
    """)
    
    print("""<div class="button-link">
        <a href='registerProductSupplier.cgi'>Back</a>
        </div>
        """)

finally:
    # Closing database connection
    if connection:
        connection.close()

print("""
        </div>
    </div>
    </body>
    </html>
""")
