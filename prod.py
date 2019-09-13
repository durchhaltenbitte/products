import os #operating system 

#refector: 重构程式

def read(filename):
    products = []
    with open(filename, 'r') as f:
        for line in f:
            if '商品, 价格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print('已录入商品:\n', products)
    return products

def write(products):
    while True:
        print('正在添加商品')
        name = input('请输入商品名称：')
        if name == 'q':
            break
        price = input('请输入商品价格：')
        products.append([name, price])
    return products

def show(products):
    for p in products:
        print(p[0], '的价格是', p[1])

def save(filename, products):
    with open(filename, 'w') as f:
        f.write('商品, 价格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')
    print('文档写入成功!')

def main():
    x = 1
    while x:
        filename = input('请输入要读取的文件名:')
        if os.path.isfile(filename):
            print('文档读取成功！')
            products = read(filename)
        else:
            print('找不到该文档')
        products = write(products)
        show(products)
        save(filename, products)
        x = input('继续执行(1)/退出程序(0)?:')
        x = int(x)

main()
