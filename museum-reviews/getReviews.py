# -*- coding: UTF-8 -*-

"""
Gather Wildlife Photographer of the Year reviews from Google Maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SimilarWeb trial: https://account.similarweb.com/journey/quiz
https://www.nhm.ac.uk/ (landing page too static. visitors don't know what the fad is about)
==Competitors==
1. https://www.londonzoo.org/ London Zoo (similar theme: endangered animals)
2. https://www.rmg.co.uk/ National Maritime Museum (similar nature: Astronomy Photographer of the Year)
3. https://www.vam.ac.uk/ V&A (proximity, one can visit for the whole day)
4. https://www.sciencemuseum.org.uk/ Science Museum (proximity, one can visit for the whole day)
5. https://www.kew.org/ Kew Gardens (well, tangential...)
6. https://www.britishmuseum.org/ the British Museum (well, tangential...)
"""

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


def get_review_gmaps():
    # Get gender (first name), geographical origin (full name), and age (profile pic, if present) of the person
    # ('Gender', 'Geography', 'Age')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    lst = []

    for keyword in ['photographer', 'photography']:
        # Directly enter 'Reviews'
        seed = 'https://www.google.com/maps/place/Natural+History+Museum/@51.496715,-0.1789475,17z/data=!3m1!5s0x4876055d2a7da3ef:0xf1f051391800f80!4m8!3m7!1s0x48760542e6182f3f:0x7bb7e385c39764c4!8m2!3d51.496715!4d-0.1763672!9m1!1b1!16zL20vMDF0Mzcy?entry=ttu&hl=en'

        driver.get(seed)
        sleep(1)
        driver.execute_script("if (document.querySelector('#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.AIC7ge > div.CxJub > div.VtwTSb > form:nth-child(2) > div > div > button > div.VfPpkd-RLmnJb')) document.querySelector('#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.AIC7ge > div.CxJub > div.VtwTSb > form:nth-child(2) > div > div > button > div.VfPpkd-RLmnJb').click();")
        sleep(2)
        driver.execute_script("if (document.querySelector('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div.m6QErb.Pf6ghf.XiKgde.KoSBEe.ecceSd.tLjsW > div.i7mKJb.fontBodyMedium > div.m3rned > div.pV4rW.q8YqMd > div > button > span')) document.querySelector('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div.m6QErb.Pf6ghf.XiKgde.KoSBEe.ecceSd.tLjsW > div.i7mKJb.fontBodyMedium > div.m3rned > div.pV4rW.q8YqMd > div > button > span').click();")
        sleep(2)

        driver.execute_script(
            f"document.querySelector('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div.m6QErb.Pf6ghf.XiKgde.KoSBEe.ecceSd.tLjsW > div.i7mKJb.fontBodyMedium.zzWGUd > div.MrFZRe.g8q29e > div > input').value = '{keyword}';")
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        sleep(2)

        for _ in range(30):
            driver.execute_script(f"document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2)').scrollTo(0, document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2)').scrollHeight * 2);")
            sleep(.5)

        cnt = 1

        try:
            while True:
                driver.execute_script(f"if (document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({
                                      cnt}) > div > div > div:nth-of-type(4) > div:nth-of-type(2) > div > span:nth-of-type(2) > button')) document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({cnt}) > div > div > div:nth-of-type(4) > div:nth-of-type(2) > div > span:nth-of-type(2) > button').click();")
                sleep(1)
                avatar = driver.execute_script(f"return document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({
                                               cnt}) > div > div > div:nth-of-type(1) > button > img').src")
                poster = driver.execute_script(f"return document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({
                                               cnt}) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1) > button > div:nth-of-type(1)').innerText;")
                spl = poster.split(' ')
                if len(spl) > 1:
                    last = spl[-1]
                    first = ' '.join(spl[:-1])
                else:
                    last = '[unknown]'
                    first = poster
                stars = driver.execute_script(f"return document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({
                                              cnt}) > div > div > div:nth-of-type(4) > div:nth-of-type(1) > span:nth-of-type(1)').querySelectorAll('.elGi1d').length;")
                comment = driver.execute_script(f"return document.querySelector('body > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(8) > div:nth-of-type(9) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(10) > div:nth-of-type({
                                                cnt}) > div > div > div:nth-of-type(4) > div:nth-of-type(2) > div > span:nth-of-type(1)').innerText;")
                print(f'--{int((cnt-1)/3)+1}-----------------------')
                print(f'{last}, {first}')
                print(stars)
                print(comment)
                lst.append([avatar, last, first, ec.classify_names([poster])[0].replace(
                    'rus', 'slv'), GenderExtractor().extract_gender(first.split(' ')[0]), stars, comment])

                cnt += 3
        except:
            pass
    df = pd.DataFrame(lst, columns=[
                      'avatar', 'last', 'first', 'nationality', 'gender', 'stars', 'comment'])
    df.drop_duplicates(inplace=True, ignore_index=True)
    df.to_excel('reviews2.xlsx', index=False)
    print(df)

    wordcloud

def format_similarweb():
    # Relatively high bounce rate
    # Short visit duration
    # Known high (~80%), social media low (<5 %).
    sns.set_theme()


if __name__ == '__main__':
    get_review_gmaps()
    # format_similarweb()
