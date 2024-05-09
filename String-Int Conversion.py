def string_to_int(string):
    num = 0
    ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    string = string[::-1] #start from the end
    for i in range(len(string)): 
        for j in ints:
            if float(string[i]) == j:
                num += j*(10**i)
    return num

def int_to_string(i):
    s = f"{i}"
    return s
    
sStr = "11233"
print(string_to_int(sStr))

i = 3
print(int_to_string(i))