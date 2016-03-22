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


def reps_of_words(list):
    reps = dict()

    for sentence in list:
        for word in sentence:
            if word in reps.keys():
                reps[word] += 1
            else:
                reps.update({word: 1})

    return reps


def average_count_of_words(list):
    return sum(len(item) for item in list) / len(list)


def median_count_of_words(list):
    list = sorted(list, key=lambda item: len(item))

    if len(list) % 2 == 1:
        mid = int(len(list)/2)
        return float(len(list[mid]))
    else:
        mid = int(len(list)/2)
        return (len(list[mid]) + len(list[mid-1]))/2


def top_grams(list, k=10, n=4):
    grams = dict()

    for sentence in list:
        for word in sentence:
            for nGram in [word[i: i+n] for i in range(len(word) - n + 1)]:
                if nGram in grams.keys():
                    grams[nGram] += 1
                else:
                    grams.update({nGram: 1})

    sorted_grams = sorted(grams.items(),key=lambda item: item[1], reverse=True)

    if len(sorted_grams) > k:
        return [temp for temp in sorted_grams[:k]]
    else:
        return [temp for temp in sorted_grams]
