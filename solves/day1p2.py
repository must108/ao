
def main():
    with open("input.txt", "r") as f:
        lines = [line.rstrip() for line in f]

    line1 = []
    line2 = []

    for line in lines:
        t, t1 = line.split("   ")
        line1.append(int(t))
        line2.append(int(t1))

    h = {}
    for n in line2:
        if n in h:
            h[n] += 1
        else:
            h[n] = 1

    score = 0
    for n in line1:
        if n in h:
            score += n * h[n]

    print(score)


main()
