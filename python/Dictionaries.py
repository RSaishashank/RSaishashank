'''alien={'colour':'green','point':5}
print(alien['colour'])
print(alien['point'])
new = alien['point']
print("you earned",str(new),"points")
alien["x_position"]=5
alien['y_position']=25
print(alien)

alien={}
alien['colour']='green'
alien['points']=str(5)
print(alien)
alien['color']='red'#code modified to red.
print(alien)

alien={'x_position':0, 'y_position':25,'speed': 'medium' }
print("original x-position:"+ str(alien['x_position']))

if alien['speed']=='slow':
    x_increment=1
elif alien['speed']=='medium':
    x_increment = 2
else :
    x_increment = 3

alien["x_position"]=alien['x_position'] + x_increment
print("new position"+str(alien["x_position"]))

person={'first name':'Sai Shashank','last name':'Ragi', "age":str(22),'Place':'mancherial'}
for key, value in person.items():
   print(value)
   print(key)

person={'first name':'shashi','last name':'ragi','age':str(18),'place':'mncl'}
for name in person.values():
    print(name)

person={'first name':'shashi','last name':'ragi','age':str(18),'place':'mncl'}
if 'shashi' in person.values():
    print("shashi is there")
else:
    print("shashank")'''

'''d={"shashi": 3,"shasha":50}
print(d.items())'''

'''a = {1,2,3,4,5}
b = {1,4,9,16,25}

d=dict(zip(a,b))
print(d)'''

#l = [1,2,3,4,5]
'''d = dict.fromkeys(l,0)
print(d)'''

'''d1 ={1:1,2:5,6:10,4:16}
2 ={5:25,6:36,7:49}

d1.update(d2)
print(d1)'''

#pop
#popitem
#clear
#del

'''r = l.pop(2)
print(l,r)'''
'''dl = {5:10,6:30,10:25}
r = dl.popitem()
print(dl,r)'''

'''del d1
print(d1)'''




























   