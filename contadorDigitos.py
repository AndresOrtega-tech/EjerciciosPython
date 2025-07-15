import math

def contar_digitos_string(numero):
    """Cuenta dígitos convirtiendo a string (método más simple)."""
    return len(str(abs(numero)))

def contar_digitos_math(numero):
    """Cuenta dígitos usando logaritmo (método matemático)."""
    if numero == 0:
        return 1
    return math.floor(math.log10(abs(numero))) + 1

def main():
    try:
        # Solicitar entrada al usuario
        numeroUser = int(input("Ingrese un número: "))
        
        # Método 1: Usando conversión a string
        digitos_string = contar_digitos_string(numeroUser)
        
        # Método 2: Usando logaritmo
        digitos_math = contar_digitos_math(numeroUser)
        
        # Imprimir resultado
        print(f"El número tiene {digitos_string} dígitos")
        
    except ValueError:
        print("Error: Por favor ingrese un número entero válido")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
