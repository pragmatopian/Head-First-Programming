import urllib.request
 
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty.html") 
text = page.read() . decode("utf8")


 
price = text[text.find("$")+1:text.find("$")+6]
print(price)
