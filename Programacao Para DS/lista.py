palavra = 'BANANA'

#plv = palavra[0::2]

for i in range(len(palavra)):
    if i % 2 == 0:
        print(palavra[i])


#x=len(palavra)

#print(x)

#print(range(x))
x = 5*palavra[2:5]
print(f' {x} batmaann \n{x}')

palavra = 'termodinamica'

print(palavra[1:8:2])

print(palavra[1:8:3])


palindromo = 'socorro me subi no onibus em marrocos'


print(palindromo[::-1])