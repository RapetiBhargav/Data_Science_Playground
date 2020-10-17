#list comprehensions, dictionary comprehensions

a_list = [1, 9, 8, 4]
print ([elem * 2 for elem in a_list] )          
#[2, 18, 16, 8]

print (a_list)                                  
#[1, 9, 8, 4]

a_list = [elem * 2 for elem in a_list]          
print (a_list)
#[2, 18, 16, 8]

#Using list comprehension when working with files
import os, glob
print (glob.glob('*.xml') )                                
#['feed.xml']

print ([os.path.realpath(f) for f in glob.glob('*.xml')])  
#Gives back realpath of the file

print ([f for f in glob.glob('*.py') if os.stat(f).st_size < 6000])

import os, glob
print ([(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.xml')] )           
#[(2796, '/usercode/feed.xml')]

import sys
print(sys.path)

print (sys)
#Add your sys path as first item                                                 
print (sys.path.insert(0, 'D:\\DataSciencePractice\\Data_Science_Playground\\Python-Basics'))  
print (sys.path) 

import humansize
print ([(humansize.approximate_size(os.stat(f).st_size), f) for f in glob.glob('*.xml')])  

#Dictionary Comprehensions
import os, glob

metadata = [(f, os.stat(f)) for f in glob.glob('*Python*.py')]             
print (metadata[1])                                                     
# ('Python-Dictionary.py', os.stat_result(st_mode=33261, 
# st_ino=1057919, st_dev=2049, st_nlink=1, st_uid=1003, 
# st_gid=50, st_size=4640, st_atime=1472210494, 
# st_mtime=1472151083, st_ctime=1472210494))

metadata_dict = {f:os.stat(f) for f in glob.glob('*Python*.py')}           
print (type(metadata_dict))                                              
#<class 'dict'>

print (list(metadata_dict.keys()))                                       
#['romantest2.py', 'romantest3.py', 'romantest1.py']

print (metadata_dict['Python-Dictionary.py'].st_size)                           


metadata_dict = {f:os.stat(f) for f in glob.glob('*')}                                  
humansize_dict = {os.path.splitext(f)[0]:humansize.approximate_size(meta.st_size)     
                   for f, meta in metadata_dict.items() if meta.st_size < 6000}         

print (list(humansize_dict.keys()))

#Fun stuff: Swapping key-value in dictionary
a_dict = {'a': 1, 'b': 2, 'c': 3}
print ({value:key for key, value in a_dict.items()})

#Set Comprehensions
a_set = set(range(10))
print (a_set)
#{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print ({x ** 2 for x in a_set} )          
#{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

print ({x for x in a_set if x % 2 == 0})  
#{0, 8, 2, 4, 6}

print ({2**x for x in range(10)})         
#{32, 1, 2, 64, 4, 128, 256, 512, 8, 16}                                      