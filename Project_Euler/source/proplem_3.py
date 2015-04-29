import time


max = 142093
computed_max = max
start = time.time()
list = []
######
pos = 2
while(pos <= computed_max):
    for x in list:
        if(pos % x == 0):
            pos += 1
            continue
        3
    if max % pos == 0:
        list.append(pos)
        sum = 1
        
        for x in list:
            sum *= x
            
        computed_max = max - sum
        print pos
        
    pos += 1
    
######
end = time.time()
print str("%.4f ms" % ((end - start) * 1000))
