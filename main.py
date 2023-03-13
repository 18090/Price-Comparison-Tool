import json

if __name__ == '__main__':
    price_data = None
    price = []
    with open('data.json', encoding='utf8') as f:
        price_data = f.read()

    if price_data is not None:
        json_price_data = json.loads(price_data)

for d in json_price_data:
            price.append({'name': d['name'], 'price': float(d['newworld_price']), 'url': d['newworld_url']})
            price.append({'name': d['name'], 'price': float(d['paknsave_price']), 'url': d['paknsave_url']})
            price.append({'name': d['name'], 'price': float(d['countdown_price']), 'url': d['countdown_url']})
            minPricedItem = min(price, key=lambda x: x['price'])
            print(minPricedItem)
            print('=================')
            price = []