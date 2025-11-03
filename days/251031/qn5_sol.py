### Problem 5

    #Write a Python program that:

    #1. Accepts a sequence of numbers from the user.
    #2. Stores the numbers in a list and finds the **maximum and minimum values**.
    #3. Stores the results (list, max, min) in a file named **`minmax_data.txt`**.
    #4. Reads and prints the saved data from the file.
numbers=input("Enter sequence of numbers : ")
list_numbers=numbers.split()
new_list=[]
for nums in list_numbers:
    nums=int(nums)
    new_list.append(nums)
min_val=new_list[0]
max_val=new_list[0]
for integer in new_list:
    if integer<min_val:
        min_val=integer
    if integer>max_val:
        max_val=integer
print(min_val)
print(max_val)
with open("minmax_data.txt","w") as output_file:
    output_file.write(f"List:{new_list}\n")
    output_file.write(f"Minimum:{min_val}\n")
    output_file.write(f"Maximum:{max_val}\n")
with open("minmax_data.txt","r") as input_file:
    file=input_file.read()
    print(file)