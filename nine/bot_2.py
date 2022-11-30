contacts_dict = {}


def input_error(function):
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contact cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
    return inner


@input_error
def hello_func():
    return 'How can I help you?'


@input_error
def exit_func():
    return 'good bye'


@input_error
def add_func(data):
    name, phone = create_data(data)
    if name in contacts_dict:
        raise ValueError('This contact already exist.')
    contacts_dict[name] = phone
    return f'You added new contact: {name} with this {phone}.'


@input_error
def change_func(data):
    name, phone = create_data(data)
    if name in contacts_dict:
        contacts_dict[name] = phone
        return f'You changed number to {phone} for {name}.'
    return 'Use add command plz.'


@input_error
def search_func(name):
    if name.strip() not in contacts_dict:
        raise ValueError('This contact does not exist.')
    return contacts_dict.get(name.strip())


@input_error
def show_func():
    contacts = ''
    for key, value in contacts_dict.items():
        contacts += f'{key} : {value} \n'
    return contacts


COMMANDS_DICT = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': add_func,
    'change': change_func,
    'show all': show_func,
    'phone': search_func
}


def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()


def reaction_func(reaction):
    return COMMANDS_DICT.get(reaction, break_func)


def create_data(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phone = new_data[1]
    if name.isnumeric():
        raise ValueError('Wrong name.')
    if not phone.isnumeric():
        raise ValueError('Wrong phone.')
    return name, phone


def break_func():
    return 'Wrong enter.'


def main():
    while True:
        user_input = input('Enter command for bot: ')
        result = change_input(user_input)
        print(result)
        if result == 'good bye':
            break


if __name__ == '__main__':
    main()