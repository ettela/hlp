def print_char(char1, char2, number):
    for i in range(ord(char1), ord(char2) + 1, number):
        end = min(i + number, ord(char2) + 1)
        print(*(f"{chr(j):4}" for j in range(i, end)))


if __name__ == "__main__":
    print_char("A", "Z", 5)
    print()  # Print a new line
    print_char("!", "9", 10)
