def earth():
    x = "Bangladesh"
    y = "Barbados"
    
    result1 = x < y
    result2 = y < x
    
    return [
        f"The result of {x} comes first in the dictionary than {y} is {result1}.",
        f"The result of {y} comes first in the dictionary than {x} is {result2}."
    ]

if __name__ == "__main__":
    for line in earth():
        print(line)
