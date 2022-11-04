def recipe_book(file):
	book = {}
	for line in file:
		dish = line.strip('\n')
		book[dish] = []
		ingred_quant = file.readline()
		for _ in range(int(ingred_quant)):
			ingred = file.readline().strip('\n').split(" | ")
			book[dish].append({'ingredient_name': ingred[0], 'quantity': ingred[1], 'measure': ingred[2]})
		file.readline()
	return book


def get_shop_list_by_dishes(dishes, person_count):
	shop_list = {}
	for dish, ingrediens in cook_book.items():
		if dish in dishes:
			for ingr in ingrediens:
				if ingr['ingredient_name'] in shop_list.keys():
					shop_list[ingr['ingredient_name']]['quantity'] += int(ingr['quantity'])*person_count
				else:
					shop_list[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': int(ingr['quantity'])*person_count}
	return shop_list


if __name__ == "__main__":

	with open('recipes.txt', 'rt', encoding='utf-8') as recipes:
		cook_book = recipe_book(recipes)

	new_shop = get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2)
	for i, j in new_shop.items():
		print(i, ": ", dict(j))

