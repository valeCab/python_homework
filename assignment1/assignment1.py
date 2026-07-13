# Task 1:
def hello():
    return "Hello!"
print(hello())

# Task 2:
def greet(name):
    return f"Hello, {name}!"
print(greet("Vale"))

#Task 3:
def calc(num1, num2, operation="multiply"):
    try: 
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2 
        elif operation == "divide":
            return num1 / num2
        elif operation == "modulo":
            return num1 % num2
        elif operation == "int_divide":
            return num1 // num2
        elif operation == "power":
            return num1 ** num2
        else: 
            return "invalid"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
#Task 4: 
def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        if data_type == "int":
            return int(float(value))
        elif data_type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    
#Task 5: 
def grade(*args):
    try: 
        average = sum(args) / len(args)
        if average >= 90: 
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."
    
#Task 6:
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result
    
#Task 7:
def student_scores(option, **kwargs):
    if option == "best":
        return max(kwargs, key=kwargs.get) 
    elif option == "mean":
        return sum(kwargs.values()) / len(kwargs)
    
#Task 8:
def titleize(text):
    words = text.split()
    if len(words) == 0:
        return ""
    little_words =["a", "on", "an", "the", "of", "and", "is", "in"]
    result = []

    for i, word in enumerate(words): #not sure
        

        if i == 0 or i == len(words) -1:
            result.append(word.capitalize())
        elif word.lower() in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return " ".join(result)

#Task 9:
# Task 9:
def hangman(secret, guess): 
    result = ""

    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"

    return result



#Task 10:
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result_words = []

    for word in words:
        if word[0] in vowels:
            new_word = word + "ay"

        else:
            vowel_index = 0

            while vowel_index < len(word):
                if word[vowel_index] in vowels:
                    if word[vowel_index-1:vowel_index+1] == "qu":
                        vowel_index += 1
                    break
                vowel_index += 1

            consonants = word[:vowel_index]
            rest_of_word = word[vowel_index:]
            new_word = rest_of_word + consonants + "ay"

        result_words.append(new_word)

    return " ".join(result_words)