# para saber se um set está englobando outro set, se ele é "super"ior.

conjunto_a = {1,2,3};
conjunto_b = {4,1,2,5,6,3};

print(conjunto_a.issuperset(conjunto_b)); # False
print(conjunto_b.issuperset(conjunto_a)); # True