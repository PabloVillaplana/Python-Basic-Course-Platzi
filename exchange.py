
def foreign_exchange_calculator(amount):
    max_to_dolara_rate = 562.97

    return amount / max_to_dolara_rate

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte colones a dolares')
    print('')

    amount = float(input('Digite el monto en Colones: '))

    result = foreign_exchange_calculator(amount)

    print('${} colones son ${} dolares'.format(amount,result))
    print('')


if __name__ == "__main__":
    run()