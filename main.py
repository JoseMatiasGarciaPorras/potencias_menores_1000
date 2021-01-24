def run():
    print('CALCULADORA DE POTENCIAS')
    base = int(input('Introduce el número cuyas potencias quieres calcular: '))
    resultado = 0
    potencia = 0
    while True:
        resultado = base ** potencia
        if resultado < 1000:
            print('{} elevado a {} es igual a {}'.format(base, potencia, resultado))
            potencia = potencia + 1
        else:
            break



if __name__ == '__main__':
    run()
