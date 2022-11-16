import re
from Python_Study.nine.help_func import help_func


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contact cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
    return inner

@input_error
def main():
    contacts = {}
    while True:
        command = input('Please input the command: ')
        if re.findall(r'\.|exit|close|good.bye', command.lower()):
            print('Good bye!')
            break
        elif command.strip().lower() == 'hello':
            print('Hi! How can I help you?')
        elif command.strip().lower() == 'help':
            print(help_func())
        elif re.findall(r'^add', command.lower()) or re.findall(r'^change', command.lower()):
            add_change_func(command, contacts)
        elif re.findall(r'^phone', command.lower()):
            phone_func(command, contacts)
        elif re.findall(r'^show all', command.lower()):
            print(contacts)


def add_change_func(command, contacts):
    new_data = command.split(' ')
    contacts[new_data[1]] = new_data[2]


def phone_func(command, contacts):
    new_data = command.split(' ')
    print(contacts[new_data[1]])


if __name__ == '__main__':
    main()

