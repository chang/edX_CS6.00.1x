def fixed_monthly_payment(initialBalance, annualInterestRate):
	'''
	given an initial balance and an annualInterestRate
	returns the minimum monthly payment amount to pay off the balance in a year
	'''
	interest = annualInterestRate/12
	payment = round(initialBalance/12, -1)
	balance = 0
	count = 0

	while balance >= 0:
		balance = initialBalance
		payment += 10
		for i in range(0, 12):
			balance -= payment
			balance += balance * interest
		count += 1
	
	print(count)	
	return payment