#!/usr/bin/python3
import cgi
import psycopg2
import login

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Remove Customer</title>
    <style>
        body {
          background-color: #111;
          color: #fff;
          font-family: Arial, sans-serif;
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
          background-color: #222;
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }

        .form-container h3 {
          margin-top: 0;
          color: #fff;
        }

        .form-container p {
          text-align: left;
          margin-bottom: 15px;
        }

        .form-container label {
          display: inline-block;
          width: 150px;
          text-align: right;
          margin-right: 10px;
          color: #fff;
        }

        .form-container input[type="text"],
        .form-container input[type="number"],
        .form-container textarea {
          width: 200px;
          padding: 5px;
          border-radius: 5px;
          border: 1px solid #ccc;
          background-color: #fff;
          color: #333;
        }

        .form-container .button-container {
          text-align: center;
        }

        .form-container input[type="submit"] {
          margin-top: 10px;
          display: inline-block;
          padding: 10px 20px;
          border-radius: 5px;
          border: none;
          background-color: #007bff;
          color: #fff;
          cursor: pointer;
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
        <h3>Remove Customer</h3>
        <form method="POST" action="removeCustomer.cgi">
            <p>
                <label for="cust_no">Customer Number:</label>
                <select id="cust_no" name="cust_no" required>
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
            </p>
            <p class="button-container">
                <input type="submit" value="Submit">
            </p>
        </form>
        <div class="button-link">
        <a href="registerRemoveCustomer.cgi">Back</a>
        </div>
      </div>
    </div>
    </body>
    </html>
""")
