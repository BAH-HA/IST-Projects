#!/usr/bin/python3
import cgi
import psycopg2
import login

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Choose customer</title>
    <style>
        body {
            background-color: #111111;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
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
            padding: 20px;
            border-radius: 4px;
            background-color: #222222;
        }
        .client-form select {
            width: 200px;
            padding: 6px 10px;
            border-radius: 4px;
            border: 1px solid #222222;
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
    </style>
    </head>
    <body>
""")

print("""
    <div class="container">
    <button class="return-button" onclick="window.location.href='mainMenu.cgi'">Return to Menu</button>
""")

print("""
    <div class="center">
        <h2>Choose customer</h2>
        <div class="client-form">
            <form method="GET" action="choseOrder.cgi">
                <label for="client_id">Customer number:</label>
                <select id="client_id" name="client_id" required>
""")

connection = None
try:
    # Establishing connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Retrieve clients' client_no from the database
    query = "SELECT cust_no FROM customer;"
    cursor.execute(query)
    clients = cursor.fetchall()

    # Populate the dropdown with the client_no values
    for client in clients:
        client_no = client[0]
        print('<option value="{}">{}</option>'.format(client_no, client_no))

except (Exception, psycopg2.Error) as error:
    print("<option>Error retrieving clients: {}</option>".format(str(error)))

finally:
    # Closing database connection
    if connection:
        connection.close()

print("""
                </select>
                <input type="submit" value="Submit">
            </form>
        </div>
    </div>
""")

print("""
    </body>
    </html>
""")
