a = 0
b = 50

for i in range(a, b+1):
    if i % 15 == 0:
        print('FOOBAR')
    elif i % 5 == 0:
        print('BAR')
    elif i % 3 == 0:
        print('FOO')
    else:
        print(i)

# This is step in my nonsense