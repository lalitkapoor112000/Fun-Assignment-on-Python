def makes_twenty(a,b):
    if a+b==20 or a==20 or b==20:
        return True
    else:
        return False

m,n=input("Enter two numbers seperated by comma:").split(",")
print(makes_twenty(int(m),int(n)))
