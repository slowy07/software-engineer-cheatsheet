def reverse(arr):
    new_arr = []
    for index in range(len(arr)):
        new_arr.insert(0, arr[index])

    return new_arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(arr)
    print(f"reverse: {reverse(arr)}")
