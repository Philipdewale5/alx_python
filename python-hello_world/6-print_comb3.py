for x in range(10):
    for y in range(x + 1, 10):
        print(f"{:02}, {:02}".format(x ,y), end="")
        if x != 8 or y != 9:
            print(", ", end="")
        else:
            print()
