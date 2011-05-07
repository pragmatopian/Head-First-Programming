def save_transaction(price, credit_card, description):
    file = open("transactions.txt","a")
    file.write("%07d%s%s\n" % (price * 100, credit_card, description))
    file.close()
