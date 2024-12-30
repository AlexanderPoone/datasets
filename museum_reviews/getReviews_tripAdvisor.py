'''
Copyleft Alexander Poone 2024 Edutainment.

let names = [...document.querySelectorAll('body > div:nth-of-type(1) > main > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > section:nth-of-type(10) > div > div > div > section > section > div:nth-of-type(1) > div > div:nth-of-type(5) > div > div > div > div > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(2) > span > a')].map(e=>e.innerText);
	let dates = [...document.querySelectorAll('body > div:nth-of-type(1) > main > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > section:nth-of-type(10) > div > div > div > section > section > div:nth-of-type(1) > div > div:nth-of-type(5) > div > div > div > div > div:nth-of-type(4)')].map(e=>e.innerText.split(' • ')[0]);
	let modes = [...document.querySelectorAll('body > div:nth-of-type(1) > main > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > section:nth-of-type(10) > div > div > div > section > section > div:nth-of-type(1) > div > div:nth-of-type(5) > div > div > div > div > div:nth-of-type(4)')].map(e=>e.innerText.split(' • ')[1]);
	let titles = [...document.querySelectorAll('body > div:nth-of-type(1) > main > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > section:nth-of-type(10) > div > div > div > section > section > div:nth-of-type(1) > div > div:nth-of-type(5) > div > div > div > div > div:nth-of-type(3) > a > span')].map(e=>e.innerText);
	let comments = [...document.querySelectorAll('body > div:nth-of-type(1) > main > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > section:nth-of-type(10) > div > div > div > section > section > div:nth-of-type(1) > div > div:nth-of-type(5) > div > div > div > div > div:nth-of-type(5) > div:nth-of-type(1) > div > span > span')].map(e=>e.innerText);
	let stars = [...document.querySelectorAll('body > div:nth-of-type(1) > main > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > section:nth-of-type(10) > div > div > div > section > section > div:nth-of-type(1) > div > div:nth-of-type(5) > div > div > div > div > div:nth-of-type(2) > svg')].map(e=>e.querySelectorAll('path[d=\'M 12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.38 12-12c0-6.612-5.38-12-12-12z\']').length);
	let origins = [...document.querySelectorAll('body > div:nth-of-type(1) > main > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > section:nth-of-type(10) > div > div > div > section > section > div:nth-of-type(1) > div > div:nth-of-type(5) > div > div > div > div > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(2) > div > div > span:nth-of-type(1)')].map(e=>e.innerText.includes('contribution') ? undefined : e.innerText);
	for (let x = 0; x<10;x++){
	# names dates modes titles comments stars origins
	console.log(`${names[x]} | ${dates[x]} | ${modes[x]} | ${titles[x]} | ${comments[x]} | ${stars[x]} | ${origins[x]}`.replaceAll('\n','\\n'));
}
'''

from time import sleep

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from ethnicseer import EthnicClassifier
from gender_extractor import GenderExtractor
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from wordcloud import wordcloud

ec = EthnicClassifier.load_pretrained_model()

def get_reviews_tripadvisor():
	# Get gender (first name), geographical origin (full name), and age (profile pic, if present) of the person
	# ('Gender', 'Geography', 'Age')
	pd.set_option('display.max_columns', None)
	pd.set_option('display.max_rows', None)

	options = webdriver.ChromeOptions()
	driver = webdriver.Chrome(options=options)
	lst = []

	for keyword in ['photographer', 'photography']:
		# Directly enter 'Reviews'
		seed = 'https://www.tripadvisor.co.uk/Attraction_Review-g186338-d187676-Reviews-Natural_History_Museum-London_England.html'

		driver.get(seed)
		sleep(1)
		driver.execute_script("if (document.querySelector('#tab-data-qa-reviews-0 > div > div.LXdgT > div > div > div.Jscab > form > div').click();")
		sleep(2)
		driver.execute_script("if (document.querySelector('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div.m6QErb.Pf6ghf.XiKgde.KoSBEe.ecceSd.tLjsW > div.i7mKJb.fontBodyMedium > div.m3rned > div.pV4rW.q8YqMd > div > button > span')) document.querySelector('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div.m6QErb.Pf6ghf.XiKgde.KoSBEe.ecceSd.tLjsW > div.i7mKJb.fontBodyMedium > div.m3rned > div.pV4rW.q8YqMd > div > button > span').click();")
		sleep(2)

		driver.execute_script(f"document.querySelector('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div.m6QErb.Pf6ghf.XiKgde.KoSBEe.ecceSd.tLjsW > div.i7mKJb.fontBodyMedium.zzWGUd > div.MrFZRe.g8q29e > div > input').value = '{keyword}';")
		ActionChains(driver).send_keys(Keys.ENTER).perform()
		sleep(2)

		for _ in range(30):
			driver.execute_script(f"document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2)').scrollTo(0, document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2)').scrollHeight * 2);")
			sleep(.5)

		cnt = 1


		try:
			while True:
				driver.execute_script(f"if (document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({cnt}) > div > div > div:nth-of-type(4) > div:nth-of-type(2) > div > span:nth-of-type(2) > button')) document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({cnt}) > div > div > div:nth-of-type(4) > div:nth-of-type(2) > div > span:nth-of-type(2) > button').click();")
				sleep(1)
				avatar = driver.execute_script(f"return document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({cnt}) > div > div > div:nth-of-type(1) > button > img').src")
				poster = driver.execute_script(f"return document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({cnt}) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1) > button > div:nth-of-type(1)').innerText;")
				spl = poster.split(' ')
				if len(spl) > 1:
					last = spl[-1]
					first = ' '.join(spl[:-1])
				else:
					last = '[unknown]'
					first = poster
				stars = driver.execute_script(f"return document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({cnt}) > div > div > div:nth-of-type(4) > div:nth-of-type(1) > span:nth-of-type(1)').querySelectorAll('.elGi1d').length;")
				comment = driver.execute_script(f"return document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({cnt}) > div > div > div:nth-of-type(4) > div:nth-of-type(2) > div > span:nth-of-type(1)').innerText;")
				print(f'--{int((cnt-1)/3)+1}-----------------------')
				print(f'{last}, {first}')
				print(stars)
				print(comment)
				lst.append([avatar, last, first, ec.classify_names([poster])[0].replace('rus', 'slv'), GenderExtractor().extract_gender(first.split(' ')[0]), stars, comment])

				cnt += 3
		except:
			pass
	df = pd.DataFrame(lst, columns=['avatar', 'last', 'first', 'nationality', 'gender', 'stars', 'comment'])
	df.drop_duplicates(inplace=True, ignore_index=True)
	df.to_excel('reviews2.xlsx', index=False)
	print(df)

	wordcloud

if __name__ == '__main__':
	get_reviews_tripadvisor()