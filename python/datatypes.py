#string are immutable
#string is odered data structure
#indexing
#s= "python is a simple language"
'''print(s[0])
print(id(s))
s = "shashank"
print(id(s))'''

#slicing
'''s="shashank"
print(s[0:6])
print(s[:2])
print(s[:-8])'''

#strid

'''print(s[::2])
print(s[0::2])
print(s[1::2])
'''
#builtin function of datatypes

'''num1 = 100
num2 = 200
print("value of num1 {value1},value of num2 {value2}".format(value1=num1,value2=num2))'''

#pop
#remove
#clear
#del

'''l=[10,20,30,40,50,10]'''
'''r=l.pop(1)
print(l,r)'''
'''l.remove(20)
print(l)'''

'''l.clear()
print(l)'''

'''l.sort()
print(l)'''

'''print(l.sort())
print(l[::-1])
l.reverse
print(l)'''

'''d = sorted(l)
print(d)'''

'''print(l.count(30))'''

'''d = [10,20,30,10]
f = [50,60,20,10]
s = d+f
s.sort()
print(s)'''


#tuple
#immutable datastructure
#ordered indexing and slicing
t = (10,20,30,40,50,60)
#print(t,type(t))
#help(tuple)
#print(t[10])
#print(t[::])

#print(t.index(20))
#print(t.count(20))

l = [10,20,30,40,50,60]

#for index,value in enumerate(l):
#    print(index,value)

#for t in enumerate(l):
#    print(t[1])

'''t = tuple(l)
print(t)'''

'''t = ("a","b","c",100)
l = list(t)
print(l,type(l))'''


#Sets
#sets are mutable
#all the elements should be unique
#immutable element in the set - int float tuple str
#unordered 

'''s = {10,20,30,40,10,20,30,40}
print(s)'''

#s1 = {10,20,30,40,50,60}
#s2 = {40,50,60,70,80,90}

'''s3 =s1.union(s2)
print(s3)'''
#s3 = s1.intersection(s2)
#print(s3)

'''s3= s1.difference(s2)
print(s3)
s3 = s2.difference(s1)
print(s3)'''

'''s3 = s1.symmetric_difference(s2)
print(s3)'''

'''s1 = {100,200,300,400,500}
s2 = {100,200,300}

print(s2.issubset(s1))
print(s1.issuperset(s2))'''

'''l1 = [100,200,300,400,500]
l2 = [50,20,15,25,5,62,45]

s1 =set(l1)
s2 =set(l2)
s3 = s1.union(s2)
print(s3)'''

'''l3 = sorted(s3)
print(l3)'''

'''l3 = list(s3)
print(l3)

l3.sort()
print(l3)'''
'''
pop
remove
discard
clear
del'''

s = {100,200,300,400,500,600}
 
'''r = s.pop()#cannot remove particular element
print(r)'''

'''r = s.remove(100)#remove particular element but cant show which element it was
print(r)'''

'''s.discard(1000)
print(s)
'''





