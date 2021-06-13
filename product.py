# 二維陣列清單
# List in List
# 重複輸入商品名稱,價格
# |--------------|--------------|--------------|--------------|
# |   --------   |   --------   |   --------   |   --------   |
# |  |n   |p  |  |  |n   |p  |  |  |n   |p  |  |  |n   |p  |  |
# |   --------   |   --------   |   --------   |   --------   |
# |--------------|--------------|--------------|--------------|
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	# Method 1
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	# Method 2
	#p = [name, price]
	#products.append(p)
	# Method 3
	products.append([name, price])
print(products)

#請輸入商品名稱: 珍奶 50
#請輸入商品價格: 紅茶 40
#請輸入商品名稱: q
#[['珍奶 50', '紅茶 40']]
#兩個中括弧[[]] ==> 2D list

products[0][0] 
#大list的第0個sub-list的第0值
