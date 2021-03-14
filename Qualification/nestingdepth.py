def build_nested_string(input_string):

    output_string = []
    input_len = len(input_string)
    depth = 0

    for i in range(0, input_len):

        ele = int(input_string[i])
        dif = ele - depth

        if dif < 0:
            # add abs(dif) closed par
            output_string.append(")" * abs(dif))

        elif dif > 0:
            # add diff open parethesis
            output_string.append("(" * dif)

        output_string.append(input_string[i])
        depth = ele

    if depth > 0:
        # add depth closed par
        output_string.append(")" * depth)

    return "".join(output_string)

def main():

    # number of test cases
    test_case_count = int(input())

    for test_case_number in range(0, test_case_count):

        input_string = input()
        output_string = build_nested_string(input_string)

        print(f'Case #{test_case_number + 1}: {output_string}')


if __name__ == "__main__":
    main()
