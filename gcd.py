#GCD of two numbers
#input a,b are seperated by space in a single line

a,b = map(int,input().split())

#this loop runs until the remainder (b) is zero
while(b!=0):
    c = a%b
    a = b
    b = c
#print GCD of 2 numbers
print(a)    

