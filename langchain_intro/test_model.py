
import pandas as pd
from sklearn.model_selection import train_test_split

# Загрузка данных
data = pd.read_csv('faq_data.csv')  # ваш файл с данными
questions = data['question'].tolist()
answers = data['answer'].tolist()# Разделение данных на обучающую и тестовую выборки
train_questions, test_questions, train_answers, test_answers = train_test_split(questions, answers, test_size=0.2, random_state=42)
from transformers import BertModel, BertForSequenceClassification, Trainer, TrainingArguments
import torch

# Загрузка токенизатора и модели
tokenizer = BertModel.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(set(answers)))# Токенизация данных
def tokenize_function(questions):    return tokenizer(questions, padding="max_length", truncation=True, max_length=128)
train_encodings = tokenize_function(train_questions)
test_encodings = tokenize_function(test_questions)
class FaqDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)#train_![image]()