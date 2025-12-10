#!/usr/bin/python3
import cgi
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
        .client-form {
            text-align: center;
            margin-top: 30px;
        }
        .client-form input[type="text"] {
            width: 200px;
            padding: 6px 10px;
            border-radius: 4px;
            border: 1px solid #dddddd;
        }
        .client-form input[type="submit"] {
            margin-top: 10px;
            padding: 8px 20px;
            font-size: 14px;
            border-radius: 4px;
            border: none;
            background-color: #007bff;
            color: #ffffff;
            cursor: pointer;
        }
        .client-form input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .pay-btn {
            text-align: center;
            margin-top: 10px;
        }
        .pay-btn a {
            padding: 6px 12px;
            font-size: 14px;
            border-radius: 4px;
            border: none;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            cursor: pointer;
        }
        .pay-btn a:hover {
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
""")


# Check if the client ID is provided in the URL parameters
form = cgi.FieldStorage()
client_id = form.getvalue('client_id')

if client_id:
    connection = None
    try:
        # Establish connection
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        # Retrieve orders for the client ID not present in the "pay" table
        sql_order = """
            SELECT o.order_no, o.cust_no, o.date
            FROM orders o
            LEFT JOIN pay p ON o.order_no = p.order_no
            WHERE o.cust_no = %s AND p.order_no IS NULL;
        """
        cursor.execute(sql_order, (client_id,))
        order_info = cursor.fetchall()

        if order_info:
            # Display orders table
            print('<div class="center">')
            print('<h2>Orders for Client ID: {}</h2>'.format(client_id))
            print('<table class="orders-table">')
            print('<tr><th>Order number<th>Customer number<th>Date<th>Action</tr>')
            for row in order_info:
                order_number = row[0]
                print('<tr>')
                for value in row:
                    print('<td>{}</td>'.format(value))
                print('<td class="pay-btn"><a href="payOrder.cgi?order_id={}&client_id={}">Pay</a></td>'.format(order_number, client_id))
                print('</tr>')
            print('</table>')
            print('</div>')
        else:
            # No orders found for the client ID or all orders have been paid
            print('<div class="center">')
            print('<p>No unpaid orders found for Client ID: {}</p>'.format(client_id))
            print('</div>')
            
        print('<div class="button-link">')
        print('<a href="choseClient.cgi">Back</a>')
        print('</div>')

        # Closing connection
        cursor.close()

    except Exception as e:
        # Print errors on the webpage if they occur
        print('<div class="center">')
        print('<h1>An error occurred.</h1>')
        print('<p>{}</p>'.format(e))
        print('</div>')
        
        print('<div class="button-link">')
        print('<a href="choseClient.cgi">Back</a>')
        print('</div>')

    finally:
        if connection is not None:
            connection.close()

print("""
    </body>
    </html>
""")
