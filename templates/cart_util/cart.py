from string import Template


class MyTemplate(Template):
    """
    adding delimiter to replace default $ delimiter
    """
    delimiter = "#"


def cart_template():
    cart = []
    cart.append(dict(item="cake", price=8, qty=2))
    cart.append(dict(item="cake", price=12, qty=1))
    cart.append(dict(item="fish", price=32, qty=4))
    t = Template("$qty * $item =$price")
    total = 0
    for data in cart:
        print(t.substitute(data))
        # print(f"data is {data}")
        total += data["price"]
    print(f"total price is {str(total)}")
    return (total)


def cart_modify_template():
    cart = []
    cart.append(dict(item="cake", price=8, qty=2))
    cart.append(dict(item="cake", price=12, qty=1))
    cart.append(dict(item="fish", price=32, qty=4))
    t = Template("$qty * $item =$price")
    total = 0
    for data in cart:
        print(t.substitute(data))
        # print(f"data is {data}")
        total += data["price"]
    print(f"total price is {str(total)}")
    return (total)



