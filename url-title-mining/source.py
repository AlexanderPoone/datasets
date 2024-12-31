import pandas as pd
from selenium import webdriver
from time import sleep

# Root
root = 'https://www.oriprobe.com/journals/caod_7305/2015_25.html'
self.driver.get(root)

all_links_script = r'''let entities = [...document.querySelectorAll("body > div > div:nth-child(4) > div:nth-child(1) > div > div:nth-child(1) > a")];
let links = entities.map(e=>({'href': e.href, 'innerText': e.innerText}));
return links;'''

mydict = self.driver.execute_script(all_links_script)
pprint(mydict)

for x in mydict:
	self.driver.get(x['href'])
	sleep(1)
	self.driver.execute_script('document.querySelector("body > div.Pages > div.icontent > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > a").click()')
	sleep(1)
	ground_truth = self.driver.execute_script('return document.querySelector("#form1 > div:nth-child(6) > table > tbody > tr:nth-child(1) > td:nth-child(2) > strong").innerText')
	print(ground_truth)
	self.ground_truths.append(ground_truth)

	self.df = pd.DataFrame()
