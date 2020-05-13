"""
    重构
"""

dict_commodity_info = {
    101: {
        "name": "tld",
        "price": 10000
    },
    102: {
        "name": "ytj",
        "price": 10000
    },
    103: {
        "name": "jyzj",
        "price": 8000
    },
    104: {
        "name": "xlsbz",
        "price": 9000
    },
    105: {
        "name": "lmsj",
        "price": 8000
    },
}

list_order = []


def select_menu():
    while True:
        str_number = input("1 : shopping, 2 : account")
        if str_number == "1":
            shopping()
        elif str_number == "2":
            settlement()


def settlement():
    """
        结算
    :return:
    """
    print_order()
    total_price = get_total_price()
    pay(total_price)


def pay(total_price):
    """
        支付
    :param total_price: 需要支付的价格
    :return:
    """
    while True:
        money = float(input("total price is %d . pl. input money: " % total_price))
        if money >= total_price:
            print("success, change : ￥%d" % (money - total_price))
            list_order.clear()
            break
        else:
            print("no money")


def print_order():
    """
        打印订单
    :return:
    """
    for item in list_order:
        commodity_info_item = dict_commodity_info[item["number"]]
        print("commodity: %s, price: %d, count: %d" % (
            commodity_info_item["name"], commodity_info_item["price"], item["count"]
        ))


def get_total_price():
    """
        计算总价
    :return:
    """
    total_price = 0
    for item in list_order:
        commodity_info_item = dict_commodity_info[item["number"]]
        total_price += item["count"] * commodity_info_item["price"]
    return total_price


def shopping():
    """
        购物
    :return:
    """
    print_commodity()
    dict_order = create_order()
    list_order.append(dict_order)
    print("add shopping car")


def create_order():
    """
        创建订单
    :return:
    """
    while True:
        int_commodity_number = int(input("pl. input commodity number"))
        if int_commodity_number in dict_commodity_info:
            break
        else:
            print("do not have this")
    int_commodity_count = int(input("pl. input commodity count"))
    return {"number": int_commodity_number, "count": int_commodity_count}


def print_commodity():
    """
        打印商品信息
    :return:
    """
    for key, value in dict_commodity_info.items():
        print("编号：%d, 名称：%s, 单价： %d." %
              (key, value["name"], value["price"]))


select_menu()
