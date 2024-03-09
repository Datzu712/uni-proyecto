def gen_inputs_to_dict(structure_reference):
    new_structure = {}

    for attribute in structure_reference.__annotations__.keys():
        question = getattr(structure_reference, attribute)
        user_input = input(f'Digite el {question}: ')

        new_structure[attribute] = user_input

    return new_structure
