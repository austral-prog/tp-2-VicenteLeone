def format_names(first_name: str, last_name: str):
    # Convertir todo a minúsculas
    lower_case = f"{first_name.lower()} {last_name.lower()}"
    
    # Convertir a formato título (primera letra en mayúscula)
    title_case = f"{first_name.capitalize()} {last_name.capitalize()}"
    
    # Convertir todo a mayúsculas
    upper_case = f"{first_name.upper()} {last_name.upper()}"
    
    # Agregar tabulación antes de la versión en minúsculas
    tabbed_lower_case = f"\t{lower_case}"
    
    # Imprimir los resultados
    print(lower_case)
    print(title_case)
    print(upper_case)
    print(tabbed_lower_case)

# Ejemplo de uso
first_name = "AdA"
last_name = "LoVeLAce"
format_names(first_name, last_name)
