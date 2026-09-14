def ft_harvest_info(i, days):
    if i <= days:
        print(f"Day {i}")
        ft_harvest_info(i + 1, days)
    else:
        print("Harvest time!")

def ft_count_harvest_recursive():
    i = int(input("Days until harvest: "))
    ft_harvest_info(1, i)
