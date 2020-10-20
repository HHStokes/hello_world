import cmath
from cmath import sqrt

def main():
    print("Hello, I am a quaratic formula calculator")
    # x = (-b +-(b^2-4ac)^-2)/2a
    try: 
        a = float(input("What is A: "))
        b = float(input("What is B: "))
        c = float(input("What is C: "))
    except:
        print("Input not valid")

    else: 
        # breaking up each section into smaller easier to
        # handle parts
        # q = (b^2 - 4ac)

        q = (b*b) - (4*a*c)
        r1 = -b + q
        r2 = -b - q

        x1 = r1 / (a * 2)
        x2 = r2 / (a * 2)
        print("x is equal to: ")
        print(x1,"and",x2)
    
    
main()

