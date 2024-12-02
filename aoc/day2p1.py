
def main():
    with open("input.txt", "r") as f:
        total = 0

        for level in f:
            split = level.split(" ")
            t = []
            for num in split:
                t.append(int(num))

            n = len(t)
            flag = False
            check = True

            if t[0] < t[1]:
                flag = True

            for i in range(n-1):
                if flag:
                    if t[i] >= t[i+1] or abs(t[i] - t[i+1]) > 3:
                        check = False
                        break
                else:
                    if t[i] <= t[i+1] or abs(t[i] - t[i+1]) > 3:
                        check = False
                        break

            if check:
                total += 1

        print(total)


main()
