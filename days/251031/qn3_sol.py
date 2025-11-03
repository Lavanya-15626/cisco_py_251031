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