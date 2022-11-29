import requests
import random


class ApiDataMock:
    '''
    I made an schema for different values:
        first_name / last_name / email / password
    And with that, made an API that generate 100 values of them
    '''
    
    url = 'https://my.api.mockaroo.com/users.json?key=64068820'
    response = requests.get(
        'https://my.api.mockaroo.com/users.json?key=64068820'
    )
    data = response.json() # manage response as a json

    i = random.randint(0, 99) # Number from 0 to 99 (quantity of values that the json have)

    first_name = data[i]['first_name']
    last_name = data[i]['last_name']
    email_address = data[i]['email']
    password = data[i]['password']

    # print(f'The first name is: {first_name}, followed by his last name: {last_name}')
    # print(f'The email address is: "{email_address}". And his password: "{password}"')