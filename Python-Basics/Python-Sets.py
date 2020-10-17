a_set = {1, 2}          
print (type(a_set)) 
#<class 'set'>
print (a_set)
#{1, 2}

#Convert a list to a set
a_list = ['a', 'b', 'mpilgrim', True, False, 42]
a_set = set(a_list)                                   
print (a_set )

#Empty set
a_set = set()            
print (a_set )           
#set()

print (type(a_set))      
#<class 'set'>

print (len(a_set))       
#0

#You can not create an empty set with two curly brackets. This actually creates an empty dictionary, not an empty set.
#print (not_sure = {})

#Modifying a set using add() and update()
a_set = {1, 2}
a_set.add(4)          
print (a_set)
#{1, 2, 4}

print (len(a_set))    
#3

a_set.add(1)          
print (a_set)
#{1, 2, 4}

print (len(a_set))    
#3

a_set = {1, 2, 3}
print (a_set)
#{1, 2, 3}

a_set.update({2, 4, 6})                       
print (a_set )                                
#{1, 2, 3, 4, 6}

a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})  
print (a_set)
#{1, 2, 3, 4, 5, 6, 8, 9, 13}

a_set.update([10, 20, 30])                    
print (a_set)
#{1, 2, 3, 4, 5, 6, 8, 9, 10, 13, 20, 30}

#Removing Items From A Set - Using discard() and remove()
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
print (a_set)
#{1, 3, 36, 6, 10, 45, 15, 21, 28}

a_set.discard(10)                        
print (a_set)
#{1, 3, 36, 6, 45, 15, 21, 28}

a_set.discard(10)                        
print (a_set)
#{1, 3, 36, 6, 45, 15, 21, 28}

a_set.remove(21)                         
print (a_set)
#{1, 3, 36, 6, 45, 15, 28}

#print (a_set.remove(21)) 
#keyError

#Like lists, sets have a pop() method.
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
print (a_set.pop())                                
#1

print (a_set.pop())
#3

print (a_set.pop())
#36

print (a_set)
#{6, 10, 45, 15, 21, 28}

a_set.clear()                                      
print (a_set)
#set()

#print (a_set.pop() ) 
#Error since on empty set

##Common Set Operations
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
print (30 in a_set)                                                     
#True

print (31 in a_set)
#False

b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
print (a_set.union(b_set))                                              
#{1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}

print (a_set.intersection(b_set))                                       
#{9, 2, 12, 5, 21}

print (a_set.difference(b_set) )                                        
#{195, 4, 76, 51, 30, 127}

print (a_set.symmetric_difference(b_set))                               
#{1, 3, 4, 6, 8, 76, 15, 17, 18, 195, 127, 30, 51}

# continued from the previous example
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}

print (b_set.symmetric_difference(a_set))                                       
#{1, 195, 4, 3, 6, 8, 76, 15, 17, 18, 51, 30, 127}

print (b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set))  
#True

print (b_set.union(a_set) == a_set.union(b_set))                                
#True

print (b_set.intersection(a_set) == a_set.intersection(b_set) )                 
#True

print (b_set.difference(a_set) == a_set.difference(b_set) )                     
#False

##few questions you can ask of sets.
a_set = {1, 2, 3}
b_set = {1, 2, 3, 4}
print (a_set.issubset(b_set))    
#True

print (b_set.issuperset(a_set))  
#True

a_set.add(5)                     
print (a_set.issubset(b_set))
#False

print (b_set.issuperset(a_set))
#False

#Sets In A Boolean Context
def is_it_true(anything):
   if anything:
     print("yes, it's true")
   else:
     print("no, it's false")

print (is_it_true(set()))          
#no, it's false
#None

print (is_it_true({'a'}))          
#yes, it's true
#None

print (is_it_true({False}))        
#yes, it's true
#None