end = False
while  not end :

    num = int(input("enter a number of ur choce : "))

    def isPrime(num):
        if num%2 == 0 or num%3 == 0 or num%5 == 0 or num%7 == 0 :
            print("it is not a prime number")
        
        else:
            print("it is a prime number")
        
    if(num > 56464):
        end = True    



    isPrime(num)