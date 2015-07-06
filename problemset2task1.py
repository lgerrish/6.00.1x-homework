balance = 4842
annual_interest_rate = 0.2
monthly_payment_rate =0.04
monthly_interest_rate = annual_interest_rate / 12
monthly_payment = monthly_payment_rate * balance
new_balance= (balance - monthly_payment) * (1 + monthly_interest_rate)

total=0
for month in range(1, 13):
    monthly_payment = monthly_payment_rate * balance
    balance = (balance - monthly_payment) * (1 + monthly_interest_rate)

    total=total+ monthly_payment
    print('Month: %d \n Minimum monthly payment: %g \n Remaining balance: %g'\
          % (month, round(monthly_payment, 2), round(balance,2)))
print "Total paid: " + str(round(total,2))
print "Remaining balance: " +str(round(balance,2))