import pluralIterator

r1 = pluralIterator.LazyRules()
r2 = pluralIterator.LazyRules()
print (r1.rules_filename)                               
#plural-rules.txt

print (r2.rules_filename)
#plural-rules.txt

r2.rules_filename = 'r2-override.txt'                   
print (r2.rules_filename)
#r2-override.txt

print (r1.rules_filename)
#plural-rules.txt

print (r2.__class__.rules_filename )                    
#plural-rules.txt

r2.__class__.rules_filename = 'papayawhip.txt'  
print (r1.rules_filename)
#papayawhip.txt

print (r2.rules_filename)                              
#r2-overridetxt