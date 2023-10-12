def es_valido(s):
    balance = 0  # Variable para llevar el equilibrio de paréntesis

    for char in s:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
        
        # Si en algún momento el balance se vuelve negativo, significa que hay un cierre sin una apertura previa
        if balance < 0:
            return False
    
    # Al final del bucle, el balance debe ser igual a cero para que los paréntesis sean válidos
    return balance == 0

cadena = input("Ingrese una cadena con paréntesis: ")

if es_valido(cadena):
    print("Los paréntesis en la cadena son válidos.")
else:
    print("Los paréntesis en la cadena no son válidos.")
