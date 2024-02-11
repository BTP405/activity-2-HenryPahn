import matplotlib.pyplot as plt

# this function counts number of integers exists in the range
def count(arr, start, end):
    cnt = 0
    for x in arr:
        if start <= x <= end:
            cnt += 1
    return cnt

def graphSnowfall(t):
    # achieve the data from file
    # open file
    text_file = open(t,'r')
    
    # achieve lines into array
    arr = [int(line) for line in text_file.readlines()]

    # close file
    text_file.close()
    
    x = ["0-10cms", "11-20cms", "21-30cms", "31-40cms", '41-50cms']
    y = [count(arr, 0, 10), count(arr, 11, 20), count(arr, 21, 30), count(arr, 31, 40), count(arr, 41, 50)]

    # barh( x , y ) draws the bars along the vertical axis at the locations specified by x
    plt.barh(x, y)
    
    # add text to the graph
    for index, value in enumerate(y):
        plt.text(value, index, str(value))
        
    # save the graph image 
    plt.savefig("q2.png")

    # show temporary graph image
    plt.show()

graphSnowfall('./q2.txt')