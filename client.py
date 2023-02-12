import requests

# response = requests.post('http://127.0.0.1:5000/users',
#                          json={'username': 'user3', 'password' : '123456',})




# response2 = requests.post('http://127.0.0.1:5000/post',
#                          json={'header' : '5', 'description' : 'test1', 'owner' : 'user1'})


response2 = requests.get('http://127.0.0.1:5000/post/8')
#
# response3 = requests.get('http://127.0.0.1:5000/user/5')




# print(response2.status_code)
# print(response2.text)
#
# print(f'юзеры - {response3.status_code}, {response3.text}')

print(response2.status_code, response2.text)