import periodictable

Atomic_number = int(input("Enter Element Atomic Number: "))
Element = periodictable.elements[Atomic_number]
print('Atomic number: ',Element.number)
print('Symbol: ', Element.symbol)
print('Name: ', Element.name)
print('Atomic Mass :', Element.mass)
print('Density: ', Element.density)
