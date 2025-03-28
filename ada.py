def ada():
    first_name = "AdA"
    last_name = "LoVeLAce"
    return [
        f"{first_name.lower()} {last_name.lower()}",
        f"{first_name.capitalize()} {last_name.capitalize()}",
        f"{first_name.upper()} {last_name.upper()}",
        f"\t{first_name.lower()} {last_name.lower()}"
    ]

if __name__ == "__main__":
    for line in ada():
        print(line)
