#!/usr/bin/python3
import cgi
import psycopg2
import login

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Remove Product</title>
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
        .form-container {
            width: 400px;
            text-align: center;
            padding: 20px;
            background-color: #222222;
            border-radius: 8px;
        }
        .form-container h3 {
            color: #ffffff;
            margin-bottom: 20px;
        }
        .form-container p {
            text-align: left;
            margin-bottom: 10px;
        }
        .form-container label {
            display: inline-block;
            width: 100px;
            text-align: right;
            margin-right: 10px;
            color: #ffffff;
        }
        .form-container select,
        .form-container textarea {
            width: 200px;
            padding: 5px;
            border: 1px solid #dddddd;
            border-radius: 4px;
        }
        .form-container input[type="submit"] {
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            color: #ffffff;
            font-size: 14px;
            text-decoration: none;
            cursor: pointer;
            display: block;
            margin: 0 auto; /* Center the submit button horizontally */
        }
        .form-container input[type="submit"]:hover {
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
      <div class="form-container">
        <h3>Remove Product</h3>
        <form method="POST" action="removeProduct.cgi">
            <p>
                <label for="sku">SKU:</label>
                <select id="sku" name="sku" required>
""")

connection = None
try:
    # Establishing connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Retrieve products' SKU from the database
    query = "SELECT sku FROM product;"
    cursor.execute(query)
    products = cursor.fetchall()

    # Populate the dropdown with the SKU values
    for product in products:
        sku = product[0]
        print('<option value="{}">{}</option>'.format(sku, sku))
        
    

except (Exception, psycopg2.Error) as error:
    print("<option>Error retrieving products: {}</option>".format(str(error)))
   

finally:
    # Closing database connection
    if connection:
        connection.close()
        
    

print("""
                </select>
            </p>
            <p>
                <input type="submit" value="Submit">
            </p>
        </form>
        <div class="button-link">
        <a href="registerProductSupplier.cgi">Back</a>
        </div>
      </div>
    </div>
    </body>
    </html>
""")


