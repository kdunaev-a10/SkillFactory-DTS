import pandas as pd # Импорт библиотеки pandas — при выполнении последовательно всех примеров ниже, импорт библиотеки pandas выполняется один раз
import json # Импортируем модуль json
from pprint import pprint # Импортируем функцию pprint()

 
with open('c:/Users/kot/OneDrive/Documents/GitHub/SkillFactory-DTS/module-python/module16/data/recipes.json') as f:
    recipes = json.load(f)

all_ingredients=set() # Создаем пустое множество для хранения реестра уникальных ингредиентов
for recipe in recipes: # Начинаем перебор всех блюд входящих в список
    for ingredient in recipe['ingredients']: # Начинаем перебор всех ингредиентов входящих в состав текущего блюда
        all_ingredients.add(ingredient ) # Добавляем уникальный ингредиент в реестр
    
df = pd.DataFrame(recipes) # Создаем объект DataFrame из списка recipes

def contains(ingredient_list): # Определяем имя функции и передаваемые аргументы
    if ingredient_name in ingredient_list: # Если ингредиент есть в текущем блюде,
        return 1 # возвращаем значение 1
    else: # Если ингредиента нет в текущем блюде,
        return 0 # возвращаем значение 0
            
for ingredient_name in all_ingredients: # Последовательно перебираем ингредиенты в реестре all_ingredients
    df[ingredient_name] = df['ingredients'].apply(contains) # В DataFrame cоздаем столбец с именем текущего ингредиента и заполняем его единицами и нулями, используя ранее созданную функцию contains

df['ingredients'] = df['ingredients'].apply(len) # Заменяем список ингредиентов в рецепте, на их количество


