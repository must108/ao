
def main():
    with open("input.txt", "r") as f:
        total = 0

        def noIssue(flag, t):
            for i in range(len(t) - 1):
                if flag:
                    if t[i] >= t[i+1] or abs(t[i] - t[i+1]) > 3:
                        return False
                else:
                    if t[i] <= t[i+1] or abs(t[i] - t[i + 1]) > 3:
                        return False
            return True

        def checkIssue(flag, t):
            for i in range(len(t)):
                temp = t[:i] + t[i + 1:]
                new = temp[0] < temp[1] if len(temp) > 1 else flag
                if noIssue(new, temp):
                    return True
            return False

        for level in f:
            split = level.strip().split()

            t = [int(num) for num in split]

            flag = t[0] < t[1]

            if noIssue(flag, t) or checkIssue(flag, t):
                total += 1

        print(total)


main()
