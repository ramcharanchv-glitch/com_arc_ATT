
def to_binary(num, bits):
    return format(num & ((1 << bits) - 1), '0{}b'.format(bits))


def signed_value(binary, bits):
    value = int(binary, 2)
    if value >= (1 << (bits - 1)):
        value -= (1 << bits)
    return value


def binary_subtraction(a, b):
    bits = 16

    # Convert operands into 16-bit 2's complement
    A = a & 0xFFFF
    B = b & 0xFFFF

    # Subtraction: A - B = A + 2's complement of B
    result = (A + ((~B + 1) & 0xFFFF)) & 0xFFFF

    # Check signed overflow
    decimal_result = signed_value(to_binary(result, bits), bits)
    overflow = not (-32768 <= a - b <= 32767)

    print("\nOperands (8-bit 2's complement):")
    print("A =", to_binary(a, 8))
    print("B =", to_binary(b, 8))

    print("\nOperands (16-bit 2's complement):")
    print("A =", to_binary(a, 16))
    print("B =", to_binary(b, 16))

    print("\nBinary subtraction:")
    print("A - B =", to_binary(result, 16))

    print("Decimal result =", decimal_result)
    print("Overflow =", overflow)


# Given expressions
print("Expression (a): 35 - (+29)")
binary_subtraction(35, 29)

print("\n-----------------------------")

print("Expression (b): (-35) - (-12)")
binary_subtraction(-35, -12)
