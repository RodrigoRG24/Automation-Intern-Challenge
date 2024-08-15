def total_candy_bars(initial_money, candy_price, wrappers_needed_for_free):
    initial_bars = initial_money // candy_price
    total_bars = initial_bars
    wrappers = initial_bars

    while wrappers >= wrappers_needed_for_free:
        free_bars = wrappers // wrappers_needed_for_free
        total_bars += free_bars
        wrappers = wrappers % wrappers_needed_for_free + free_bars

    return total_bars


initial_money = 30
candy_price = 2
wrappers_needed_for_free = 3

result = total_candy_bars(initial_money, candy_price, wrappers_needed_for_free)
print(f"Kyle puede obtener un total de {result} barras de chocolate.")
