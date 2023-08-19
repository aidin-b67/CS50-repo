#Informing of customer how much they need to pay
amount_due = 50


while amount_due > 0:
# print the amount due
    print("Amount due: ", amount_due)

#ask customer to insert coin
    insert_coin = int(input ("insert coin: "))

#create loop for amount due and change owed
    if insert_coin in [25, 10, 5]:
        amount_due -= insert_coin

change_owed = abs(amount_due)
print("Change Owed: ",change_owed)