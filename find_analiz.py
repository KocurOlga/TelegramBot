import pandas as pd

#def find_price(dict, text):


text = input("Введите нужный анализ: ")

#считываем данные из прайса
price_data = pd.read_excel('List_analyz.xlsx', sheet_name='data') #считывает данные из файла
price_dict = price_data.to_dict(orient='records') #преобразовываем данные в словарь Услуга-Цена

find_price = [] #в этот список будут сохраняться найденные услуги

for element in price_dict:
    str1 = text.lower()
    str2 = str(element['Service']).lower()
    if set(str1.split()).issubset(set(str2.split())):
    # if text.lower() in str(element['Service']).lower():
        find_price.append(element['Service'] + ' - ' + element['Price'])
    
print(*find_price, sep='\n')
