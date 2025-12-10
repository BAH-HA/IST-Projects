#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()

# Retrieve the form field values
cust_no = form.getvalue('cust_no')
name = form.getvalue('name')
email = form.getvalue('email')
phone = form.getvalue('phone')
address = form.getvalue('address')

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Adding Customer</title>
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
        .form-container {
            max-width: 500px;
            margin: 0 auto;
            background-color: #222222;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        }
        .form-container input[type="text"],
        .form-container input[type="email"] {
            width: 100%;
            padding: 10px;
            border-radius: 4px;
            border: none;
            background-color: #1a1a1a;
            color: #ffffff;
            margin-bottom: 10px;
        }
        .form-container input[type="submit"] {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border-radius: 4px;
            border: none;
            background-color: #007bff;
            color: #ffffff;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .form-container input[type="submit"]:hover {
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
        .success-message {
            margin-top: 30px;
            padding: 20px;
            border-radius: 8px;
            background-color: #222222;
            color: #ffffff;
            text-align: center;
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
    # Establishing connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Insert into customer Table
    query = "INSERT INTO customer (cust_no, name, email, phone, address) VALUES (%s, %s, %s, %s, %s);"
    values = (cust_no, name, email, phone, address)
    cursor.execute(query, values)
    connection.commit()

    # Display success message in a box
    print('<div class="success-message">')
    print('<h2>Customer Added Successfully</h2>')
    print('<p>Customer Number: {}</p>'.format(cust_no))
    print('<p>Name: {}</p>'.format(name))
    print('<p>E-mail: {}</p>'.format(email))
    print('<p>Phone: {}</p>'.format(phone))
    print('<p>Address: {}</p>'.format(address))
    print('</div>')

    # Display "Voltar" link as a button
    print('<div class="button-link">')
    print('<a href="registerRemoveCustomer.cgi">Back</a>')
    print('</div>')

except (Exception, psycopg2.Error) as error:
    print("<h2>Error Adding Customer</h2>")
    print("<p>{}</p>".format(str(error)))
    print("""<div class="button-link">
            <a href='registerRemoveCustomer.cgi'>Back</a>
            </div>
            """)
    
    # Display "Voltar" link as a button
    print('<div class="button-link">')
    print('<a href="registerRemoveCustomer.cgi">Back</a>')
    print('</div>')

finally:
    # Closing database connection
    if connection:
        connection.close()

print("""
    </div>
    </body>
    </html>
""")
