def search(arr, element):
    for index in range(0, len(arr)):
        if arr[index] == element:
            return index

    return -1


if __name__ == "__main__":
    arr = [20, 5, 7, 25]
    element = 5

    print(search(arr, element))
