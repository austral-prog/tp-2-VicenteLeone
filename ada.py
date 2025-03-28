def format_names(first_name: str, last_name: str) -> list:
    """
    Given a first name and a last name, return a list with the formatted names in different styles.
    """
    return [
        f"{first_name.lower()} {last_name.lower()}",
        f"{first_name.capitalize()} {last_name.capitalize()}",
        f"{first_name.upper()} {last_name.upper()}",
        f"\t{first_name.lower()} {last_name.lower()}"
    ]


if __name__ == "__main__":
    first_name = "AdA"
    last_name = "LoVeLAce"
    for line in format_names(first_name, last_name):
        print(line)
