#!/usr/bin/python3
import cgi
import psycopg2
import login

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Payment Success</title>
    <style>
        body {
            background-color: #111111;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            color: #ffffff;
        }
        .center {
            text-align: center;
            margin-top: 200px;
        }
        .message-box {
            display: inline-block;
            padding: 20px;
            border: 1px solid transparent;
            border-radius: 4px;
            background-color: #222222;
        }
        h2 {
            color: #ffffff;
            margin-bottom: 20px;
        }
        p {
            color: #ffffff;
            margin-bottom: 20px;
        }
        .back-link {
            display: block;
            text-align: center;
            margin-top: 20px;
        }
        .back-link a {
            color: #007bff;
            text-decoration: none;
        }
        .back-link a:hover {
            text-decoration: underline;
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

# Check if the order ID is provided in the URL parameters
form = cgi.FieldStorage()
order_id = form.getvalue('order_id')
client_id = form.getvalue('client_id')

if order_id:
    connection = None
    try:
        # Establish connection
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        # Retrieve quantity and price information
        sql_contains = "SELECT qty, sku FROM contains WHERE order_no = %s;"
        cursor.execute(sql_contains, (order_id,))
        contains_info = cursor.fetchall()

        # Calculate total amount
        total_amount = 0
        for row in contains_info:
            qty = row[0]
            sku = row[1]
            sql_product = "SELECT price FROM product WHERE sku = %s;"
            cursor.execute(sql_product, (sku,))
            product_price = cursor.fetchone()[0]
            total_amount += qty * product_price

        # Insert order_id and client_id into the pay table
        sql_pay = "INSERT INTO pay (order_no, cust_no) VALUES (%s, %s);"
        cursor.execute(sql_pay, (order_id, client_id))
        connection.commit()

        # Display success message with payment amount
        print('<div class="center">')
        print('<div class="message-box">')
        print('<h2>Payment Successful</h2>')
        print('<p>Payment Amount: {}</p>'.format(total_amount))
        print('</div>')
        print('</div>')

        # Closing connection
        cursor.close()
        
        # Display "Voltar" link as a button
        print('<div class="button-link">')
        print('<a href="choseOrder.cgi">Back</a>')
        print('</div>')

    except Exception as e:
        # Print errors on the webpage if they occur
        print('<div class="center">')
        print('<h1>An error occurred.</h1>')
        print('<p>{}</p>'.format(e))
        print('</div>')
        
        print('<div class="button-link">')
        print('<a href="choseOrder.cgi">Back</a>')
        print('</div>')

    finally:
        if connection is not None:
            connection.close()

print("""
    </body>
    </html>
""")
