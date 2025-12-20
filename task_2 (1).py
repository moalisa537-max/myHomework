salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_reserve = 0
monthly_expense = spend

for _ in range(months):
    shortage = monthly_expense - salary
    total_reserve += shortage
    monthly_expense *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(total_reserve))