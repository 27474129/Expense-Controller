def convert_fields_for_update(fields: dict, updatable_fields: list) -> str:
    """Convert fields from dict.

    Example:
        fields: {"name": "some_name", "current_amount": 25}
        result: "name = 'some_name', current_amount = 25"

    This is required to use fields in SQL query in SET block during update request
    """

    result = ''
    for field in fields:
        if field in updatable_fields:
            result += f"{field} = "

            if type(fields[field]) is str:
                result += f"'{fields[field]}', "
            else:
                result += f'{fields[field]}, '

    # Return result without last two symbols (",", "space")
    return result[:-2]
