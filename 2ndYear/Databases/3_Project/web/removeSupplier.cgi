#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()

# Retrieve the form field values
tin = form.getvalue('tin')

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Removing Supplier</title>
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
        .container {
            width: 400px;
            text-align: center;
            padding: 20px;
            background-color: #222222;
            border-radius: 8px;
        }
        .container h2 {
            color: #ffffff;
            margin-bottom: 20px;
        }
        .container p {
            text-align: center;
        }
        .container input[type="submit"] {
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            color: #ffffff;
            font-size: 14px;
            text-decoration: none;
            cursor: pointer;
        }
        .container input[type="submit"]:hover {
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
    <div class="center">
        <div class="container">
""")

connection = None
try:
    # Establishing connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Start the transaction
    connection.autocommit = False

    # Check if Supplier exists

    query = "DELETE FROM delivery WHERE TIN = %s RETURNING TIN;"
    values = (tin,)
    cursor.execute(query, values)
    deleted_TIN = cursor.fetchall()

    #Deletes orders related to the supplier
    query = "SELECT sku FROM supplier WHERE TIN = %s;"
    values = (tin,)
    cursor.execute(query, values)
    selected_sku = cursor.fetchall()
    if selected_sku:
        for sku in selected_sku:
            query = "DELETE FROM contains WHERE sku = %s RETURNING order_no;"
            cursor.execute(query, (sku[0],))
            order_no = cursor.fetchall()
            if order_no:
                for order in order_no:
                    query = "SELECT order_no FROM pay WHERE order_no = %s ;"
                    values = (order[0],)
                    cursor.execute(query, values)
                    order_no2 = cursor.fetchall()
                    if not order_no2:
                        query = "DELETE FROM process WHERE order_no = %s RETURNING order_no;"
                        values = (order[0],)
                        cursor.execute(query, values)
                        query = "DELETE FROM orders WHERE order_no = %s RETURNING order_no;"
                        values = (order[0],)
                        cursor.execute(query, values)

    query = "DELETE FROM supplier WHERE TIN = %s RETURNING tin;"
    values = (tin,)
    cursor.execute(query, values)
    deleted_tin = cursor.fetchone()

    if deleted_tin:
        # Delete related data from other tables
        delete_query = "DELETE FROM product WHERE sku IN (SELECT sku FROM supplier WHERE TIN = %s);"
        cursor.execute(delete_query, (tin,))

        # Commit the transaction
        connection.commit()

        print("<h2>Supplier Deleted Successfully</h2>")
        print("<p>TIN: {}</p>".format(deleted_tin[0]))
        print("""<p><a href='registerProductSupplier.cgi'>
            <input type="submit" value="Back">
            </a></p>
            """)

    else:
        print("<h2>No Supplier Found with TIN: {}</h2>".format(tin))
        print("""<p><a href='registerProductSupplier.cgi'>
            <input type="submit" value="Back">
            </a></p>
            """)
        


except (Exception, psycopg2.Error) as error:
    # Rollback the transaction on error
    if connection:
        connection.rollback()

    print("<h2>Error Removing Supplier</h2>")
    print("<p>{}</p>".format(str(error)))
    print("""<p><a href='registerProductSupplier.cgi'>
            <input type="submit" value="Back">
            </a></p>
            """)
    
    # Display "Voltar" link as a button
    print('<div class="button-link">')
    print('<a href="registerProductSupplier.cgi">Back</a>')
    print('</div>')

finally:
    # Reset autocommit and close the database connection
    if connection:
        connection.autocommit = True
        connection.close()

print("""
        </div>
    </div>
    </body>
    </html>
""")
