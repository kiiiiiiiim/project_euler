'''
Created on 2015. 4. 29.

@author: EDGAR
'''
def compute():
    num_list = [x for x in range(2, 21)]
    prime_list = []
    max = 1

    # prime compute
    for x in num_list:
        max *= x
        flag = True
        count = 0 
        for y in range(2, x):
            if x % y == 0:
                flag = False
        
        if flag:        
            prime_list.append(x)
            
    print num_list
    print prime_list
    
    
    count_added = 1
    
    # compute add value
    for x in prime_list:
        count_added *= x
    
    print "max : " , max
    print "add value : ", count_added
    flag = False
    count = count_added
    
    # answer
    while(count <= max):
        flag = True
        for y in range(1, 22):
            if count % y == 0 and flag and y < 21:
                continue
            elif y == 21 and flag:
                print "answer : " , count
                return
            else:
                flag = False
        count += count_added
if __name__ == '__main__':
    compute()
