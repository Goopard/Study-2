def select(*field_name: str):
    """This function creates a function which is used to select certain columns (defined in *field_name) from some
    table.

    :param field_name: Names of the columns that will be included in the resulting table.
    :type field_name: str.
    :returns function.
    """
    def selection(table: list) -> list:
        """This functions creates the selection from the table.

        :param table: Original table.
        :type table: list.
        :returns list -- The required selection.
        """
        res_table = []
        for line in table:
            res_line = {}
            for colon in line:
                if colon in field_name:
                    res_line[colon] = line[colon]
            res_table.append(res_line)
        return res_table
    return selection


def field_filter(field_name: str, possible_values: list):
    """This function creates a function which is used to create a filtered version of some table, viz. to select only
    the lines with the values from possible_values in the field field_name.

    :param field_name: Name of the field by which the table will be filtered.
    :type field_name: str.
    :param possible_values: Allowed values for the name of the field (field_name).
    :type possible_values: list
    :returns function.
    """
    def field_filterer(table: list) -> list:
        """This functions creates the filtered version of the table.

        :param table: Original table.
        :type table: list.
        :returns list -- The filtered version of the table.
        """
        res_table = []
        for line in table:
            if line[field_name] in possible_values:
                res_table.append(line)
        return res_table
    return field_filterer


def query(table: list, selection, *field_filterers) -> list:
    """This function embodies the query to the table, which returns filtered selection from the table.

    :param table: Original table.
    :type table: list.
    :param selection: Function which creates the selection from the table.
    :type selection: function.
    :param field_filterers: Functions that filter the table.
    :type field_filterers: function.
    :returns list.
    """
    res_table = table
    res_table = selection(res_table)
    for func in field_filterers:
        res_table = func(res_table)
    return res_table


friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
    {'name': 'Джон', 'gender': 'Мужской', 'sport': 'Волейбол', 'email': 'email2@email2.com'}
]
result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('gender', ['Мужской']),
    field_filter('sport', ['Волейбол', 'Баскетбол'])
)
print(result)
