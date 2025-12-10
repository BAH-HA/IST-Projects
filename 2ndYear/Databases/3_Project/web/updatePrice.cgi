#!/usr/bin/python3
import psycopg2
import cgi

import login

form = cgi.FieldStorage()

# Retrieve the form field values
SKU = form.getvalue('SKU')
price = form.getvalue('price')

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Products and Suppliers</title>
    <style>
        body {
            background-color: #0E1116;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #E4E6EB;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
        }
        h3 {
            text-align: center;
            color: #E4E6EB;
            margin-top: 15px;
        }
        p {
            text-align: center;
            margin-bottom: 10px;
            color: #E4E6EB;
        }
        .success-message {
            margin-top: 30px;
            padding: 10px;
            border-radius: 5px;
            background-color: #222222;
            color: #E4E6EB;
            display: inline-block;
            text-align: center;
        }
        .box {
            padding: 20px;
            border-radius: 5px;
            background-color: #222222;
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

connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Making query
    sql = 'UPDATE product SET price = %s WHERE SKU = %s;'
    data = (price, SKU)

    # Feed the data to the SQL query as follows to avoid SQL injection
    cursor.execute(sql, data)

    # Commit the update (without this step the database will not change)
    connection.commit()

    # Closing connection
    cursor.close()

    # Display success message in a box
    print('<div class="box">')
    print('<div class="success-message">')
    print('<h3>Price updated successfully for product {}</h3>'.format(SKU))
    print('<p>Price: {}</p>'.format(price))
    print('</div>')
    print('</div>')
    
    # Display "Voltar" link as a button
    print('<div class="button-link">')
    print('<a href="changePriceDescription.cgi">Back</a>')
    print('</div>')


except Exception as e:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    
    # Display "Voltar" link as a button
    print('<div class="button-link">')
    print('<a href="changePriceDescription.cgi">Back</a>')
    print('</div>')


finally:
    if connection is not None:
        connection.close()

print("""
    </div>
    </body>
    </html>
""")
