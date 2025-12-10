#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()

# Retrieve the form field values
order_no = form.getvalue('order_no')
cust_no = form.getvalue('cust_no')
date = form.getvalue('date')
sku = form.getlist('sku[]')  # This is a list
qty = form.getlist('qty[]')  # This is a list

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Adding Product</title>
    <style>
        body {
            background-color: #111111;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            color: #ffffff;
        }
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .message-container {
            width: 400px;
            text-align: center;
            background-color: #222222;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        }
        h2 {
            margin-bottom: 20px;
        }
        .success {
            color: #2ecc71;
        }
        .error {
            color: #e74c3c;
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
""")

# Establish connection
connection = psycopg2.connect(login.credentials)
cursor = connection.cursor()

try:
    # Start the transaction
    connection.autocommit = False
    #verifica se o Product tem suplier
    for i in range(len(sku)):
        query = "SELECT * FROM supplier WHERE sku = %s;"
        values = (sku[0],)
        cursor.execute(query, values)
        if cursor.rowcount == 0:
            print('<div class="center">')
            print('<div class="message-container">')
            print('<h2 class="error">Product {} does not have a supplier</h2>'.format(sku[i]))
            print("""<div class="button-link">
                <a href='createOrder.cgi'>Voltar</a>
                </div>
                """)
            exit()
    # Insert into orders Table
    query = "INSERT INTO orders (order_no, cust_no, date) VALUES (%s, %s, %s);"
    values = (order_no, cust_no, date)
    cursor.execute(query, values)

    # Insert into contains Table
    for i in range(len(sku)):
        query = "INSERT INTO contains (order_no, sku, qty) VALUES (%s, %s, %s);"
        values = (order_no, sku[i], qty[i])
        cursor.execute(query, values)

    # Commit the transaction
    connection.commit()

    print('<div class="center">')
    print('<div class="message-container">')
    print('<h2 class="success">Order Added Successfully</h2>')
    print("<p>Order number: {}</p>".format(order_no))
    print("<p>Customer number: {}</p>".format(cust_no))
    print("<p>Date: {}</p>".format(date))
    print("<h2>Products:</h2>")
    for i in range(len(sku)):
        print("<p>SKU: {} - Quantity: {}</p>".format(sku[i], qty[i]))
    
    
    print("""<div class="button-link">
        <a href='createOrder.cgi'>Back</a>
        </div>
        """)

except Exception as e:
    # Rollback the transaction in case of an error
    connection.rollback()
    print("An error occurred:", e)
    print("""<div class="button-link">
        <a href='createOrder.cgi'>Back</a>
        </div>
        """)

finally:
    # Reset autocommit to its default value
    connection.autocommit = True

    # Closing connection
    cursor.close()
    connection.close()

print("""
    </body>
    </html>
""")