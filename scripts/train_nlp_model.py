# train_nlp_model.py

import torch
from transformers import BertForSequenceClassification, Trainer, TrainingArguments, BertTokenizer
from datasets import load_dataset

def load_data(dataset_name="imdb"):
    dataset = load_dataset(dataset_name)
    return dataset['train'], dataset['test']

def preprocess_data(tokenizer, dataset):
    def tokenize_function(examples):
        return tokenizer(examples['text'], padding="max_length", truncation=True)

    return dataset.map(tokenize_function, batched=True)

def train_model(train_dataset, eval_dataset, model_name="bert-base-uncased", output_dir="./models"):
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

    train_dataset = preprocess_data(tokenizer, train_dataset)
    eval_dataset = preprocess_data(tokenizer, eval_dataset)

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
        evaluation_strategy="epoch",
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )

    trainer.train()
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)

if __name__ == "__main__":
    train_dataset, eval_dataset = load_data()
    train_model(train_dataset, eval_dataset)
    print("Model training complete. The fine-tuned model has been saved.")
