# Very short method to create list of even number fromm a given list
#Advance-Python
print("Method 1: Enter a list and a list containing only even numbers from that list is given as output")
print("Method 2: Enter a range and a list of positive even numbers is returned 
choice = int(input("Which method would yo like to apply(1 or 2) :"))
valid_choices = [1, 2]

if choice == 1:
    list_number=list(map(int,input().split()))
    even_list=[i for i in list_number if i%2==0]
    print(even_list)
elif choice == 2:
    n = int(input("Enter the required range : "))  # user input
    list = []

    if (n < 0):
        print("Not a valid number, please enter a positive number!")
    else:
        print(list(range(0,n+1, 2))) # stes are set to 2 so number returned is always even
else:
    print('Invalid Choice')
