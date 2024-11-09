from openai import OpenAI

client = OpenAI(base_url='http://localhost:1234/v1', api_key='not-needed')
file4 = open("C:/Users/oleg2/PycharmProjects/aitest/text.txt", encoding='utf-8').read()

import re
from docx import Document
import PyPDF2

def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)
def read_pdf(file_path):
    pdftext = ''
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            pdftext += page.extract_text()
    return pdftext
def find_sentence_4(file_path, keywordsall):
    try:

        if file_path.endswith('.docx'):
            text = read_docx(file_path).lower()
        elif file_path.endswith('.pdf'):
            text= read_pdf(file_path)
        else:
            raise ValueError("Unsupported file format")

        # Разделение текста на предложения с использованием регулярных выражений
        sentences = re.split(r'(?<=[.!?])\s+', text)

        for sentence in sentences:
            if all(any(keyword in sentence for keyword in keywords) for keywords in keywordsall):
                return sentence

        return " "
    except FileNotFoundError:
        print("Файл не найден.")
        return None


file_path2 = "C:/Users/oleg2/Downloads/Проект контракта.pdf"
file_path1 = "C:/Users/oleg2/Downloads/ТЗ  Сценическое покрытие    (1).docx"

keywordsall = [['поставки', 'дней'], ['поставка', 'дней'],['доставка','дней']]



result_sentence = find_sentence_4(file_path1, keywordsall)
result_sentence_pdf= find_sentence_4(file_path2, keywordsall)

data="1 - 200 дней"
completion = client.chat.completions.create(
 model="mathstral-7b-v0.1",
 messages=[
    {"role": "system", "content": "Checker"},
    {"role": "user", "content": file4+''+data + '/'+result_sentence}
  ]
)
c = completion.choices[0].message.content
completion1 = client.chat.completions.create(
 model="mathstral-7b-v0.1",
 messages=[
    {"role": "system", "content": "Checker"},
    {"role": "user", "content": file4+" "+data+' / '+result_sentence_pdf}
  ]
)
print(c + completion1.choices[0].message.content)
