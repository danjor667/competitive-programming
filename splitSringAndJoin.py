def split_and_join(line):
    string_list = line.split(" ")
    return ("-".join(string_list))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
