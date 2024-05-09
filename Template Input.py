# Writing a template function to get and validate input

# Main program
def main():
    s1 = getInput("Input str: ")
    print (s1)
    f2 = getInput("Input float: ", "non-negative float")
    print (f2)
    
    return

def getInput(sPrompt, sType= "string"):
    """Get and validate user input for one of the following types:
    string, bool, float, int, non-negative float, non-negative int"""
    
    # Types of input the function can handle
    INPUT_TYPES = ["string", "bool", "float", "int", 
                   "non-negative float", "non-negative int", ]
    
    # check if the requested input is a valid type
    if sType not in INPUT_TYPES: 
        raise ValueError
    
    # a var to store the input
    varInput = None
    while True:
        try:
            varInput = input(sPrompt)
            if sType == "string":
                return varInput
            elif sType == "bool":
                return bool(varInput)
            elif sType == "float" or sType == "non-negative float":
                varInput = float(varInput)
                if sType == "float" or varInput >= 0:
                    return varInput
                else: raise ValueError
            else: #sType == "int" or sType == "non-negative int":
                varInput = int(varInput)
                if sType == "int" or varInput >= 0:
                    return varInput
                else: raise ValueError
        except KeyboardInterrupt:
            print("\nGoodbye.")
            raise SystemExit
        except ValueError:
            print("\nError, input must be: " + sType)
        except:
            print("\nSomething went wrong.")
            return None
        
        print(f"Could not accept '{varInput}'. Please try again.")

    return #varInput


# The first line actually executed, calling main()
main()