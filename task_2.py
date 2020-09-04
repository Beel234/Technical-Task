def prime(n):
    #for i in range(2, n):
    i=2
    j=3
    if n%i==0 or n%j==0:
#prime numbers are numbers which gives a remainder when divided  with values i.e 
#it is only capable of dividing itself and 1
            return False #if the value n divided by 2 doesnt give a remainder hence it isnt a prime number
    else:
        return True #if it does hence in is a prime number 

prime(21)