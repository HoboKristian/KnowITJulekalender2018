from sympy.ntheory.primetest import isprime

def all_palindromes(text):
    best = 0
    text_length = len(text)
    for idx, char in enumerate(text):
        print(idx, best)
        # Check for longest odd palindrome(s)
        start, end = idx - 1, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            pali_sum = sum(text[start:end+1])
            if pali_sum > best:
                if isprime(pali_sum):
                    best = pali_sum
            start -= 1
            end += 1

        # Check for longest even palindrome(s)
        start, end = idx, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            pali_sum = sum(text[start:end+1])
            if pali_sum > best:
                if isprime(pali_sum):
                    best = pali_sum
            start -= 1
            end += 1

    return best

def main():
    txt = open("./input-palindrom.txt").read()
    txt = txt.replace(",", "")
    nums = [int(n) for n in txt]
    print(all_palindromes(nums))

if __name__ == "__main__":
    main()
