account = input("Introduce tu correo electronico: ")
head, sep, tail = account.partition('@')
print('{}@ceu.es'.format(head))
