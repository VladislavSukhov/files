from pprint import pprint
import os

def book_to_dict(file_path):
    cb_dict = {}
    with open (file_path) as f:
        while True:
            name = f.readline()
            if name == os.linesep:
                continue
            name = name.strip()
            if not name:
                break
            quantity = int(f.readline().strip())
            ingredients = []
            for i in range(quantity):
                ing = f.readline().strip().split(' | ')
                ingredient = {}
                ingredient['ingredient_name'] = ing[0]
                ingredient['quantity'] = ing[1]
                ingredient['measure'] = ing[2]
                ingredients.append(ingredient)
            cb_dict[name] = ingredients
    return cb_dict



def get_shop_list_by_dishes(dishes, person = 1):
    cb_dict = book_to_dict('recipes.txt')
    list_of_ingredients = {}
    for dish in dishes:
        if dish in cb_dict.keys():
            for sdish in cb_dict[dish]:
                amount = {}                
                sdish['quantity'] = int(sdish['quantity']) * person
                amount['measure'] = sdish['measure']
                amount['quantity'] = sdish['quantity']
                list_of_ingredients[sdish['ingredient_name']] = amount
    pprint(list_of_ingredients)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
