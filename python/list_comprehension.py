'''l = [100,200,300,400,500]
l2 = [value*value for value in l]'''

'''for value in l:
    l2.append(value*value)

print(l2)'''

'''l = [10,20,30,40,25,35,70,85]
l2 = [value for value in l if value%2 == 0]#we always specify output in starting
print(l2)'''

'''l =[100,105,25,647,25,82]
l2 = ["even" if value%2==0 else "odd" for value in l]
print(l2)'''

#dict comprehension

'''d = {x:x**2 for x in range(1,20)}
print(d)'''

'''d = {chr(x):x for x in range(97,123)}
#print(d)
d2 = {value:key for key,value in d.items()}
print(d2)'''


