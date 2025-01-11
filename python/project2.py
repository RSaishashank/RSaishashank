for i in range(1,6):
            for j in range(1,6):
              print(i,j)
              if i ==int(5) and j ==int(1):
                  print("key found")
              elif i==int(2) and j==int(1):
                    print("key found of 1,2")
              else:
                    print("key not found")      

alien =['green','yellow','red']

if 'green' in alien:
      print("player got 5 points")
elif 'red' in alien:
      print("player got 5 points")
else:
      print("player got 15 points")

age = int(input("enter the age: "))
if age<2:
      print("baby")
elif age >=2 and age < 4:
      print("toodler")
elif age >=4 and age < 13:
        print("kid")
elif age >=13 and age<20:
      print("teenager")
elif age >= 20 and age <65:
      print("adult")
elif age >=65 and age <100:
      print("too old")
else:
      print("maybe dead")

