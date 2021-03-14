def build_schedule(activities):

    output_string = [0] * len(activities)
    c_activity_end = -1
    j_activity_end = -1

    for activity in activities:

        start, end, index = activity

        if c_activity_end <= start:
            c_activity_end = end
            index = activity[2]
            output_string[index] = 'C'

        elif j_activity_end <= start:
            j_activity_end = end
            index = activity[2]
            output_string[index] = 'J'

        else:
            output_string = "IMPOSSIBLE"
            break

    return "".join(output_string)

def main():

    test_case_count = int(input())

    for test_case_number in range(0, test_case_count):

        activity_count = int(input())
        activities = []

        for index in range(0, activity_count):

            start, end = input().split(" ")
            activities += [[int(start), int(end), index]]

        # compare the start times of activities with a lower weight to
        # lower end times i.e. sort asc by start time, then subsort equal
        # start times asc by end time
        # Note: I'm unsure if the subsort is entirely neccessary but it
        # does guarantee the correct answer
        comparator = lambda activity : activity[0]+(activity[1]/10000)
        activities.sort(key=comparator)

        output_string = build_schedule(activities)

        print(f'Case #{test_case_number+1}: {output_string}')



if __name__ == "__main__":
    main()
