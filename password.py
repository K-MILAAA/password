import random
caracteres = "=!#$%&/()=?¡¿@-+*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZñÑ"
lenght = int(input("¿Cuántos caracteres ocupa tu contraseña? "))
contra = ""
for i in range(lenght):
    contra += random.choice(caracteres)
print(contra)
