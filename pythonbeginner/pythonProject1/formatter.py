def arithmetic_arranger(problems, solver=False):
    # Principal Variables

    first_number = ""
    operator = ""
    second_number = ""
    lines = ""
    solution = ""

    # First Check after the FOR loop

    if len(problems) > 5:
        return "Error: Too many problems."

    # Core FOR Loop

    for problem in problems:
        problem_array = problem.split()
        first_number = problem_array[0]
        operator = problem_array[1]
        second_number = problem_array[2]

        # Checks for the items before the split

        if first_number.isdigit() and second_number.isdigit():
            if len(first_number) > 4 < len(second_number):
                return "Error: Numbers cannot be more than four digits"
        else:
            return "Error: Numbers must only contain digits."

        if operator == "+":
            solution == int(first_number) + int(second_number)
        elif operator == "-":
            solution == int(first_number) - int(second_number)
        else:
            return "Error: Operator must be '+' or '-'."

        # Distance comprobation

        distance = max(len(first_number), len(second_number)) + 2

        # Items Padding

        top_item = str(first_number.rjust(distance)) + "    "
        bottom_item = str(operator.ljust(distance)) + " " + str(second_number.rjust(distance)) + " "
        lines = ""
        solution_item = str(solution.rjust(distance))
        for line in range(distance):
            lines += "-"

    if solver == True:
        operations = top_item + "/n" + bottom_item + "/n" + lines + "/n" + solution_item
    else:
        operations = top_item + "/n" + bottom_item + "/n" + lines

    return operations


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))