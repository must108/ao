import re


def main():
    with open("input.txt", "r") as f:
        block = f.read()
        pattern = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"

        ins = re.findall(pattern, block)

        total, enable = 0, True

        for i in ins:
            if i == "do()":
                enable = True
            elif i == "don't()":
                enable = False
            elif i.startswith("mul(") and enable:
                nums = list(map(int, re.findall(r'\d+', i)))
                total += nums[0] * nums[1]

        print(total)


main()
