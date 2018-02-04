from random import randint

MATCHES = 15
results = ["1","X","2"]
results15 = ["2","1","0","M"]

for i in range(0,MATCHES):
    x =  randint(0,2) 
    print ("%d .- %s "%(i+1, results[x]))
    if (i == 14):
        y = randint(0,3)
        z = randint(0,3)
        print ("%d .- %s - %s "%(i+1, results15[y], results15[z]))    
