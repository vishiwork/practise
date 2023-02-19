# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def pattern(num):
    
    for i in range(0,num,1):
        for j in range(0,i+1):
            print('*',end=' ')
    
        print('\n')
    for i in range(num,1,-1):
        for j in range(i,1,-1):
            print('*',end=' ')
    
        print('\n')

pattern(5)