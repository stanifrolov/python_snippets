text = "affe";

def anti_vowel(text):
    text = str(text)
    text = text.replace("a", "")
    text = text.replace("A", "")
    text = text.replace("e", "")
    text = text.replace("E", "")
    text = text.replace("i", "")
    text = text.replace("I", "")
    text = text.replace("o", "")
    text = text.replace("O", "")
    text = text.replace("u", "")
    text = text.replace("U", "")
    return text


print anti_vowel(text)