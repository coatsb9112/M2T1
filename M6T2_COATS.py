# Brandon Coats
# CTI 110
# M6T2_FeetToInches
# Solves feet to inches.

INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter a number of feet: '))

    print(feet,'equals', feet_to_inches(feet), 'inches.')

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()

