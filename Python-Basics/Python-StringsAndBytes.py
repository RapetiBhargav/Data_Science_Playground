s = '&^ Python'              
print (len(s))               
#9

print (s[0])                 
#&

print (s + ' 3')             
#&^ Python 3

#{0} is replaced by the 1st format() argument. {1} is replaced by the 2nd.
username = 'Bhargav'
password = 'NoneOfYourBusiness'                                     
print ("{0}'s password is {1}".format(username, password))  

import humansize,sys
si_suffixes = humansize.SUFFIXES[1000]              
print (si_suffixes)
#['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

print ('1000{0[0]} = 1{0[1]}'.format(si_suffixes))  
#'1000KB = 1MB'

print ('1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys))
#1MB = 1000KB

#Format Specifiers
print ('{0:.1f} {1}'.format(698.24, 'GB'))
#698.2 GB

#Common string methods
s = '''Finished files are the re-  
 sult of years of scientif-
 ic study combined with the
 experience of years.'''
                                    
print(s.splitlines())               
#['Finished files are the re-',
# 'sult of years of scientif-',
# 'ic study combined with the',
# 'experience of years.']

print(s.lower())                    
#finished files are the re-
#sult of years of scientif-
#ic study combined with the
#experience of years.

print(s.lower().count('f'))  

query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&')          #better off using the urllib.parse.parse_qs() function                               
print (a_list)
#['user=pilgrim', 'database=master', 'password=PapayaWhip']

a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v]  
print (a_list_of_lists)
#[['user', 'pilgrim'], ['database', 'master'], ['password', 'PapayaWhip']]

a_dict = dict(a_list_of_lists)                                   
print (a_dict)
#{'user': 'pilgrim', 'database': 'master', 'password': 'PapayaWhip'}

#Slicing
a_string = 'My alphabet starts where your alphabet ends.'
print (a_string[3:11])

#Strings vs Bytes
by = b'abcd\x65'
print (by)
#b'abcde'

print (type(by) )         
#<class 'bytes'>

print (len(by) )          
#5

by += b'\xff'             
print (by)
#b'abcde\xff'

print (len(by))           
#6

print (by[0])             
#97



