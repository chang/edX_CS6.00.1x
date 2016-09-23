def bisect_monthly_payment(initialBalance, annualInterestRate):
	'''
	given an initial balance and an annualInterestRate
	returns the minimum monthly payment amount to pay off the balance in a year
	'''
	interest = annualInterestRate/12
	lower = initialBalance/12
	upper = (initialBalance * (1 + interest)**12)/12
	balance = initialBalance
	
	count = 0
	while abs(balance) > .01:
		# Set new payment
		payment = (upper - lower)/2 + lower

		# Calculate balance
		balance = initialBalance
		for i in range(0, 12):
			balance -= payment
			balance += balance * interest

		# Set new bounds
		if balance > 0:
			lower = payment
		else:
			upper = payment
			
		count += 1

	print(count)	
	return round(payment, 2)