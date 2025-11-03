#   Write a Python program that:

    #1. Reads a line of integers from the user (separated by spaces).
    #2. Stores them in a **list** and calculates the **sum and average**.
    #3. Saves the list, sum, and average into a text file named **`numbers_data.txt`**.
    #4. Reads the contents of the file and prints them back to the user.
integers_seq=input("integers(separated by space): ")
print(integers_seq)
integers=integers_seq.split()
print(type(integers))
summ=0
for i in integers:
    summ=summ+int(i)
print(summ)
average=summ/len(integers)
print(average)
with open("qn02_data.txt","w") as output_file:
   output_file.write(f"list:{integers}\n")
   output_file.write(f"summ:{summ}\n")
   output_file.write(f"average:{average}\n")

#output_file.close()
with open("qn02_data.txt","r") as input_file:
   file = input_file.read()
   print(file)
