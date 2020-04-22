# coding:utf-8
# @Time  : 2020/4/22 18:37
# @Author: Xiawang
# Description:


def check_total_price(shopping_list):
    total_price = 0
    for need_commodity, shopping_quantity in shopping_list:
        commodity_total_price = get_commodity_prices(need_commodity) * shopping_quantity
        total_price += commodity_total_price
    return total_price


def get_commodity_prices(need_commodity):
    commodity_price = [
        ('wine', 'drink', 15),
        ('cola', 'drink', 5),
        ('pork', 'meat', 25),
        ('chicken', 'meat', 10),
        ('light', 'electronics', 100)
    ]
    for commodity, kind, price in commodity_price:
        if need_commodity == commodity:
            return price


if __name__ == '__main__':
    user_shopping_list = [('wine', 1), ('cola', 2),
                          ('pork', 2), ('chicken', 5), ('light', 1)]
    result = check_total_price(user_shopping_list)
    print(result)
