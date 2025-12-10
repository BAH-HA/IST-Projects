#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()

# Retrieve the form field values
sku = form.getvalue('sku')

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Deleting Product</title>
    <style>
        body {
            background-color: #111111;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            color: #ffffff;
        }
        .center {
            margin-left: auto;
            margin-right: auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
        }
        .container {
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
    

    # Delete from contains Table
    query = "DELETE FROM contains WHERE sku = %s RETURNING order_no;"
    values = (sku,)
    cursor.execute(query, values)
    order_no = cursor.fetchall()

    if order_no:
        query = "SELECT TIN FROM supplier WHERE sku = %s;"
        values = (sku,)
        cursor.execute(query, values)
        deleted_tin = cursor.fetchone()[0]
        
        query = "DELETE FROM delivery WHERE TIN = %s RETURNING TIN;"
        values = (deleted_tin,)
        cursor.execute(query, values)
        
        query = "DELETE FROM supplier WHERE sku = %s RETURNING sku;"
        values = (sku,)
        cursor.execute(query, values)


        for order in order_no:
            query = "SELECT order_no FROM contains WHERE order_no = %s ;"
            values = (order[0],)
            cursor.execute(query, values)
            order_no1 = cursor.fetchall()

            if not order_no1:
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
    
    query = "DELETE FROM product WHERE sku = %s RETURNING sku;"
    values = (sku,)
    cursor.execute(query, values)
    sku_product = cursor.fetchone()
    
    # Commit the transaction
    connection.commit()
    
    if sku_product:
        print("<h2>Product Deleted Successfully</h2>")
        print("<p>SKU: {}</p>".format(sku_product[0]))
    else:
        print("<h2>No Product Found with SKU: {}</h2>".format(sku))

    print("""
    <form action="registerProductSupplier.cgi" method="post">
        <input type="submit" value="Voltar">
    </form>
    """)

except (Exception, psycopg2.Error) as error:
    # Rollback the transaction on error
    if connection:
        connection.rollback()
    print("<h2>Error Deleting Product</h2>")
    print("<p>{}</p>".format(str(error)))
    print("""
    <form action="registerProductSupplier.cgi" method="post">
        <input type="submit" value="Voltar">
    </form>
    """)

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
