'''r => read
r+
w = > write
w+
a => append
a+'''


#s = open("datatypes.py","r")
'''content = s.read()
print(content)'''

'''content = s.read(25)
print(content)'''
'''print("---------")
content =s.read()
print(content)'''

#readlines
#readline
#readline function only return one line
#read function return in string and readlines return in list
'''content = s.readlines()
print(content)'''

'''content = s.readline()
print(content)'''

'''fp = open("functionss.py","w") #even the file doesn't exist the python create a new file and write
fp.write("#write this program")'''

'''fp = open("functionss.py","w+") #even the file doesn't exist the python create a new file and write+ is used read and write operation
print(fp.tell())
fp.write("#write this program")#same goes for r+ too
print(fp.tell())
print(fp.seek(0,0))
content = fp.read()
print(fp.tell())
print(content)'''


#tell => current fp position
#seek(offset,position) => to change the fp position

'''offset => number of char
position => 0 => start of the file
            1 => current position 
            2 => end of the file'''

#seek(15,0) => change the fp by 15 char from start of the file
#seek(0,2)  => change fp by 0 char from end of the file


#r+ is used to add the content = read + write

'''content = open("functionss.py","r+")
fp = content.read()
print(fp)

content.write("\n\n#sample line added using python script")'''

#a
#a+

#r,r+,w,w+ => fp is at start
#a and a+ => at the end






