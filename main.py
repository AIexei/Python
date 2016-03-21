from modules.text_statistics import text_to_list, average_count_of_words

text = input()
list = text_to_list(text)
print(list)
print(average_count_of_words(list))
