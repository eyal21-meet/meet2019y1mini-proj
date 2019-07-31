def prime(x):
    if int(x) < 2:
        prime_num = False
    else:    
        z = 2
        y = int((int(x))**(0.5)) + 1
        prime_num = True
        while z < y:
            if int(x) % z == 0:
                prime_num = False
                break
            else:
                z += 1
        if prime_num == True:
            print(x)
            primes.append(x)
            
primes = []
def all_primes(limit):
    for i in range(limit):
        prime(i)
       
limit = input("I want to know all the prime numbers until: ")
print(" ")
all_primes(int(limit))
print(" ")
print("number of primes: " + str(len(primes)))
      

