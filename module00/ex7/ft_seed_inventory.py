def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets" or unit == "grams" or unit == "area":
        match unit:
            case "packets":
                unit = "packets available"
            case "grams":
                unit = "grams total"
            case "area":
                unit = "square meters"
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit}")
    else:
        print("Unknown unit type")

