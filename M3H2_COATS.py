# CTI-110
# Brandon Coats
# M3HW2
# 9/19/17

#input

purchaseQuantity = int( input( 'Please enter # of software packages: ' ))

packagePrice = 99

#output

if purchaseQuantity < 10:
    discount = 0.00;
elif purchaseQuantity < 20:
    discount = 0.10
elif purchaseQuantity < 50:
    discount = 0.20
elif purchaseQuantity < 100:
    discount = 0.30
else:
    discount = 0.40

subTotal = purchaseQuantity * packagePrice
discountAmount = discount * subTotal
finalTotal = subTotal - discountAmount


print( "Amount of discount: $" + format( discountAmount, ",.2f" ) + "Total amount: $" + format( finalTotal, ",.2f" ) )
