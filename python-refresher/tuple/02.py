#Unpacking tuple
a,b,_,d,e,f =(1,2,3,4,5,6)
print(a,b,d,e,f)


a,*b,e =('mango','guava','pawpaw','cashew','peanut')
print(a,b,e)