birth = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
day, month, year = birth.split('/')
day = day.zfill(2)
month = month.zfill(2)
print(f"Dia: {day}")
print(f"Mes: {month}")
print(f"Año: {year}")

