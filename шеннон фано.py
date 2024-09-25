def fano(array, left, right):
    if left == right:
        return

    border = delit(array, left, right)

    for i in range(left, border + 1):
        array[i][2] += "1"
    for i in range(border + 1, right + 1):
        array[i][2] += "0"

    fano(array, left, border)
    fano(array, border + 1, right)


def delit(array, left, right):
    sum_left = array[left][1]
    sum_right = array[right][1]
    while left < right:
        if sum_right <= sum_left:
            right -= 1
            sum_right += array[right][1]
        else:
            left += 1
            sum_left += array[left][1]
    return right 


if __name__ == "__main__":
    array = [["a", 3, ""], ["b", 3, ""], ["c", 3, ""], ["d", 3, ""]]
    fano(array, 0, len(array) - 1)
    print(array)
