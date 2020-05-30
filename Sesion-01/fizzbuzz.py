# RETO: FizzBuzz

# 1. Imprime lista de enteros del 1 al 20
# 2. Si el número es múltiplo de 3 y 5 remplazar por FizzBuzz
# 3. Si no, entonces es múltiplo de 3 remplazar por Fizz
# 4. Si no, entonces es múltiplos de 5 remplazar por Buzz
# 5. Si no, entonces imprime el número

n = 20
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
