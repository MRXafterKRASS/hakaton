from openai import OpenAI
import re
import PyPDF2
client = OpenAI(base_url='http://localhost:1234/v1', api_key='not-needed')
file4 = open("C:/Users/oleg2/PycharmProjects/aitest/text.txt", encoding='utf-8').read()

# Открытие PDF файла
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        pdftext = ''
        for page in reader.pages:
            pdftext += page.extract_text()
    return pdftext
def find_sentence_4(file_path, keywordsall):
    try:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read().lower()

                # Разделение текста на предложения с использованием регулярных выражений
                sentences = re.split(r'(?<=[.!?])\s+', text)

                for sentence in sentences:
                    if all(any(keyword in sentence for keyword in keywords) for keywords in keywordsall):
                        return sentence

            return " "
        except UnicodeDecodeError:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                pdftext = ''
                for page in reader.pages:
                    pdftext += page.extract_text()
                text = pdftext.lower()

                # Разделение текста на предложения с использованием регулярных выражений
                sentences = re.split(r'(?<=[.!?])\s+', text)

                for sentence in sentences:
                    if all(any(keyword in sentence for keyword in keywords) for keywords in keywordsall):
                        return sentence
    except FileNotFoundError:
        print("Файл не найден.")
        return None


file_path = "C:/Users/oleg2/PycharmProjects/aitest/testtxt.txt"
keywordsall = [['поставки', 'дней'], ['поставка', 'дней'],['доставка','дней']]



result_sentence = find_sentence_4(file_path, keywordsall)
result_sentence_pdf= find_sentence_4("pdf\huy.pdf", keywordsall)

completion = client.chat.completions.create(
 model="mathstral-7b-v0.1",
 messages=[
    {"role": "system", "content": "Checker"},
    {"role": "user", "content": file4+'1 - 15 дней / '+result_sentence}
  ]
)
c = completion.choices[0].message.content
completion1 = client.chat.completions.create(
 model="mathstral-7b-v0.1",
 messages=[
    {"role": "system", "content": "Checker"},
    {"role": "user", "content": file4+' 1 - 15 дней / '+result_sentence_pdf}
  ]
)
print(c == completion1.choices[0].message.content)