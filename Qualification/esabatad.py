import sys

def complement(arr):

    arr_len = len(arr)

    for i in range(0,arr_len):

        if arr[i] == '0':
            arr[i] = '1'
        elif arr[i] == '1':
            arr[i] = '0'


def reverse(arr):

    arr_len = len(arr)
    index = 0
    swap_index = arr_len - 1

    while swap_index > index:

        temp = arr[index]
        arr[index] = arr[swap_index]
        arr[swap_index] = temp
        swap_index -= 1
        index += 1


def query(index):

    # Since the input array is in range 1 to B, output index+1
    print(f'{index+1}', flush=True)
    return input()


def mutate_arr(arr, same, dif):

    if same != -1 and dif != -1:

        same_2 = query(same)
        dif_2 = query(dif)

        if same_2 != arr[same] and dif_2 == arr[dif]:

            complement(arr)
            reverse(arr)

        elif same_2 == arr[same] and dif_2 != arr[dif]:
            reverse(arr)
        elif same_2 != arr[same] and dif_2 != arr[dif]:
            complement(arr)

    elif same != -1:

        same_2 = query(same)

        if same_2 != arr[same]:
            complement(arr)

        # Do this so that the query count will be 10 after 8 more queries
        query(same)

    elif dif != -1:
        # print("detected case 2: different")

        dif_2 = query(dif)

        if dif_2 != arr[dif]:
            complement(arr)

        # Do this so that the query count will be 10 after 8 more queries
        query(dif)


def main():

    inp = input().split(" ")
    test_case_count = int(inp[0])
    arr_len = int(inp[1])

    for _ in range(0, test_case_count):

        arr = [-1] * arr_len
        first = 0
        last = arr_len - 1
        same = -1
        dif = -1
        read_count = 0

        while first < last:

            if read_count == 150:
                sys.exit(-1)

            if read_count % 10 == 0 and read_count:

                mutate_arr(arr, same, dif)
                read_count += 2

            else:

                arr[first] = query(first)
                arr[last] = query(last)

                if arr[first] == arr[last] and same < 0:
                    same = first
                elif arr[first] != arr[last] and dif < 0:
                    dif = first

                first += 1
                last -= 1
                read_count += 2

        print("".join(arr))
        result = input()

        if result != 'Y':
            sys.exit(-1)


if __name__ == "__main__":
    main()
