from classes import InputData
from exceptions import IncorrectCommand

# filter, map, unique, sort, limit


def build_result_data(cmd, value, data):
    if cmd == 'filter':
        # res_through_lambda = [entry for entry in filter(lambda entry: value in entry, data)]
        res_through_list_comprehensions = [entry for entry in data if value in entry]
        return res_through_list_comprehensions

    elif cmd == 'map':
        res_through_lambda = [entry for entry in map(lambda entry: entry.split()[int(value)], data)]
        # res_through_list_comprehensions = [entry.split()[int(value)] for entry in data]
        return res_through_lambda

    elif cmd == 'limit':
        if value in ['', '0']:
            value = 10

        def data_gen(file_data, iterations):
            counter = 0
            while counter < int(iterations):
                try:
                    line = next(file_data).strip('\n')
                except StopIteration:
                    break
                yield line
                counter += 1

        result = [entry for entry in data_gen(file_data=iter(data), iterations=value)]
        return result

    elif cmd == 'unique':
        return list(set(data))

    elif cmd == 'sort':
        reverse_flag = value == 'desc'
        return sorted(data, reverse=reverse_flag)

    else:
        raise IncorrectCommand


def execute_query(query: InputData):
    with open(file=query.file_name, mode='r') as file:
        result = build_result_data(cmd=query.cmd1, value=query.value1, data=file)
        if query.cmd2:
            result = build_result_data(cmd=query.cmd2, value=query.value2, data=result)
        return result
