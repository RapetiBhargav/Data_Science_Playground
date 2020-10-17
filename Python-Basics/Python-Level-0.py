SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))

###Add to system search path: 
import sys                                                        
print (sys.path)                                                  
print (sys)
#Add your sys path as first item                                                 
#print (sys.path.insert(0, '/home/mark/diveintopython3/examples'))  
print (sys.path) 

#Catching Import Errors
try:
  import chardet
except ImportError:
  chardet = None
  
if chardet:
  print("do something")
else:
  print("continue anyway")
  
#To prioritize one api over another 
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

#boolean operations
########################
size = 1
print (size < 0)
#False

size = 0
print (size < 0)
#False

size = -1
print (size < 0)
#True

#booleans can be treated as numbers. True is 1; False is 0.
print (True + True)
#2

print (True - False)
#1

print (True * False)
#0

#division by zero
#print (True / False)


#Numbers:
############
print (type(1))                 
#<class 'int'>

print (isinstance(1, int) )     
#True

print (1 + 1 )                  
#2

print (1 + 1.0 )                
#2.0

print (type(2.0))
#<class 'float'>

#Coercing numbers
print(float(2)) 

#Number operations:
#divide
print (11 / 2)     
#5.5

#rounds “up” to the nearest integer.
print (11 // 2)     
#5

x = -11
print ( x // 2)     
#−6

print (11.0 // 2)   
#5.0
#To the power of 2
print (11 ** 2)     
#121
#Reminder
print (11 % 2)      
#1

#Fractions:
import fractions                      
x = fractions.Fraction(1, 3)          
print (x)
#Fraction(1, 3)

print (x * 2 )
#Fraction(2, 3)                        

print (fractions.Fraction(6, 4))      
#Fraction(3, 2)

#Trignometry
import math
print (math.pi )               
#3.141592653589793

print (math.sin(math.pi / 2))  
#1.0

print (math.tan(math.pi / 4))  
#0.99999999999999989

#Numbers as boolean context:
def is_it_true(anything):             
  if anything:
     print("yes, it's true")
  else:
     print("no, it's false")   

print (is_it_true(1)) 
#yes, it's true
#None



