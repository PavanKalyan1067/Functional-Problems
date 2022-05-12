def sum_of_three(arr, target=0):
    result = list()
    arr.sort()

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                result.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
    else:
        print("Don't with the loop")
    return result


if __name__ == '__main__':
    print(sum_of_three([3, 5, -4, 25, 15, 1, -1, 10]))
