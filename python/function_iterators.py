'''def sa(num):
    for value in num:
        print(value)



l = [10,20,30,40,50,60,70]
sa(l)'''

def fibo():
    first = 0
    second = 1
    while(True):
        next = first+second
        yield next
        first,second = second,next

g = fibo()

'''print(g) #generator is used in infinity calculations

print(next(g))
print(next(g))
print(next(g))'''
'''
for value in range(10):
    print(next(g))

for value in range(20):  #generators maintain state value it continues next value of above function
    print(next(g))
'''


