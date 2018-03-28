def add(person: str, number: int):
    """This function adds a new contact to the phone book.

    :param person: The name of the contact user wishes to add.
    :type person: str.
    :param number: The phone number of the contact user wishes to add.
    :type number: int.
    :returns None.
    """
    global phone_book
    if person in phone_book:
        if number in phone_book[person]:
            print('{} already has the phone number {}.'.format(person, number))
        else:
            phone_book[person].append(number)
            print('The new phone number {} for {} has been successfully added to your phone book!'.format(number, person))
    else:
        phone_book[person] = [number]
        print('{} with the phone number {} has been successfully added to your phone book!'.format(person, number))


def show_numbers(person: str):
    """This function prints all the phone numbers of the person from the phone book.

    :param person: The name of the person whose phone numbers will be printed.
    :type person: str.
    :returns None.
    """
    global phone_book
    if person in phone_book:
        print("Name", end='')
        for i in range(len(person) - 1):
            print(end=' ')
        print("Phone number")
        for number in phone_book[person]:
            print(person, end='   ')
            print(number)
    else:
        print('There is no such person as {} in your phone book!'.format(person))


def delete_person(person: str):
    """This function deletes a person with all of his/her phone numbers from the phone book.

    :param person: The name of the person who will be deleted.
    :type person: str.
    :returns None.
    """
    global phone_book
    if person in phone_book:
        phone_book.pop(person)
        print('{} has been successfully deleted from your phone book!'.format(person))
    else:
        print('There is no such person as {} in your phone book!'.format(person))


def parse_command(comm: str) -> list:
    """This function parses the string to the substrings (ignoring the spaces) and returns all the substrings stored by
    order in a list.

    :param comm: The string that will be parsed.
    :type comm: str.
    :returns list -- the list, which contains the substrings.
    """
    buff = ''
    res = []
    for c in comm:
        if c != ' ':
            buff += c
        else:
            if len(buff) > 0:
                res.append(buff)
                buff = ''
    if len(buff) > 0:
        res.append(buff)
    return res


print('Hello! This is your personal phone book. You can use it to store your contacts.\n'
      'Use these commands to manage it:\n'
      '- Print "Add *NAME* *NUMBER*" to add a new contact or a new phone number for the existing contact. Print the '
      'name and the number of the contact you wish do add or complement instead of *NAME* and *NUMBER* respectively.\n'
      '- Print "Delete *NAME*" to delete a contact (including all of its phone numbers). Print the name of the contact '
      'you wish to delete instead of *NAME*.\n'
      '- Print "Show *NAME*" to show all the numbers of the contact with the name *NAME*.\n'
      '- If you wish to terminate this session, print "Exit".\n')
phone_book = {}
while True:
    command = str(input('>>>'))
    todo = parse_command(command)
    if todo[0] == 'Add' and len(todo) == 3:
        add(todo[1], int(todo[2]))
    elif todo[0] == 'Show' and len(todo) == 2:
        show_numbers(todo[1])
    elif todo[0] == 'Delete' and len(todo) == 2:
        delete_person(todo[1])
    elif todo[0] == 'Exit' and len(todo) == 1:
        print("Goodbye!")
        exit(0)
    else:
        print('Incorrect input! Please try again.')
