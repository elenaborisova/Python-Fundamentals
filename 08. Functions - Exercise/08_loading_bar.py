def visualize_loading_bar(number):
    symbol_count = number // 10

    if 0 <= number < 100:
        print(f"{number}% [{symbol_count * '%' + (10 - symbol_count) * '.'}]")
        print("Still loading...")
    elif number == 100:
        print("100% Complete!")
        print(f"[{symbol_count * '%'}]")


number = int(input())
visualize_loading_bar(number)
