def ft_harvest_total():
    sum = 0;
    for i in range(3):
        sum += int(input(f"Day {i} harvest: "))
    print("Total harvest:", sum)
