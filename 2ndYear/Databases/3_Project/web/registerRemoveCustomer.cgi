#!/usr/bin/python3
import psycopg2
import login
import cgi

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Customers</title>
    <style>
        body {
            background-color: #0f0f0f;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            color: #ffffff;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h2, p {
            text-align: center;
            color: #ffffff;
            margin-top: 30px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }
        table th {
            background-color: #222222;
            color: #ffffff;
            text-align: left;
            padding: 10px;
            border-bottom: 1px solid #333333;
        }
        table td {
            padding: 10px;
            border-bottom: 1px solid #333333;
        }
        table tr:nth-child(even) td {
            background-color: #1a1a1a;
        }
        a {
            display: inline-block;
            padding: 10px 20px;
            margin-top: 20px;
            border-radius: 4px;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            text-align: center;
            transition: background-color 0.3s;
        }
        a:hover {
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

        .navigation-buttons {
            text-align: center;
        }
    
        .navigation-buttons a {
            display: inline-block;
            padding: 6px 12px;
            margin-top: 20px;
            border-radius: 4px;
            background-color: #0065bb;
            color: #ffffff;
            text-decoration: none;
            text-align: center;
            transition: background-color 0.1s;
            font-size: 12px;
            margin: 10px 5px;
        }
    
        .navigation-buttons a:hover {
            background-color: #004c99;
        }
    </style>
    </head>
    <body>
    <div class="container">
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

    # Retrieve the current page from the query parameters
    params = cgi.FieldStorage()
    if 'page' in params:
        current_page = int(params['page'].value)
    else:
        current_page = 1

    # Number of rows per page
    rows_per_page = 8

    # Calculate the offset based on the current page and rows per page
    offset = (current_page - 1) * rows_per_page

    # Customers
    print('<h2>Customer</h2>')
    sql = 'SELECT * FROM customer LIMIT {} OFFSET {}'.format(rows_per_page, offset)

    # Get and display customer info
    cursor.execute(sql)
    customerInfo = cursor.fetchall()

    print('<table>')
    print('<tr><th>Number</th><th>Name</th><th>Email</th><th>Phone</th><th>Address</th></tr>')
    for row in customerInfo:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')

    # Add navigation buttons
    print('<div class="navigation-buttons">')
    if current_page > 1:
        print('<a href="?page={}">Previous</a>'.format(current_page - 1))
    if len(customerInfo) == rows_per_page:
        print('<a href="?page={}">Next</a>'.format(current_page + 1))
    print('</div>')
    
    # Add or Remove Client links
    print("""
    <div style="text-align: center">
        <a href="addCustomerForm.cgi">Add customer</a>
        <a href="removeCustomerForm.cgi">Remove customer</a>
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
print('</div>')
print('</body>')
print('</html>')
