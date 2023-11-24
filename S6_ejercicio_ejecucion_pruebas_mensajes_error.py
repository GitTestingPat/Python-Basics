def check_answer(letter):
    if (letter == "Y"):
        return True
    if (letter == "y"):
        return True
    return False

# Prueba para la letra "Y" mayúscula
assert check_answer("Y") == True, "Y es un carácter que significa confirmación, así que la función debería haber devuelto True"

# Prueba para la letra "y" minúscula
assert check_answer("y") == True, "y es un carácter que significa confirmación, así que la función debería haber devuelto True"

# Prueba para un carácter aleatorio "N" mayúscula
assert check_answer("N") == False, "Esto no parece Y o y, así que la función debería haber devuelto False"
