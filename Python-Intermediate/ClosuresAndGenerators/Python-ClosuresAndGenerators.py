import re
print (re.search('[abc]', 'Mark'))    
#<_sre.SRE_Match object at 0x001C1FA8>

print (re.sub('[abc]', 'o', 'Mark'))  
#Mork

print (re.sub('[abc]', 'o', 'rock'))  
#rook

print (re.sub('[abc]', 'o', 'caps'))  
#oops

def plural(noun):          
    if re.search('[sxz]$', noun):             
        return re.sub('$', 'es', noun)        
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)       
    elif re.search('[^aeiou]y$', noun):      
        return re.sub('y$', 'ies', noun)     
    else:
        return noun + 's'

print (re.search('[^aeiou]y$', 'vacancy'))
#<_sre.SRE_Match object at 0x001C1FA8>

print (re.search('[^aeiou]y$', 'boy'))      
#None

print (re.search('[^aeiou]y$', 'day'))
#None

print (re.search('[^aeiou]y$', 'pita'))     
#None

print (re.sub('y$', 'ies', 'vacancy') )              
#vacancies

print (re.sub('y$', 'ies', 'agency'))
#agencies

print (re.sub('([^aeiou])y$', r'\1ies', 'vacancy'))  
#vacancies

