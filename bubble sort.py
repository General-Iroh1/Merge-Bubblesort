def bubble_sort(list):
    lengthoflist = len(list)

    for item in range(lengthoflist-1):
        for number in range(lengthoflist-1):
            if list[number] > list[number+1]:
                #number+1 is the next number in the list.
                tmp = list[number]
                list[number] = list[number+1]
                list[number+1] = tmp

    return list

def main():
    list = [1,8,6,5,5,3,2,1]
    bubble_sort(list)
    print(list)


main()
