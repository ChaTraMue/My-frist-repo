investment = 1000
rate = 0.05

for year in range (1, 31):
	investment = investment * (1+rate)
	print("Year", year, ":" , round(investment, 2))
