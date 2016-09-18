from bs4 import BeautifulSoup
from urllib.request import urlopen

def vardas_kaina(adresas):
	html	= urlopen(adresas)
	bsObj	= BeautifulSoup(html.read(),"lxml")
	name	= bsObj.find("span",{"id":"hikashop_product_name_main"})
	price	= bsObj.find("span",{"class":"hikashop_product_price hikashop_product_price_0"})
	try:
		tekstas = name.string.strip()+"\t"+price.string
	except AttributeError:
		tekstas = name.string.strip()+"\t nera"
	return tekstas

target	="http://www.medialight.lt/component/hikashop/LED-produkcija/1-led-juosta-4-8w-silto-salto-spektro-ip33?Itemid=102"
print(vardas_kaina(target))

