def wordCount(t):
    # open the file in read mode
    text_file = open(t,'r')

    # create an empty dictionary
    dictionary = dict()

    # the current line number 
    curr_line = 1
    for line in text_file: 
        # remove the leading spaces and newline character. then conver the characters in line to lowercase
        line = line.strip().lower()

        # split the line into words
        words = line.split(" ") 

        # Iterate over each word in line 
        for word in words: 
            # Check if the word is already in dictionary 
            if word in dictionary: 
                # Add another line 
                dictionary[word].append(curr_line)
            else: 
                # Record the line that the word exists
                dictionary[word] = [curr_line]
        curr_line += 1

    # close file
    text_file.close()

    # display dictionary
    for key in list(dictionary.keys()): 
        print(key, ":", dictionary[key])   
    
wordCount('q3.txt')


  