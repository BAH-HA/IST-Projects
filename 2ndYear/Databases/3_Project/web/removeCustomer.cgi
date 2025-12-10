#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()

# Retrieve the form field values
cust_no = form.getvalue('cust_no')

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Deleting Customer</title>
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
        .message-box {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            border-radius: 8px;
            background-color: #222222;
            color: #ffffff;
        }
        .button-container {
            text-align: center;
            margin-top: 20px;
        }
        .button-container input[type="submit"] {
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 4px;
            border: none;
            background-color: #007bff;
            color: #ffffff;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .button-container input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .back-link {
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
        
        
    </style>
    </head>
    <body>
    <div class="container">
""")

connection = None
try:
    # Establishing connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Delete from customer Table
    
    
    
    
    query = "SELECT order_no FROM orders WHERE cust_no = %s;"
    values = (cust_no,)
    cursor.execute(query, values)
    order_nos = cursor.fetchall()
    
    for order_no in order_nos:
            
    
        query = "DELETE FROM process WHERE order_no = %s RETURNING order_no;"
        values = (order_no,)
        cursor.execute(query, values)
        deleted_process = cursor.fetchone()
        
        
        query = "DELETE FROM contains WHERE order_no = %s RETURNING order_no;"
        values = (order_no,)
        cursor.execute(query, values)
        deleted_contains = cursor.fetchone()
        
    
    

    
    query = "DELETE FROM pay WHERE cust_no = %s RETURNING cust_no;"
    values = (cust_no,)
    cursor.execute(query, values)
    deleted_pay = cursor.fetchone()
    
    
    query = "DELETE FROM orders WHERE cust_no = %s RETURNING cust_no;"
    values = (cust_no,)
    cursor.execute(query, values)
    deleted_order = cursor.fetchone()
    
    
    
    
    
    query = "DELETE FROM customer WHERE cust_no = %s RETURNING cust_no;"
    values = (cust_no,)
    cursor.execute(query, values)
    deleted_cust_no = cursor.fetchone()

    if deleted_cust_no:
        connection.commit()
        print('<div class="message-box">')
        print("<h2>Customer Deleted Successfully</h2>")
        print("<p>Customer Number: {}</p>".format(deleted_cust_no[0]))
        print('</div>')
        print("""<div class="button-container">
            <input type="submit" value="Voltar" onclick="window.location.href='registerRemoveCustomer.cgi'">
            </div>
            """)
    else:
        print('<div class="message-box">')
        print("<h2>No Customer Found with Customer Number: {}</h2>".format(cust_no))
        print('</div>')
        print("""<div class="button-container">
            <input type="submit" value="Voltar" onclick="window.location.href='registerRemoveCustomer.cgi'">
            </div>
            """)

except (Exception, psycopg2.Error) as error:
    print('<div class="message-box">')
    print("<h2>Error Deleting Customer</h2>")
    print("<p>{}</p>".format(str(error)))
    print('</div>')
    print("""<div class="button-container">
            <input type="submit" value="Voltar" onclick="window.location.href='registerRemoveCustomer.cgi'">
            </div>
            """)

finally:
    # Closing database connection
    if connection:
        connection.close()

print("""
    </div>
    </body>
    </html>
""")
