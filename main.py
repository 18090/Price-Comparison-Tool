import json

if __name__ == '__main__':
    price_data = None
    price = []
    with open('data.json', encoding='utf8') as f:
        price_data = f.read()

    if price_data is not None:
        json_price_data = json.loads(price_data)