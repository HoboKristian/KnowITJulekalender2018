def test(a, r):
    tmp = sum([int(c)*d for c,d in zip(a,r)]) % 11
    if tmp == 0:
        return 0
    return 11 - tmp

def main():
    numbers = open("./input-fnr.txt").read().strip().split("\n")
    range1 = [3,7,6,1,8,9,4,5,2]
    range2 = [5,4,3,2,7,6,5,4,3,2]

    count = 0
    valid_date = filter(lambda num: int(num[:2]) <= 31 and num[2:4] == "08", numbers)
    valid_female = filter(lambda num: int(num[8]) % 2 == 0, valid_date)
    for num in valid_female:
        k1 = test(num[:9], range1)
        if k1 == 10 or str(k1) != num[9]:
            continue
        k2 = test(num[:9]+str(k1), range2)
        if k2 == 10 or str(k2) != num[10]:
            continue
        count += 1
        print(num)
    print(count)

if __name__ == "__main__":
    main()
