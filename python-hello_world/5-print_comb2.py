output = ""
for x in range(100):
    if x < 10:
        output += "0{}, ".format(x)
    else:
        if x == 99:
            output += "{}\n".format(x)
        else:
            output += "{}, ".format(x)

print(output, end="")

