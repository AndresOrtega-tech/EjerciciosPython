#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles 
# para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la 
# pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print('''Ingredientes Vegetarianos
    - Pimento
    - Tofu
      
Ingredientes no Vegetarianos
    - Peperoni
    - Jamon
    - Salmon''')

ingrediente = input('Escribe el ingrediente que quieres, ademas de tomate y mozarella: ')

if ingrediente == 'Peperoni' or ingrediente == 'Jamon' or ingrediente == 'Salmon':
    print('Tu pizza no es vegetariana')
elif ingrediente == 'Pimento' or ingrediente == 'Tofu':
    print('Tu pizza es vegetariana')
else:
    print('No tenemos ese ingrediente')