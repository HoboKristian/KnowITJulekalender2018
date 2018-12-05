import itertools

def remove_n(option):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]

    out_numbers = []
    out_options = []
    for o, curr in zip(option, numbers):
        if o == "n":
            old = out_numbers[-1]
            out_numbers[-1] = old * 10 + curr
        else:
            out_numbers.append(curr)
            out_options.append(o)
    return zip(out_options, out_numbers)


def convert(option):
    s = 0
    option = list(option)
    option.insert(0, "a")
    for o, n in remove_n(option):
        if o == "a":
            s += n
        elif o == "s":
            s -= n
    return s


def main():
    possibilities = itertools.product("asn", repeat=14)
    print(sum(map(lambda x: x == 42,
                    map(convert, possibilities))))

main()
