import re

def find_sentence_4(file_path, keywordsall):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()

            # Разделение текста на предложения с использованием регулярных выражений
            sentences = re.split(r'(?<=[.!?])\s+', text)

            for sentence in sentences:
                if all(any(keyword in sentence for keyword in keywords) for keywords in keywordsall):
                    return sentence

        return None
    except FileNotFoundError:
        print("Файл не найден.")
        return None

# Пример использования
file_path = "C:/Users/oleg2/PycharmProjects/aitest/testtxt.txt"
keywordsall = [['поставки', 'дней'], ['поставка', 'дней'],['доставка','дней']]

result_sentence = find_sentence_4(file_path, keywordsall)

if result_sentence:
    print("Найденное предложение:")
    print(result_sentence)
else:
    print("Предложение с ключевыми словами не найдено.")