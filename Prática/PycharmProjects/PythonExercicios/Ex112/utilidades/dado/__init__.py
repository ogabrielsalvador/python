
def leiaDinheiro(text):
    while True:
        number = str(input(text)).replace(',', '.')
        if number.strip().replace('.', '').isdigit():

            return float(number)
        print(f'\033[1;31mERRO! Por favor, digite um valor monetário válido...\033[m')
