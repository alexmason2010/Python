largest = None # you don't need this
smallest = None # you don't need this
numlist = []
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else :
        try:
            numlist.append(int(num))
        except:
            print('Invalid input')

largest = max(numlist)
smallest = min(numlist)
    

print("Maximum is", largest)
print("Minimum is", smallest)
