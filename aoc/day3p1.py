import re


def main():
    with open("input.txt", "r") as f:
        block = f.read()
        pattern = r"mul\(\d+,\d+\)"

        matches = re.findall(pattern, block)

        prod = 0
        for match in matches:
            t = 1
            nums = re.findall(r'\d+', match)
            for num in nums:
                t *= int(num)
            prod += t

        print(prod)


main()
