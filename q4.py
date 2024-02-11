def printStatsDecorator(func):
    def wrapper(numbers):
        print("Numbers read: ", numbers)
        print("The count of the number read: ", len(numbers))
        print("Average: ", sum(numbers) / len(numbers))
        print("Maximum: ", max(numbers))
    return wrapper

def printStats(t):
    text_file = open(t, 'r')

    for line in text_file: 
        # extract and convert numbers into an array of ints
        numbers = list(map(int, line.split())) 

        # this function is decorated to print the statistics
        @printStatsDecorator
        def passLines(numbers): 
            pass 

        # pass the array to decorator function
        passLines(numbers)

    text_file.close()

printStats('q4.txt')