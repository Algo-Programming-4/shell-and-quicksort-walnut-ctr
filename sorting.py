def bubble(ary):
    """sorts an array with bubble sort"""
    sorted = False
    times = len(ary)
    while sorted == False:
        sorted = True
        times -= 1
        for i in range(times):
            if ary[i] > ary[i+1]:
                sorted = False
                checking = 0
                while not(not(i+checking < times) and ary[i] > ary[i + checking]):
                    checking += 1
                    print("i",i)
                    print("check",checking)
                    print("times",times)
            swap = ary[i]
            ary[i] = ary[i + checking]
            ary[i + checking]= swap
            print(ary)
    return ary


def selection(ary):
    for i in range(len(ary)):
        min = i
        for j in range(len(ary[i:])):
            if ary[j+i] < ary[min]:
                min = j+i
        swap = ary[i] 
        ary[i] = ary[min]
        ary[min] = swap
    return ary


def insertion(ary):
    for i in range(len(ary)):
        j = i
        while j > 0 and ary[j-1] > ary[j]:
            ary[j-1],ary[j] = ary[j], ary[j-1]
            j -= 1
    return ary


def partition(numbers, start_index, end_index):
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]
    low = start_index
    high = end_index
   
    done = False
    while not done:
        while numbers[low] < pivot:
            low = low + 1
      
        while pivot < numbers[high]:
            high = high - 1
        if low >= high:
            done = True
        else:
            temp = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp
            low = low + 1
            high = high - 1
    return high

def quicksort(numbers, start_index, end_index):
    if end_index <= start_index:
        return
    high = partition(numbers, start_index, end_index)
    quicksort(numbers, start_index, high)
    quicksort(numbers, high + 1, end_index)


def interlev(ary,start,gap):
    for i in range(start + gap, len(ary),gap):
        j = i
        while (j - gap >= start) and (ary[j] < ary[j-gap]):
            ary[j-1],ary[j] = ary[j], ary[j-1]
            j -= gap      

def shell(ary ,gaps):
    for gap in gaps:
        for i in range(gap):
            interlev(ary,i,gap)
    return ary

def main():
    easy_test = [9,8,7,6,5,4,3,2,1]
    test_ary = [6,3,2,5,4,7,6,5,7,7,6,5,5,5,5555,4,4,34,3]
    print(shell(easy_test,[4,2,1]))


if __name__ == "__main__":
    main()
            
