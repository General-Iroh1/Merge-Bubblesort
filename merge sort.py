def merge_sort(list):
    length = len(list)

    if length == 1:
        return list

    partition = length // 2

    partition1 = merge_sort(list[:partition])
    partition2 = merge_sort(list[partition:])

    return merge(partition1, partition2)


def merge(partition1, partition2):
    finalresult = []
    partitionitem1 = partitionitem2 = 0

    while partitionitem1 < len(partition1) and partitionitem2    < len(partition2):
        if partition1[partitionitem1] < partition2[partitionitem2]:
            finalresult.append(partition1[partitionitem2])
            partitionitem1 += 1
        else:
            finalresult.append(partition2[partitionitem2])
            partitionitem2 += 1

    finalresult.extend(partition1[partitionitem1:])
    finalresult.extend(partition2[partitionitem2:])

    return finalresult


def main():
    unsorted = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    sorted = merge_sort(unsorted)
    print(sorted)
main()