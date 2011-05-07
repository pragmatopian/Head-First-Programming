import Ch06_POS_TransactionModule
import Ch06_POS_Promotion
import Ch06_POS_StarbuzzPromotion

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.0, 1.80, 1.20]
running = True

while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")

    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        new_price = Ch06_POS_Promotion.discount(prices[choice - 1])

        hasstarbuzzdiscountcard = input("Does customer have Starbuzz discount card? (Y/N)")

        if hasstarbuzzdiscountcard == "Y":
            new_price = Ch06_POS_StarbuzzPromotion.discount(new_price)

        Ch06_POS_TransactionModule.save_transaction(new_price, credit_card, items[choice - 1])
