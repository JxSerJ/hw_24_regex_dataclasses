from dataclasses import dataclass


@dataclass
class InputData:
    file_name: str
    cmd1: str
    value1: str
    cmd2: str
    value2: str

    def __repr__(self):
        return f'Request:\n' \
               f'{"file_name"}: {self.file_name} \n' \
               f'{"cmd1"}: {self.cmd1} \n' \
               f'{"value1"}: {self.value1} \n' \
               f'{"cmd2"}: {self.cmd2} \n' \
               f'{"value2"}: {self.value2} \n'
