import re

def text_to_list(text):
    temp = re.sub(r'[!?]', '.', text)

    result = []
    for sentence in re.split(r'\.', temp):
        consist = []
        sentence = re.sub(r'\,|\"|\-|\'|\;', ' ', sentence)

        for word in re.split(' ', sentence):
            if word != '':
                consist.append(word)

        if consist != []:
            result.append(consist)

    return result


def average_count_of_words(list):
    return sum(len(item) for item in list) / len(list)

def median_count_of_words(list):
    list = sorted(list)
    return 0