# This is from the second section of the lab
# This implementation uses binary numbers for each of the options (where yes = 1, no = 0) for the 8 questions (8 bits)
# The result is a number between 0 and 256
def to_treatment():
    zero = input("Did you use extra nitrogen-based fertiliser? (y/n)")
    one = input("Did you use extra phosphate-based fertiliser? (y/n)")
    two = input("Did you allow early flooding of the field? (y/n)")
    three = input("Was the field left fallow (empty) the previous season? (y/n)")
    four = input("Did you harvest early? (y/n)")
    five = input("Did you drain the field before harvest? (y/n)")
    six = input("Were the grains dried in the sun before delivery? (y/n)")
    seven = input("Did you use the more expensive new variety? (y/n)")

    inputs = [zero, one, two, three, four, five, six, seven]
    outputs = []

    for c in inputs:
        if c is 'y':
            outputs.append("1")
        else:
            outputs.append("0")
    
    dec_output = bin_to_dec(outputs)
    print(dec_output)

# From q5 - to convert from a binary to decimal
def bin_to_dec(string):
    decimal = 0
    multiplier = 1

    for c in reversed(string):
        decimal += multiplier * int(c)
        multiplier *= 2

    return decimal

to_treatment()