def check_rows(lines, ele_cnt):

    line_ptr = 0
    row_repetitions = 0
    row_ptr = line_ptr

    # for each row
    for i in range(0, ele_cnt):

        row = [0] * ele_cnt
        row_ptr = line_ptr + ele_cnt * i

        # check the row for any repeated element
        for _ in range(0, ele_cnt):

            element = int(lines[row_ptr])
            index = element - 1
            row[index] = row[index] + 1

            if row[index] > 1:
                row_repetitions = row_repetitions + 1
                break

            row_ptr = row_ptr + 1

    return row_repetitions


def check_cols(lines, ele_cnt):

    line_ptr = 0
    col_repetitions = 0
    col_ptr = line_ptr

    # for each column
    for i in range(0, ele_cnt):

        col = [0] * ele_cnt
        col_ptr = line_ptr + i

        # check the column for any repeated element
        for _ in range(0, ele_cnt):

            element = int(lines[col_ptr])
            index = element - 1
            col[index] = col[index] + 1

            if col[index] > 1:
                col_repetitions = col_repetitions + 1
                break

            col_ptr = col_ptr + ele_cnt

    return col_repetitions


def calculate_trace(lines, ele_cnt):

    trace = 0
    line_ptr = 0

    # for each element of the diagonal
    for _ in range(0, ele_cnt):

        trace = trace + int(lines[line_ptr])
        line_ptr = line_ptr + ele_cnt + 1

    return trace


def main():

    test_case_count = int(input())
    test_case_number = 1

    # for each test case read test case
    while test_case_number <= test_case_count:

        # Get the first line of the test case, which contains the number
        # of elements
        ele_cnt = int(input())
        lines = []

        for _ in range(0,ele_cnt):

            inp = input().split(" ")
            lines = lines + inp

        trace = calculate_trace(lines, ele_cnt)

        # number of rows with a repeated element
        rows_with_rep = check_rows(lines, ele_cnt)

        # number of cols with a repeated element
        cols_with_rep = check_cols(lines, ele_cnt)

        # print formatted output
        print(f"Case #{test_case_number}: {trace} {rows_with_rep} "
            f"{cols_with_rep}")

        test_case_number += 1


if __name__ == "__main__":
    main()
