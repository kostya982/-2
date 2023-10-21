salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0

for _ in range(months):
    required_money = spend - salary
    if required_money > 0:
        money_capital += required_money
    spend += spend * increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
