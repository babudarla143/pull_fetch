n=eval(input('enter the input number'))
m=eval(input('enter the input number'))
if n>m:
    large=n
elif n<m:
    large=m
while True:
    if large%n==0 and large%m==0:
        lcm=large
        break
        print("n is{},m is{}".format(n,m,lcm))
 