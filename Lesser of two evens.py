def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)


m,n=input("Enter two numbers seperated by comma:").split(",")
print(lesser_of_two_evens(int(m),int(n)))
