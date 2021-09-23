x=int(input("no of patient:-"))
y=int(input("no of minutes:-"))
if y<=10:
    z=0
    for i in range(x):
        z+=y
        l=z
    print("last patient will wait:-",l-y)
else:
    print("we don't give more then 10 min" )