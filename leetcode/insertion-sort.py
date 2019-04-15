# Insertion Sort (not from LeetCode)


def insertion_sort(numbers: list) -> list:
    sorted_list = []
    for number in numbers:
        not_inserted = True
        i, n = 0, len(sorted_list)
        while i < n and number >= sorted_list[i]:
            i += 1
        sorted_list.insert(i, number)
    return sorted_list


if __name__ == '__main__':
    xs = insertion_sort([3, 1, 2, 5, -1])
    print(xs)