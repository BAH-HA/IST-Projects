#!/usr/bin/python3
import cgi

print('Content-type:text/html\n\n')
print("""
    <html>
    <head>
    <title>Add Order</title>
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
            background-color: #222222;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
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
            border-radius: 3px;
            border: 1px solid #333333;
            background-color: #111111;
            color: #ffffff;
        }
        .form-container input[type="submit"] {
            margin-top: 10px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            background-color: #007bff;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            border-radius: 3px;
            cursor: pointer;
        }
        .product-fields {
            margin-bottom: 10px;
            border-bottom: 1px solid #333333;
            padding-bottom: 10px;
        }
        .product-fields:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }
        .add-product-btn {
            text-align: center;
            margin-top: 20px;
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
        <h3>Add Order</h3>
        <form method="POST" action="addOrder.cgi">
            <p>
                <label for="order_no">Order number:</label>
                <input type="text" id="order_no" name="order_no" required>
            </p>
            <p>
                <label for="cust_no">Customer number:</label>
                <input type="text" id="cust_no" name="cust_no" required>
            </p>
            <p>
                <label for="date">Date:</label>
                <input type="text" id="date" name="date" required>
            </p>
            <div id="product-fields">
                <div class="product-fields">
                    <p>
                        <label for="sku">SKU:</label>
                        <input type="text" name="sku[]" required>
                    </p>
                    <p>
                        <label for="qty">Quantity:</label>
                        <input type="number" name="qty[]" required>
                    </p>
                </div>
            </div>
            <div class="add-product-btn">
                <button type="button" onclick="addProductFields()">Add Product</button>
            </div>
            <p>
                <input type="submit" value="Submit">
            </p>
        </form>
        <div class="button-link">
        <a href="createOrder.cgi">Back</a>
        </div>
      </div>
    </div>

    <script>
        function addProductFields() {
            var productFieldsContainer = document.getElementById("product-fields");
            var productFields = document.createElement("div");
            productFields.classList.add("product-fields");
            productFields.innerHTML = `
                <p>
                    <label for="sku">SKU:</label>
                    <input type="text" name="sku[]" required>
                </p>
                <p>
                    <label for="qty">Quantity:</label>
                    <input type="number" name="qty[]" required>
                </p>
            `;
            productFieldsContainer.appendChild(productFields);
        }
    </script>

    </body>
    </html>
""")