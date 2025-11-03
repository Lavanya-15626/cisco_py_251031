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
    