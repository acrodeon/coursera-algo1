##########################################
# Algo1 Week1 : Karatsuba Multiplication #
##########################################

def karatsuba(x,y):
    """x = 10**n/2 * a + b   y = 10**n/2 * c + d"""
    if x < 10 and y <10:
        return x*y
    else:
        if x > y:
            divider = pow(10,len(str(x))//2)
        else:
            divider = pow(10,len(str(y))//2)
    a = x // divider
    b = x % divider
    c = y // divider
    d = y % divider
    #print (a)
    #print (b)
    #print (c)
    #print (d)
    # recursive calls for a*c, b*d
    karatsuba(a,c)
    karatsuba(b,d)
    # intermediate additions
    e = a+b
    f = c+d
    # recursive call for e*f
    karatsuba(e,f)

    return (a*c*pow(divider,2) + b*d + ((e*f-b*d-a*c)*divider))

##################
# Main() to test #
##################
if __name__ == '__main__':
    x = int(input("Enter first number "))
    y = int(input("Enter second number "))
    result = karatsuba(x,y)
    print("{0} * {1}  = {2}".format(x,y,result))
