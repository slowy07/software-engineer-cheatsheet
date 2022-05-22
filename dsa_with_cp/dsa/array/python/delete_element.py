def delete(arr, element):
    if element not in arr:
        return "no element"

    new_arr = []

    for index in range(len(arr)):
        if arr[index] != element:
            new_arr.append(arr[index])

    return new_arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    element = 5
    print(arr)
    new_arr = delete(arr, element)
    print(arr)
