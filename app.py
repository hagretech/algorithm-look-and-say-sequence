# look and say sequence 


# this fuction will recv a number and return the next sequence 
def next_seq(number):
    result = []
    i = 0
    while i < len(number):
        counter = 1
        while i + 1 < len(number) and number[i] == number[i + 1]:
            i += 1
            counter +=1
        result.append(str(counter))
        result.append(number[i])
        i += 1
    return ''.join(result)


def counterer(no):
    next = no
    for i in range(100):
        next = next_seq(next)
        print(next)

counterer('1')