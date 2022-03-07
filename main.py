def read_file(filename: str):
    with open(filename + ".txt") as f:
        line = f.read()
        nums = [int(x) for x in line.split(',')]
    return nums


def write_file(filename: str, data: list):
    with open(filename + ".txt", 'w') as file_object:
        file_object.write(data.__str__())


def main():
    nums_input = read_file("input")
    nums_output = list()
    nums_recurring = list()
    for num in nums_input:
        if num in nums_output:
            nums_output.remove(num)
            nums_recurring.append(num)
        elif num not in nums_recurring:
            nums_output += [num]
    write_file("output", nums_output)


if __name__ == '__main__':
    main()
