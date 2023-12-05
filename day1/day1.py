def find_alpha_digits(string):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for n, digit in enumerate(digits):
        i = 0
        while i < len(string) and i < len(digit) and string[i] == digit[i]:
            i += 1
        if (i == len(digit)):
            return str(n + 1)
    return 0

def main():
    total = 0
    with open("input_day1") as f:
        lines = f.read().split()

    for line in lines:
        index = 0
        while index < len(line):
            first_digit = line[index]
            if first_digit in "0123456789":
                break
            first_digit = find_alpha_digits(line[index:])
            if (first_digit != 0):
                break
            index += 1

        index = len(line) - 1
        while index >= 0:
            last_digit = line[index]
            if last_digit in "0123456789":
                break
            last_digit = find_alpha_digits(line[index:])
            if (last_digit != 0):
                break
            index -= 1
        
        print(str(first_digit) + str(last_digit))
        total += int(first_digit + last_digit)

    print("result: " + str(total))

if __name__ == "__main__":
    main()