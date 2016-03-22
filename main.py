from modules import text_statistics

text = input()
list = text_statistics.text_to_list(text)
print(list)
print(text_statistics.median_count_of_words(list))
print(text_statistics.average_count_of_words(list))
print(text_statistics.top_grams(list, 10, 2))