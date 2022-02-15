# amount = 2333
# if(amount > 1000)
# print("You are eligible to purchase Dsa Self Paced")
#runtime error
# a = [1, 2, 3]
# try:
# 	print ("Second element = %d" %(a[1]))
# 	print ("Fourth element = %d" %(a[3]))
#
# except:
# 	print ("An error occurred")


#  handle multiple errors
# def fun(a):
#     if a < 4:
#          b = a / (a - 3)
#     print("Value of b = ", b)
# try:
#     #fun(3)
#     fun(5)
#     # multiple exceptions
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:
#     print("NameError Occurred and Handled")


# Program to depict else clause with try-except
def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
