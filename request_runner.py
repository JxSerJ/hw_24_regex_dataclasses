import requests

url = "http://127.0.0.1:5000/perform_query"
counter = 1

payload = [
    {
        'file_name': 'apache_logs.txt',
        'cmd1': 'filter',
        'value1': 'POST',
        'cmd2': 'map',
        'value2': '0'
    },
    {
        'file_name': 'apache_logs.txt',
        'cmd1': 'regex',
        'value1': 'images/\\w+\\.png',
        'cmd2': 'sort',
        'value2': 'asc'
    }
]

for entry in payload:
    response = requests.request("POST", url, data=entry)
    new_line = '\n'
    print(
        f'Request {counter}:\n{entry}\n\nResponse data: \n{response.text}\n\nStatus code: {response.status_code}\n\n\n')
    counter += 1
