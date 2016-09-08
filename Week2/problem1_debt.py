'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
'''

def annual_interest_payments(balance, annualInterestRate, monthlyPaymentRate):
	for i in range(1, 13):
		min_payment = balance * monthlyPaymentRate
		balance = balance - min_payment
		balance = balance + balance * annualInterestRate/12

		print("Month", i, "remaining balance:", round(balance, 2))

	return(balance)

annual_interest_payments(42, .2, .04)