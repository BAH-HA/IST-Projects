#!/usr/bin/python3
import cgi

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Add Customer</title>
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
          width: 100px;
          text-align: right;
          margin-right: 10px;
          color: #fff;
        }

        .form-container input[type="text"],
        .form-container input[type="email"],
        .form-container input[type="tel"],
        .form-container textarea {
          width: 200px;
          padding: 5px;
          border-radius: 5px;
          border: 1px solid #ccc;
          background-color: #fff;
          color: #333;
        }

        .form-container input[type="submit"] {
          margin-top: 10px;
          display: block;
          margin-left: auto;
          margin-right: auto;
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
        <h3>Add Customer</h3>
        <form method="POST" action="addCustomer.cgi">
          <p>
            <label for="cust_no">Customer No:</label>
            <input type="text" id="cust_no" name="cust_no" required>
          </p>
          <p>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
          </p>
          <p>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
          </p>
          <p>
            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone">
          </p>
          <p>
            <label for="address">Address:</label>
            <input type="text" id="address" name="address">
          </p>
          <p>
            <input type="submit" value="Add Customer">
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
