
def main():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    line1 = []
    line2 = []
    for line in lines:
        t, t1 = line.split("   ")
        line1.append(int(t))
        line2.append(int(t1))

    line1.sort()
    line2.sort()

    total = 0
    for i in range(0, len(line1)):
        total += abs(line1[i] - line2[i])

    print(total)


main()
