# Написать функцию с изменяемым числом входных параметров

def check_params(number: int, *args: int, name=None, **kwargs: dict):
    """
    This functions makes dictionary based on arguments
    """
    arguments_dictionary = {"mandatory_position_argument": number,
                            "additional_position_arguments": args,
                            "mandatory_named_argument": {"name": name},
                            "additional_named_arguments": kwargs}
    return arguments_dictionary


result = check_params(1, 2, 3, name='test', surname='test2',
                      some='something')
print(result)
