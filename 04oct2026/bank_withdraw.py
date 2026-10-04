amount=20000
withdrawl_amount=input("enter the amount:")
if len(withdrawl_amount)<=amount and amount%500==0:
    print("transaction is allwoed")
else:
    print("transactin is not allos")