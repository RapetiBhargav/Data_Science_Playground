#Creating a List
a_list = ['a', 'b', 'mpilgrim', 'z', 'example']          
print (a_list)
#['a', 'b', 'mpilgrim', 'z', 'example']

print (a_list[0] )                                       
#a

print (a_list[4] )                                       
#example

print (a_list[-1])                                       
#example

print (a_list[-3])                                       
#mpilgrim

#Slice and dice :)
print (a_list[1:3] )           
#['b', 'mpilgrim']

print (a_list[1:-1])
#['b', 'mpilgrim', 'z']

print (a_list[:3])             
#['a', 'b', 'mpilgrim']

print (a_list[3:] )            
#['z', 'example']

print (a_list[:] )
#['a', 'b', 'mpilgrim', 'z', 'example']

##Adding items to a list

a_list = ['a']
a_list = a_list + [2.0, 3]
print (a_list )                     
#['a', 2.0, 3]

a_list.append(True)                 
print (a_list)
#['a', 2.0, 3, True]

a_list.extend(['four', '/'])        
print (a_list)
#['a', 2.0, 3, True, 'four', '/']

a_list.insert(0, '/')               
print (a_list)
#['/', 'a', 2.0, 3, True, 'four', '/']

#Difference between append and extend to a list
a_list = ['a', 'b', 'c']
a_list.extend(['d', 'e', 'f'])                  
print (a_list)
#['a', 'b', 'c', 'd', 'e', 'f']

print (len(a_list))                             
#6

print (a_list[-1])
#'f'

a_list.append(['g', 'h', 'i'])                  
print (a_list)
#['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i']]

print (len(a_list))                             
#7

print (a_list[-1])
#['g', 'h', 'i']

#Searching For Values In A List
a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
print (a_list.count('new'))       
#2

print ('new' in a_list)           
#True

print ('c' in a_list)
#False

print (a_list.index('mpilgrim'))  
#3

print (a_list.index('new'))       
#2

#print (a_list.index('c') )        
#We get an error c not in list

##Removing Items from a list
a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
print (a_list[1])
#'b'

del a_list[1] 

##Don’t know the positional index? Not a problem
#call the remove() method as often as you like

a_list = ['a', 'new', 'mpilgrim', 'new']
a_list.remove('new')                      
print (a_list)
#['a', 'mpilgrim', 'new']

a_list.remove('new')                      
print (a_list)
#['a', 'mpilgrim']

#print (a_list.remove('new'))
#Exception by now

##Pop:removes the last item in the list and returns the value it removed.
a_list = ['a', 'b', 'new', 'mpilgrim']
print (a_list.pop())   
#mpilgrim

print (a_list)
#['a', 'b', 'new']

print (a_list.pop(1) ) 
#b

print (a_list)
#['a', 'new']

print (a_list.pop())
#new

print (a_list.pop())
#a

#print (a_list.pop())
#Error: Since empyty list

#Lists in boolean context
def is_it_true(anything):
   if anything:
     print("yes, it's true")
   else:
     print("no, it's false")

print (is_it_true([])) 