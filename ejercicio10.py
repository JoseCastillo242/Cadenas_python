products = input("Ingresa los productos de la cesta de la compra, separados por comas: ")
prod_list = products.split(',')
for products in prod_list:
    print(products.strip())
