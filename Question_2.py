try:
    n=int(input()) #value error
    b=int(input()) 
    a=input()
    c=n+b
    l=a+b #type error
    n.append(3)  #attribute error
except ValueError:
    raise valueError("valueError raised")
except AttributeError:
    raise AttributeError("AttributeError raised")
except TypeError:
    raise TypeError("TypeError raised")
