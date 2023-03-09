'''x = range(6)    #range()
for i in x:
	print(i)

x = range(7, 10)
for i in x:
	print(i)

x = range(11, 20, 2)
for i in x:
	print(i)

print('enter your name:')   #input()
x = input()
print('hello, ' + x)

x = input("Enter your name:")
print('hello, ' + x)'''

x = ('apple', 'banana', 'cherry')    #enumerate()
y = enumerate(x)
print(list(y))

a = (1, 2, 3, 4, 5)    #sum()
x = sum(a)
print(x)

a = (1, 2, 3, 4, 5)
x = sum(a, 22)
print(x)

x = max(5, 10)   #max()
print(x)

x = max('mike', 'john', 'vicky')
print(x)

a = (1, 5, 3, 9)
x = max(a)
print(x)

a = ('a', 'b', 'z', 'm', 'q')
x = max(a)
print(x)

x = min(5, 10)   #min()
print(x)

x = min('mike', 'john', 'vicky')
print(x)

a = (1, 5, 3, 9)
x = min(a)
print(x)

a = ('a', 'b', 'z', 'm', 'q')
x = min(a)
print(x)