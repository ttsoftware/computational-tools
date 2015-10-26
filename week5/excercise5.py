from pprint import pprint
import re
from week5.mongodb import Mongodb

db = Mongodb('Northwind')

orders = db.find_by('orders', {'CustomerID': 'ALFKI'})

order_details = db.find_by(
    'order-details', {
        'OrderID': {
            '$in': map(lambda x: x['OrderID'], orders)
        }
    }
)

products = db.find_by(
    'products', {
        'ProductID': {
            '$in': map(lambda x: x['ProductID'], order_details)
        }
    }
)


#  excercise 5.2
def excercise5_2():
    for order in orders:
        print 'Order ID:' + str(order['OrderID'])
        pprint(
            map(
                lambda y: y['ProductName'],
                db.join_in(
                    products,
                    map(
                        lambda x: x['ProductID'],
                        db.join(order_details, order, 'OrderID', 'OrderID')
                    ),
                    'ProductID'
                )
            )
        )


# excercise 5.3
def excercise5_3():
    for order in orders:
        order_products = map(
            lambda y: y['ProductName'],
            db.join_in(
                products,
                map(
                    lambda x: x['ProductID'],
                    db.join(order_details, order, 'OrderID', 'OrderID')
                ),
                'ProductID'
            )
        )

        if len(order_products) > 1:
            print 'Order ID:' + str(order['OrderID'])
            pprint(order_products)


# excercise5_2()
# excercise5_3()

def excercise5_4():
    order_details = db.find_by('order-details', {'ProductID': 7})

    orders = db.find_by('orders', {
        'OrderID': {
            '$in': map(lambda x: x['OrderID'], order_details)
        }
    })

    customers = db.find_by('customers', {
        'CustomerID': {
            '$in': map(lambda x: x['CustomerID'], orders)
        }
    })

    return customers


# customers = excercise5_4()
# pprint(len(customers))
# pprint(map(lambda x: x['ContactName'], customers))

def excercise5_5():
    customers = excercise5_4()

    orders = db.find_by('orders', {
        'CustomerID': {
            '$in': map(lambda x: x['CustomerID'], customers)
        }
    })

    order_details = db.find_by('order-details', {
        'OrderID': {
            '$in': map(lambda x: x['OrderID'], orders)
        }
    })

    products = db.find_by('products', {
        'ProductID': {
            '$in': map(lambda x: x['ProductID'], order_details),
            '$not': re.compile("7")
        }
    })

    pprint(len(products))
    pprint(map(lambda x: x['ProductName'], products))


# excercise5_5()


def excercise5_6():
    customers = excercise5_4()

    orders = db.find_by('orders', {
        'CustomerID': {
            '$in': map(lambda x: x['CustomerID'], customers)
        }
    })

    gb = db.group_by(
        'order-details',
        key={'ProductID': 1},
        condition={
            'OrderID': {
                '$in': map(lambda x: x['OrderID'], orders)
            }
        },
        reduce_function='function (current, result) { result.total += current.Quantity; }',
        initial={'total': 0}
    )

    pprint(len(orders))
    pprint(gb)

excercise5_6()
