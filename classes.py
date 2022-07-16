class InputData:
    def __init__(self, file_name, cmd1, value1, cmd2, value2):
        self.file_name = file_name
        self.cmd1 = cmd1
        self.value1 = value1
        self.cmd2 = cmd2
        self.value2 = value2

    def __repr__(self):
        return f'Request:\n' \
               f'{"file_name"}: {self.file_name} \n' \
               f'{"cmd1"}: {self.cmd1} \n' \
               f'{"value1"}: {self.value1} \n' \
               f'{"cmd2"}: {self.cmd2} \n' \
               f'{"value2"}: {self.value2} \n'
