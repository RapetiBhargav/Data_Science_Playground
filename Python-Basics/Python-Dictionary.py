a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}          
print (a_dict)
#{'server': 'db.diveintopython3.org', 'database': 'mysql'}

print (a_dict['server'] )                                                   
#db.diveintopython3.org

print (a_dict['database'] )                                                 
#mysql

#Modifying A Dictionary
a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print (a_dict)
#{'server': 'db.diveintopython3.org', 'database': 'mysql'}

a_dict['database'] = 'blog'
print (a_dict)
#{'server': 'db.diveintopython3.org', 'database': 'blog'}

#Adding a pair
a_dict['user'] = 'mark'      
print (a_dict )              
#{'server': 'db.diveintopython3.org', 'database': 'blog', 'user': 'mark'}

#Dictionary values can be of any type - integers, booleans, arbitrary objects, or even other dictionaries
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
             1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

print (len(SUFFIXES))      
#2

print (1000 in SUFFIXES)   
#True

print (SUFFIXES[1000] )    
#['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

print (SUFFIXES[1024])     #④
#['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

print (SUFFIXES[1000][3])  #⑤
#'TB'

#Dictionaries In A Boolean Context
def is_it_true(anything):
   if anything:
     print("yes, it's true")
   else:
     print("no, it's false")

print (is_it_true({}) )            
#no, it's false
#None
print (is_it_true({'a': 1}))       
#yes, it's true
#None