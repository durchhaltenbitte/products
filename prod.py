products = []
while True:
    name = input('请输入商品名称：')
    if name == 'q':
        break
    price = input('请输入商品价格：')
    products.append([name, price])

for p in products:
    print(p[0], '的价格是', p[1])

#存到本地 用Excel打开 加名头
with open('pro.csv', 'w') as f:
    f.write('商品, 价格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

