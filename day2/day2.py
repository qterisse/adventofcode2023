def part1():
    with open("day2_input") as f:
        lines = f.read()
    limits = {
        "red": 12, 
        "green": 13,
        "blue": 14
    }
    
    total = 0
    for n, line in enumerate(lines.split("\n")):
        valid = True
        for section in line.split(":")[-1].split(";"):
            for color_cubes in section.split(","):
                if int(color_cubes.strip().split(" ")[0]) > limits[color_cubes.strip().split(" ")[-1]]:
                    valid = False
        if valid:
            total += n + 1

    print("result: " + str(total))
    return total

def part2():
    with open("day2_input") as f:
        lines = f.read()

    total = 0
    for n, line in enumerate(lines.split("\n")):
        min_values = {"red": 0, "blue": 0, "green": 0}
        for section in line.split(":")[-1].split(";"):
            for color_cubes in section.split(","):
                if int(color_cubes.strip().split(" ")[0]) > min_values[color_cubes.strip().split(" ")[-1]]:
                    min_values[color_cubes.strip().split(" ")[-1]] = int(color_cubes.strip().split(" ")[0])
        total += min_values['red'] * min_values['green'] * min_values['blue']

    print("result: " + str(total))
    return total

def main():
    part2()

if __name__ == "__main__":
    main()