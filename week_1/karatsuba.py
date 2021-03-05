def karatsuba(num1, num2):

    a, b = num1[:len(num1)//2], num1[len(num1)//2:]
    c, d = num2[:len(num2)//2], num2[len(num2)//2:]

    if len(a) == 1 and len(b) == 1 and len(c) == 1 and len(d) == 1:

        ac = str(int(a) * int(c))
        ad = str(int(a) * int(d))
        bc = str(int(b) * int(c))
        bd = str(int(b) * int(d))

    else:

        ac = karatsuba(a, c)
        ad = karatsuba(a, d)
        bc = karatsuba(b, c)
        bd = karatsuba(b, d)

    return str((10 ** len(num1))*int(ac) +\
               (10**(len(num1)//2))*(int(ad) + int(bc)) + int(bd))



if __name__ == '__main__':

    num1 = '3141592653589793238462643383279502884197169399375105820974944592'
    num2 = '2718281828459045235360287471352662497757247093699959574966967627'

    print(karatsuba(num1, num2))
    print('===============================')
    print(int(num1) * int(num2))
