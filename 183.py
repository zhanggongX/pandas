import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers


if __name__ == '__main__':
    data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
    Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[1, 3], [2, 1]]
    Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})
