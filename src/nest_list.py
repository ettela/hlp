def nest_list(n):
    if n == 0:
        return []
    else:
        return [nest_list(n - 1)]


foo = nest_list


def main():

    # nest_list = lambda n: [] if n == 0 else [nest_list(n - 1)]

    print(nest_list(int(input())))


if __name__ == "__main__":
    main()
