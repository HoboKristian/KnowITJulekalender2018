def test(a, r):
    tmp = sum([int(c)*d for c,d in zip(a,r)]) % 11
    if tmp == 0:
        return 0
    return 11 - tmp

def main():
    numbers = open("./input-fnr.txt").read().strip().split("\n")
    range1 = [3,7,6,1,8,9,4,5,2]
    range2 = [5,4,3,2,7,6,5,4,3,2]

    valid_date = [num for num in numbers if int(num[:2]) <= 31 and num[2:4] == "08"]
    valid_female = [num for num in valid_date if not int(num[8]) % 2]
    valid_k1 = [num for num in valid_female if str(test(num[:9], range1)) == num[9]]
    valid_k2 = [num for num in valid_k1 if str(test(num[:10], range2)) == num[10]]
    print(len(valid_k2))

if __name__ == "__main__":
    main()
