def h_m_p_u(num):
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
                primes.append(x)
                
    primes = []
    def all_primes(limit):
        for i in range(limit):
            prime(i)
           
    all_primes(int(num))
    return len(primes)
import turtle
turtle.hideturtle()
turtle.goto(-1000, 0)
turtle.goto(1000,0)
turtle.goto(0, 0)
turtle.goto(0, 1000)
turtle.goto(0, -1000)
turtle.goto(0, 0)
n = 0
turtle.speed("fastest")
while n < 10000:
    length = h_m_p_u(n)      
    turtle.goto(n, length)
    n += 0000000000000000000000.1
turtle.mainloop()
