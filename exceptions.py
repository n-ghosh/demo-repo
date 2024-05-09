
x = 0;
amount = 0;
Max = 10;
print("Hello, World! ", x)

while amount < Max:
    print(f"Hi {x}")
    try: #try this
        amount = float(input("Input a float: "))
        if amount < 0:
            print("Input nonnegative number")
        
    except ValueError:
        print("Input a number")
        
    except KeyboardInterrupt:
        print("Bye")
        amount = Max
        break
    except: #contingency
        print("Something went wrong")