
# Dissecando uma variável

n = input('Digite algo: ')

print('O tipo primitivo digitado é ', type(n))
print('Só tem espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está apenas em maiúscula? ', n.isupper())
print('Está apenas em minúscula? ', n.islower())

# capitalizada é quando tem maiúsculas e minúsculas
print('Está capitalizada? ', n.istitle())
