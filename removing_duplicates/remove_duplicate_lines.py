filename = inventory_export.txt
with open(filename) as fold:
    #Creating a backup copy of the CSV file before writing a new copy of it.
    for temp_line in fold:
        #Replacing the # in the temp_line with noting.
        temp_line = temp_line.replace('#', "")
        #Making a split at the | character.
        temp_line = temp_line.split("|")
        #Checking to see if the length of the temp_line is equal to 10.
        if len(temp_line) == 10:
            #If the value at index 0 is first_name, then all we are doing is assigning it a value.
            if temp_line[0] == "itemname":
                #Creating a formatted line
                line = f"{temp_line[0]}, {temp_line[1]}, {temp_line[2]}, {temp_line[3]}, {temp_line[4]}, {temp_line[5]}, {temp_line[6]}\n"
            #Else, we will append all other values to a list.
            else:
                #Creating a formatted line
                line = f"\"{temp_line[0]}\", \"{temp_line[1]}\", \"{temp_line[2]}\", \"{temp_line[3]}\", \"{temp_line[4]}\", \"{temp_line[5]}\", \"{temp_line[6]}\"\n"
                #Appending each line to a list.
                output_content.append(line)
        #Else, if the length of the temp_line is not equal to 10.
        else:
            #Checking to see if the first line is first_name.
            if temp_line[0] == "itemname":
                #Creating a formatted line.
                line = f"{temp_line[0]}, {temp_line[1]}, {temp_line[2]}, {temp_line[3]}, {temp_line[4]}, {temp_line[5]}, {temp_line[6]}\n"
            else:
                #Creating a formatted line.
                line = f"\"{temp_line[0]}\", \"{temp_line[1]}\", \"{temp_line[2]}\", \"{temp_line[3]}\", \"{temp_line[4]}\", \"{temp_line[5]}\", \"{temp_line[6]}\"\n"
        ####BEGIN REMOVAL OF DUPLICATE LINES####
        #Setting a flag
        matched_word = False
        #Looping through every entry in my_nondup_lines
        for my_line in my_nondup_lines:
            #Checking for the address
            if temp_line[0] in my_line:
                #Printing a message so that I am telling the user that I am deleting the inventory with a specified address value.
                print(f"removing a duplicate line with item name: {temp_line[0]}")
                #Setting our flag to true.
                matched_word = True
                #Breaking out of the loop
                break
        #Checking to see if the matched word is true.
        if not matched_word:
            #Appending each line to the list.
            my_nondup_lines.append(line)
    #Opening the file for writing/creating if it does not exist.
    with open("text_files/inventory.csv","w+") as fawn:
        #Going through each line in the list.
        for line in my_nondup_lines:
            #Writing each line to the file.
            fawn.write(line)             
