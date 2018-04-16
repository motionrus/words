
#
# Автор: Тютин Руслан
# Тестовое задание
#


def sorted_words(key, dict_words):
    """
    Возвращает список совпадений по наибольшему количеству повторений слова в словаре
    """
    list_words = (sorted(dict_words.items(), key=lambda t: t[0]))
    sorted_count = (sorted(list_words, reverse=True, key=lambda t: t[1]))
    match_words = []
    for id_word in sorted_count:
        if id_word[0].startswith(key):
            match_words.append(id_word[0])
    return match_words[:10]


def validate_words(list_words):
    """
    Проверяет что список состоит из 15 символов, число входит в диапазон 1 <= M <= 15000 и слова не повторяются
    Возвращает словарь или ошибку в string
    """
    for id_word in range(len(list_words)):
        try:
            m = int(list_words[id_word][1])
        except ValueError:
            return "Не удалось преобразовать число в int"
        if not (1 <= m <= 15000):
            return "Число не входит в диапазон 1 <= M <= 15000"
        list_words[id_word][1] = int(list_words[id_word][1])
        if not (len(list_words[id_word][0]) <= 15 and list_words[id_word][0].isalpha()):
            return "Длина слова больше 15 симовлов или слово не состоит из символов"
        if len(list_words) != len(set([x[0] for x in list_words])):
            return "Слова не должны повторяться"

    return list_words


def input_data():
    """
    Возвращает чистые данные словаря {слово: количество совпадений}
    """
    count_word = input()
    if 1 <= int(count_word) <= 10**5:
        list_words = []
        for id_word in range(int(count_word)):
            word = (input()).split()
            list_words.append(word)
        if type(validate_words(list_words)) == str:
            print("Ошибка: {}".format(validate_words(list_words)))
            return
        return dict(list_words)


def input_part_word():
    """
    Возвращает список частей слов если они не больше 15 и состоят из символов
    """
    count_word = input()
    if 1 <= int(count_word) <= 15000:
        words = []
        for id_word in range(int(count_word)):
            word = input()
            if not (word.isalpha() and len(word) <= 15):
                print("Ошибка: Слово не состоит из символов или больше 15")
                return
            words.append(word)
        return words


if __name__ == "__main__":
    data = input_data()
    part_word = input_part_word()
    if part_word and data:
        for result in range(len(part_word)):
            print()
            match_result = (sorted_words(part_word[result], data))
            for match in match_result:
                print(match)
