#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Orders</title>
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
        }
        h2 {
            text-align: center;
            color: #ffffff;
            margin-top: 30px;
            margin-bottom: 20px;
        }
        .orders-table {
            margin: 0 auto;
            border-collapse: collapse;
            width: 80%;
            max-width: 800px;
            background-color: #222222;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        }
        .orders-table th,
        .orders-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #333333;
            white-space: nowrap; /* Prevent line breaks within table cells */
        }
        tr:nth-child(even) {
            background-color: #111111;
        }
        p {
            text-align: center;
            margin-top: 20px;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .add-order-btn {
            text-align: center;
            margin-top: 30px;
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

        .add-order-button {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 4px;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }

        .add-order-button:hover {
            background-color: #0056b3;
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
    print('<h2>Orders</h2>')
    sqlOrder = 'SELECT * FROM orders'

    # Get and display product info
    cursor.execute(sqlOrder)
    orderInfo = cursor.fetchall()

    print('<table class="orders-table">')
    print('<tr><th>Order number<th>Customer number<th>Date</tr>')
    for row in orderInfo:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')

    # Add Order button
    print("""
    <div class="add-order-btn">
        <a class="add-order-button" href="addOrderForm.cgi">Add order</a>
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
print('</body>')
print('</html>')
