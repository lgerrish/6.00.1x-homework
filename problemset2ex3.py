#      Test Case 1:
balance = 999999
annualInterestRate = 0.18

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12.0
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0


# We will look at the high bound and low bound to figure out
# what the right interest payment is. We will try in the middle each time
# recursively. We will calculate the balance left for each try. If there
# is a balance left, try paying more. Else, try paying less.
def calcSmallestPayment(balance, intRate, lowBound, highBound):
  if (highBound - lowBound) < 0.01:
  	#Round it to two decimal points
  	return round(lowBound, 2)
  # We don't have the answer, try the middle
  paymentTry = (lowBound + highBound) / 2.0
  # have intRate
  balanceLeft = balanceRemaining(intRate, balance, paymentTry)
  if (balanceLeft > 0):
    # We had money we didn't pay. We need to try higher
    return calcSmallestPayment(balance, intRate, paymentTry, highBound)
  else:
    # We paid it all off. Try lower
    return calcSmallestPayment(balance, intRate, lowBound, paymentTry)

# Calculates balance remaining. We want it to be less than zero
def balanceRemaining(monthly_interest_rate, balance, monthly_payment ):
  new_balance= (balance - monthly_payment) * (1.0 + monthly_interest_rate)

  total=0.0
  for month in range(12):
      # monthly_payment = monthly_payment_rate * balance
      balance = (balance - monthly_payment) * (1.0 + monthly_interest_rate)

      total=total+ monthly_payment
  return balance

monthlyInterestRate  = annualInterestRate / 12.0
monthlyPaymentLowerBound = balance / 12.0
monthlyPaymentUpperBound = (balance * (1.0 + monthlyInterestRate) * 12.0) / 12.0

smallestMonthlyPayment = calcSmallestPayment(balance, monthlyInterestRate, monthlyPaymentLowerBound, monthlyPaymentUpperBound)
print "Lowest Payment: " + str(smallestMonthlyPayment)