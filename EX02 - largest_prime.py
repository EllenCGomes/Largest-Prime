def is_prime(x):

    prime = True    
    num_div = 2

    while x > num_div:
    
        if x % num_div == 0:
            prime = False
        num_div = num_div + 1
    
    return prime                            

def biggest_prime(n):
    x = n        
    while x > 1 and is_prime(x) == False:
        x = x - 1
    return x