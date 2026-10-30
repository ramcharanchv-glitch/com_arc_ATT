
# Function for Rotate Left without Carry (ROL)
def ROL(num, positions):
    print("\n--- Rotate Left without Carry (ROL) ---")
    print("Original number:", format(num, '08b'))

    for i in range(positions):
        msb = (num >> 7) & 1
        num = ((num << 1) | msb) & 0xFF

        print("After rotation", i + 1, ":", format(num, '08b'))

    print("Final ROL result:", format(num, '08b'))


# Function for Rotate Left with Carry (RCL)
def RCL(num, carry, positions):
    print("\n--- Rotate Left with Carry (RCL) ---")
    print("Original number:", format(num, '08b'))
    print("Initial Carry:", carry)

    for i in range(positions):
        msb = (num >> 7) & 1
        num = ((num << 1) | carry) & 0xFF
        carry = msb

        print("After rotation", i + 1, ":",
              format(num, '08b'), "Carry:", carry)

    print("Final RCL result:", format(num, '08b'))
    print("Final Carry:", carry)


# Main program
ROL(0b11110110, 2)

RCL(0b10000110, 0, 2)
