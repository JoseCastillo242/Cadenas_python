price = input("Introduce la cantidad en euros con 2 decimales: ")
head, sep, tail = price.partition('.')
print("Son", head, "euros con", tail, "centimos")
#intente hacerlo con float pero aparentemente solo funciona con string
