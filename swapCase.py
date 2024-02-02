def swap_case(s):
    new_s = ""
    for c in s:
        new_s += c.lower() if c.isupper() else c.upper()
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
