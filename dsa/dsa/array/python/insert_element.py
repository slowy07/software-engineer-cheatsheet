def insert(arr, index, successor):
    for index in range(index, len(arr)):
        arr[index], successor = successor, arr[index]

    arr.append(successor)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    print(arr)
    insert(arr, 4, 5)
    print(arr)
