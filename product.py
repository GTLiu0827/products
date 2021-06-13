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

#products[0][0] 
#大list的第0個sub-list的第0值

# p 大List的index
# p[n] : n ==> sub-list index
for p in products:
	print(p)
	print(p[0],'的價錢是:', p[1])

# 寫出檔案
# 字串合併
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# .csv 常用的資料儲存格式
# 可以用excel打開
# encoding='utf-8' 解決中文亂碼問題
with open ('products.csv', 'w', encoding='utf-8') as f:
	# 增加 Excel的欄位名稱
	f.write('商品,價格\n')
	for p in products:
		# 合併 名稱和價格字串
		# 寫入 product.txt
		# ',' 為excel所需的重要分隔
		f.write(p[0] + ',' + p[1] + '\n')
