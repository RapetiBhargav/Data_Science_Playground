import re
    
def make_counter(x):
     print('entering make_counter')
     while True:
         yield x                           
         print('incrementing x')
         x = x + 1
 

counter = make_counter(2)                  
print (counter)                            
#<generator object at 0x001C9C10>

print (next(counter))                      
#entering make_counter
#2

print (next(counter))                      
#incrementing x
#3

print (next(counter))                      
#incrementing x
#4

###“yield” pauses a function. “next()” resumes where it left off.

##A Fibonacci Generator
def fib(max):
    a, b = 0, 1          
    while a < max:
        yield a          
        a, b = b, a + b

for n in fib(1000):      
    print(n, end=' ')    

#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

print (list(fib(1000)))  
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

##A Plural Rule Generator
def build_match_and_apply_functions(pattern, search, replace):     #①
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename='plural-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))