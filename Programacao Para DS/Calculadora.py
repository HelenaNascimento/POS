def sum(a, b):
    
    x = a + b
    print(f'Resultado é: {x}')

def sub(a, b):
    
    x = a - b
    print(f'Resultado é: {x}')

def mult(a, b):
    
    x = a * b
    print(f'Resultado é: {x}')

def div(a, b):
    
    x = a / b
    print(f'Resultado é: {x}')

def rest(a, b):
    
    x = a % b
    print(f'Resultado é: {x}')

def exp(a, b):
    
    x = a ** b
    print(f'Resultado é: {x}')

a = int(input('Informe o valor a: '))
b = int(input('Informe o valor b: '))
op = int(input('Informe a operação: \n1.Soma; \n2.Subracao; \n3.Mult; \n4.Div; \n5.Resto; \n6.Expoe: '))

if op == 1:
    sum(a, b)
elif op == 2:
    sub(a, b)
elif op == 3:
    mult(a, b)
elif op == 4:
    div(a, b)
elif op == 5:
    rest(a, b)
elif op == 6:
    exp(a, b)
else:
    print('Operação invalida')