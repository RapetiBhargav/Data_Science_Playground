#list comprehensions, dictionary comprehensions

import os                                        
os.getcwd()                                           
#/C:\Python31

#os.chdir('/Users/pilgrim/diveintopython3/examples')   
#os.getcwd() 

#Working With Filenames and Directory Names
print(os.path.join('/Users/pilgrim/diveintopython3/examples/', 'humansize.py'))              
#/Users/pilgrim/diveintopython3/examples/humansize.py

print(os.path.join('/Users/pilgrim/diveintopython3/examples', 'humansize.py'))               
#/Users/pilgrim/diveintopython3/examples\humansize.py

print(os.path.expanduser('~'))                                                               
#/nonexistent

print(os.path.join(os.path.expanduser('~'), 'diveintopython3', 'examples', 'humansize.py'))  
#/nonexistent/diveintopython3/examples/humansize.py

#functions to split full pathnames, directory names, and filenames
pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
print (os.path.split(pathname) )                                       
#('/Users/pilgrim/diveintopython3/examples', 'humansize.py')

(dirname, filename) = os.path.split(pathname)                          
print (dirname )                                                       
#/Users/pilgrim/diveintopython3/examples

print (filename )                                                      
#humansize.py

(shortname, extension) = os.path.splitext(filename)                    
print (shortname)
#humansize

print (extension)
#.py

#Listing Directories
import os
os.chdir('/Users/pilgrim/diveintopython3/')
import glob

glob.glob('examples/*.xml')                  
#['examples\\feed-broken.xml',
# 'examples\\feed-ns0.xml',
# 'examples\\feed.xml']

os.chdir('examples/')                        
glob.glob('*test*.py')                       

#Getting File Metadata
import os
print(os.getcwd())                         
#/usercode

metadata = os.stat('feed.xml')             
print (metadata.st_mtime)                  
#1317786276.0

import time                                
print (time.localtime(metadata.st_mtime))  

metadata.st_size                              
#3070

import humansize
humansize.approximate_size(metadata.st_size)
#'3.0 KiB'

#Constructing Absolute Pathnames
print(os.getcwd())
#/usercode

print(os.path.realpath('feed.xml'))
#/usercode/feed.xml
