a_tuple = ("a", "b", "mpilgrim", "z", "example")          
print (a_tuple)
#('a', 'b', 'mpilgrim', 'z', 'example')

print (a_tuple[0] )                                       
#a

print (a_tuple[-1])                                       
#example

print (a_tuple[1:3] )                                     
#('b', 'mpilgrim')

#Tuples are immutable
#print (a_tuple.append("new")) 
#print (a_tuple.remove("z")) 

print (a_tuple.index("example") )  

#Boolean context
def is_it_true(anything):
   if anything:
     print("yes, it's true")
   else:
     print("no, it's false")

print (is_it_true((False,)))       
#yes, it's true
#None

print (type((False)))              
#<class 'bool'>              ##Just False is boolean. Give (False,) for tuple

print (type((False,)))
#<class 'tuple'>

#Assigning Multiple Values At Once
v = ('a', 2, True)
(x, y, z) = v       
print (x)
#a

print (y)
#2

print (z)
#True
