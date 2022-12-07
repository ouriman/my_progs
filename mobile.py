mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}
#  Your Code Starts from here
#Example of result: Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT

dictionary_data = mobile_data.get('data')

for single_data in dictionary_data:
    name = single_data.get('name')
    made_in = single_data.get('made')
    rate_usd = (single_data.get('price'))
    while " USD" in rate_usd:
        rate_usd = rate_usd.replace(" USD",'')
    rate_usd_number = float(rate_usd)
    rate_bdt_number = float(mobile_data['exchnage_rate'])
    bdt= round(rate_bdt_number * rate_usd_number)

    sentence = f'{name} is made in {made_in}. The price is {rate_usd_number} USD which is almost equal to {bdt} BDT.'
    print(sentence)