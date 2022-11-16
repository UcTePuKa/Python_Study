import re
from homework.nine.help_func import help_func


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
            print(exit_func())
            break
        elif re.findall(r'^hello', command.lower()):
            print(hello_func())
        elif re.findall(r'^hello', command.lower()):
            print(help_func())
        elif re.findall(r'^add', command.lower()):
            add_func(command, contacts)
        elif re.findall(r'^change', command.lower()):
            change_func(command, contacts)
        elif re.findall(r'^phone', command.lower()):
            phone_func(command, contacts)
        elif re.findall(r'^show all', command.lower()):
            print(show_all_func(contacts))

def hello_func():
    return 'Hi! How can I help you?'


def exit_func():
    return 'Good bye!'



def add_func(command, contacts):
    new_data = command.split(' ')
    if new_data[1] in contacts:
        raise IndexError
    else:
        contacts[new_data[1]] = new_data[2]
        print(contacts)

def change_func(command, contacts):
    pass


def phone_func(command, contacts):
    new_data = command.split(' ')
    print(contacts[new_data[1]])


def show_all_func(contacts):
    return contacts


if __name__ == '__main__':
    main()

