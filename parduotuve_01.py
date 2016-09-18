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


def produktai(adresas):
	nr	= 0
	html	= urlopen(adresas)
	bsObj	= BeautifulSoup(html.read(),"lxml")
	for linkas in bsObj.find_all('a',href=True):
		if linkas.parent.name =="span" and "hikashop_product_name" in linkas.parent["class"]:
			nr +=1
			target= "http://www.medialight.lt"+linkas["href"]
			print(nr,"\t",vardas_kaina(target))


target	="http://www.medialight.lt/component/hikashop/LED/12-led-juostos?Itemid=102"
produktai(target)
