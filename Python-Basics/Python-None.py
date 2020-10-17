#Comparing None to anything other than None will always return False

print (type(None))
#<class 'NoneType'>

print (None == False)
#False

print (None == 0)
#False

print (None == '')
#False

print (None == None)
#True

x = None
print (x == None)
#True

y = None
print (x == y)
#True

#None In A Boolean Context

def is_it_true(anything):
   if anything:
     print("yes, it's true")
   else:
     print("no, it's false")

print (is_it_true(None))
#no, it's false
#None

print (is_it_true(not None))
#yes, it's true
#None