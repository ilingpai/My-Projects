"""
File: webcrawler.py
Name: Sandy
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html,  features="html.parser")

        # ----- Write your code below this line ----- #
        # From Jennifer
        tags = soup.find_all('td')  # 若要得到所有 <td> 與 </td> 之間的文字，可以直接對 soup 裡面的 <tbody> 物件取出文字
        data_list = []  # 把所有資料先存進這個list
        for tag in tags:
            text = tag.text.split()
            if len(text) == 1:
                data_list.append(text[0])
        text_count = 0
        rank_list = []  # 把五個值變成一個list後再計算
        sum_male = 0
        male = ''
        sum_female = 0
        female = ''
        for word in data_list:
            text_count += 1
            rank_list.append(word)
            # 每五個word變成一個list
            if text_count % 5 == 0 and text_count <= 1000:  # 200*5=1000
                for ch in rank_list[2]:
                    if ch.isdigit():
                        male += ch
                sum_male += int(male)
                male = ''

                for ch in rank_list[4]:
                    if ch.isdigit():
                        female += ch
                sum_female += int(female)
                female = ''
                rank_list = []
        print(f'Male Number:{sum_male}')
        print(f'Female Number:{sum_female}')


if __name__ == '__main__':
    main()
