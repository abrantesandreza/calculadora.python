print('Vamos juntos realizar operações!!')
print('Digite + para escolher adição!')
print('Digite - para escolher subtração!')
print('Digite * para escolher multiplicação!')
print('Digite / para escolher divisão!')
print('Digite S para finalizar o programa.')

while True:
    op = input('Qual operação deseja realizar? ')
    if ((op != '+') and (op != '-') and (op != '*') and (op != '/') and (op != 'S')):
        print('Você escolheu uma operação inválida! Vamos tentar novamente!!')
        continue
    elif (op == 'S'):
        print('Você escolheu encerrar as operações.')
        break

    num = float(input('Maravilha!! Agora digite o primeiro valor que deseja calcular:  '))
    num2 = float(input('E por último, digite o segundo valor que deseja calcular:  '))

    if (op == '+'):
        print('Você escolheu adição!! E seu cálculo é: {} + {} = {}'.format(num, num2, num+num2))
        continue

    elif (op == '-'):
        print('Você escolheu subtração!! E seu cálculo é: {} - {} = {}'.format(num, num2, num-num2))
        continue

    elif (op == '*'):
        print('Você escolheu multiplicação!! E seu cálculo é: {} * {} = {}'.format(num, num2, num*num2))
        continue

    elif (op == '/'):
        print('Você escolheu divisão!! E seu cálculo é: {} / {} = {}'.format(num, num2, num/num2))

print('Finalizando programa...')

