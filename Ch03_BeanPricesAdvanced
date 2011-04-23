import urllib.request
import time

def send_to_twitter(msg,twitterusername,twitterpassword):
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                                  "http://twitter.com/statuses",
                                  twitterusername,
                                  twitterpassword)
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode( {'status': msg} )
    print(params)

def get_price():
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html") 
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])


twitterusername = input("Enter your Twitter username:")
twitterpassword = input("Enter your Twitter password:")
emergencyprice = input("Is a price required immediately? (Y/N)")

if emergencyprice == "Y":
    send_to_twitter(get_price(), twitterusername, twitterpassword)
else:
    price = get_price()
    while price >= 4.74:
        time.sleep(60)
        price = get_price()
    send_to_twitter("Buy!",twitterusername, twitterpassword)
