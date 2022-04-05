def cast(string_list) -> str:

    kebab_casted = []  # List to store formatted words

    for index, word in enumerate(string_list):
        if word == len(word) * "-":  # Omit the word if it contains only dashes
            continue
        elif word.startswith("-") or word.endswith("-"):
            kebab_casted.append(word.lower().strip("-"))  # Remove leading/trailing dashes if they are present
        else:
            kebab_casted.append(word.lower())

    return "-".join(kebab_casted)
