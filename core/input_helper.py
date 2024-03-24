def gen_input_to_list(questions: list) -> list:
    # Lista de inputs del usuario
    data = []
    for question in questions:
        user_input = input(f'{question}\n')

        data.append(user_input)

    return data
