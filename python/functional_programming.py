#map
#filter
#lambda

'''def sqr(num1):
    return num1**2

l = [10,20,30,40,50,60]

result = list(map(sqr,l))
print(result)
        #or
for value in result:
    print(value)'''

'''def add(num1,num2):
    return num1+num2

l1 = [100,200,300,400,500]
l2 = [10,20,30,40,50]

result = list(map(add,l1,l2))
print(result)'''

#filter

'''def check_sum(num1):
    if num1%2==0:
        vapt =True
        return vapt
    else:
        return False

l = [100,115,120,125,130,140]

result = list(filter(check_sum,l))#filter purpose is to return the true result as output
print(result)'''

#lambda

'''l = [10,20,30,40,50,60]

result = list(map(lambda num1:num1**2,l))#first num1 is the parameter argument
print(result)'''

'''l = [100,115,120,125,130,140]

result = list(filter(lambda num:num%2==0,l))
print(result)'''

'''d = {8:50,3:40,2:30,1:20,5:10}

l = dict(sorted(d.items(),key=lambda x:x[1]))#we are sorting value in the list
print(l)'''


