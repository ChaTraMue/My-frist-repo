def compound_growth(investment, rate, years):
	for year in range(1, years+1):
		investment = investment * (1+rate)
		print("Year", year, ":", round(investment, 2))

compound_growth(1000, 0.05, 30)
compound_growth(5000, 0.07, 20)
compound_growth(500, 0.1, 10)
 
