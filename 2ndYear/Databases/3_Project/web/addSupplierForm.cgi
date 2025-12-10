#!/usr/bin/python3
import cgi

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Add Supplier</title>
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
        .form-container input[type="text"],
        .form-container input[type="number"],
        .form-container textarea {
            width: 200px;
            padding: 5px;
            border-radius: 4px;
            border: 1px solid #aaaaaa;
        }
        .form-container input[type="submit"] {
            margin-top: 10px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            padding: 10px 20px;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            color: #ffffff;
            font-size: 14px;
            text-decoration: none;
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
        <h3>Add Supplier</h3>
        <form method="POST" action="addSupplier.cgi">
          <p>
            <label for="tin">TIN:</label>
            <input type="text" id="tin" name="tin" required>
          </p>
          <p>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
          </p>
          <p>
            <label for="address">Address:</label>
            <input type="text" id="address" name="address" required>
          </p>
          <p>
            <label for="sku">SKU:</label>
            <input type="text" id="sku" name="sku">
          </p>
          <p>
            <label for="date">Date:</label>
            <input type="text" id="date" name="date">
          </p>
            <input type="submit" value="Add Supplier">
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
