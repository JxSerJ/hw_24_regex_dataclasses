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
        'cmd1': 'filter',
        'value1': 'GET',
        'cmd2': 'limit',
        'value2': 'hjgjk'
    },
    {
        'file_name': 'apache_logs.txt',
        'cmd1': 'limit',
        'value1': '0',
        'cmd2': 'unique',
        'value2': ''
    },
    {
        'file_name': 'apache_logs.txt',
        'cmd1': 'limit',
        'value1': '0',
        'cmd2': 'sort',
        'value2': 'desc'
    },
    {
        'file_name': '543534534_logs.txt',
        'cmd1': 'limit',
        'value1': '1332',
        'cmd2': 'unique',
        'value2': ''
    },
    {
        'file_name': 'apache_logs.txt',
        'cmd1': 'gdfgdfhfd',
        'value1': '1332',
        'cmd2': 'unibfdsgerque',
        'value2': ''
    }
]

for entry in payload:
    response = requests.request("POST", url, data=entry)
    new_line = '\n'
    print(
        f'Request {counter}:\n{entry}\n\nResponse data: \n{response.text}\n\nStatus code: {response.status_code}\n\n\n')
    counter += 1
