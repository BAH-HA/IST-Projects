#!/usr/bin/python3
print('Content-type:text/html\n\n')
print("""
<html>
<head>
    <title>Menu</title>
    <style>
        body {
            background-color: #111111;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            color: #ffffff;
        }
        .center {
            text-align: center;
            margin-top: 200px;
        }
        h2 {
            color: #ffffff;
            font-size: 48px;
            font-weight: bold;
            letter-spacing: 2px;
            font-family: 'Metaverse', sans-serif;
            margin-bottom: 40px;
        }
        .menu-buttons {
            display: flex;
            justify-content: center;
            margin-top: 40px;
            flex-wrap: wrap;
        }
        .menu-buttons a {
            display: inline-block;
            margin: 10px;
            padding: 20px 40px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 50px;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            transition: background-color 0.3s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
        .menu-buttons a:hover {
            background-color: #0056b3;
        }
    </style>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Metaverse">
</head>
<body>
<div class="center">
    <h2>Menu</h2>
    <div class="menu-buttons">
        <a href="registerProductSupplier.cgi">Register/Remove Products and Suppliers</a>
        <a href="changePriceDescription.cgi">Change Product Prices and Descriptions</a>
    </div>
    <div class="menu-buttons">
        <a href="registerRemoveCustomer.cgi">Register/Remove Customers</a>
        <a href="createOrder.cgi">Place Orders</a>
        <a href="choseClient.cgi">Pay Order</a>
    </div>
</div>
</body>
</html>
""")
