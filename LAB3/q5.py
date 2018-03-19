#Converts binary to decimal 

def bin_to_dec(string):
    decimal = 0
    multiplier = 1

    for c in reversed(string):
        decimal += multiplier * int(c)
        multiplier *= 2

    print("Decimal output:", decimal)


bin_to_dec("00111100")