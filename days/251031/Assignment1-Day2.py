 
# Problem 3
#Write a Python program that:

   #1. Accepts a sentence from the user.
    #2. Splits the sentence into words and stores them in a **list**.
    #3. Converts all words to **uppercase** and stores them in a **tuple**.
    #4. Saves both the list and tuple into a file named **`sentence_data.txt`**.
    #5. Reads back the data from the file and displays it on the screen.
sentence=input(" Enter the sentence : ")
req_list=sentence.split()
new_list=[]
for word in req_list:
    new_word=word.upper()
    new_list.append(new_word)
req_tuple=tuple(new_list)   
print(req_list,type(req_list))
print(req_tuple,type(req_tuple))
with open("sentence_data.txt","w") as output_file:
    output_file.write(f"List:{req_list}\n")
    output_file.write(f'Tuple:{req_tuple}\n')
with open("sentence_data.txt","r") as input_file:
    file=input_file.read()
    print(file)

### Problem 4

#Write a Python program that:

    #1. Reads a list of names from the user (separated by spaces).
    #2. Sorts the names alphabetically and stores them in a list.
    #3. Converts the list into a tuple.
    #4. Saves the sorted list and tuple into a file named **`names_data.txt`**.
    #5. Reads and prints the saved data from the file.
names=input("Enter the list of names(seperated by spaces) : ")
new_names=names.split()
List_of_names=[]
for names in new_names:
    names=names.capitalize()
    List_of_names.append(names)
List_of_names.sort()
Tuple_of_names=tuple(List_of_names)
print(List_of_names)
print(Tuple_of_names)
with open("names_data.txt","w") as output_file:
    output_file.write(f"List:{List_of_names}\n")
    output_file.write(f"Tuple:{Tuple_of_names}\n")
with open("names_data.txt","r") as input_file:
    file=input_file.read()
    print(file)



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
    