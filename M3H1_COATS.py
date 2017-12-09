# Brandon Coats
# CTI-110
# M3H1-Age Classifer
# 9/19/17

# Input Age
personAge = int( input('Please enter your age: '))

# Output
if personAge <= 1:
    print( 'You are an Infant' )
elif personAge < 13:
    print( 'You are a Child' )
elif personAge < 20:
    print( 'You are a Teenager' )
elif personAge >= 20:
    print( 'You are an Adult' )
