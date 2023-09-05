from flask import Flask, render_template, request, redirect, url_for
import requests, json
import xmltodict
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time

app = Flask(__name__)  # Initialize app

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/check_price", methods=["GET", "POST"])
def check_price(): #크롤링한 결과 넘기기
    search_date = request.args.get('search_date')
    item = request.args.get('item')
    avg_total_price = check(search_date, item)
    #stndrd = check2(search_date, item)
    context = {
        'search_date': search_date,
        'item': item,
        #'stndrd':stndrd,
        'avg_total_price': avg_total_price,
    }
    if avg_total_price == 0:
        context['message'] = '거래량이 없습니다.'
        
    return render_template("index.html", **context)
    #return context

@app.route('/food_info', methods=['GET'])
def food_info(): # 웹 스크래핑결과 넘기기
    ingredient = request.args.get('ingredient', '')
    if ingredient:
        food_data = food_info(ingredient)
        return render_template('index.html', food_data=food_data)
    return redirect(url_for('index'))

def check(search_date, item): # 평균가격 구하기
    api_key = 'c2917cd77707a74648073999146fd65f4f986ad3c47e6f79a83f633d8ab725cb'
    url = f'http://211.237.50.150:7080/openapi/{api_key}/xml/Grid_20150401000000000216_1/1/1000?AUCNG_DE={search_date}&PRDLST_NM={item}'
    content = requests.get(url).content
    data_dict = xmltodict.parse(content)

    totalCnt = int(data_dict['Grid_20150401000000000216_1']['totalCnt'])

    if totalCnt == 0:
        return 0

    page_size = 1000
    num_pages = (totalCnt + page_size - 1) // page_size
    total_price = []

    for i in range(num_pages):
        minimum = i * page_size + 1
        maximum = (i + 1) * page_size
        total_url = f'http://211.237.50.150:7080/openapi/{api_key}/xml/Grid_20150401000000000216_1/{minimum}/{maximum}?AUCNG_DE={search_date}&PRDLST_NM={item}'
        total_content = requests.get(total_url).content
        total_dict = xmltodict.parse(total_content)

        for row in total_dict['Grid_20150401000000000216_1']['row']:
            if isinstance(row, dict):
                total_price.append(int(row['AVRG_AMT']))

    avg_total_price = sum(total_price) // totalCnt
    return avg_total_price

def food_info(name):
    url = f"https://www.10000recipe.com/recipe/list.html?q={name}"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else : 
        print("HTTP response error :", response.status_code)
        return
    
    food_list = soup.find_all(attrs={'class':'common_sp_link'})
    food_id = food_list[0]['href'].split('/')[-1]
    new_url = f'https://www.10000recipe.com/recipe/{food_id}'
    new_response = requests.get(new_url)
    if new_response.status_code == 200:
        html = new_response.text
        soup = BeautifulSoup(html, 'html.parser')
    else : 
        print("HTTP response error :", response.status_code)
        return
    
    food_info = soup.find(attrs={'type':'application/ld+json'})
    result = json.loads(food_info.text)
    ingredient = ','.join(result['recipeIngredient'])
    recipe = [result['recipeInstructions'][i]['text'] for i in range(len(result['recipeInstructions']))]
    for i in range(len(recipe)):
        recipe[i] = f'{i+1}. ' + recipe[i]
    
    res = {
        'name': name,
        'ingredients': ingredient,
        'recipe': recipe
    }

    return res

if __name__ == "__main__":
    app.run(debug=True)
