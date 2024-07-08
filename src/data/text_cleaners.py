import re

class TextCleaner:
    def __init__(self, texts):
        self.texts = texts

    def remove_emojis(self):
        self.texts = [re.sub(r'\W+', ' ', text) for text in self.texts]

    def remove_usernames(self):
        self.texts = [re.sub(r'@\w+', '<username>', text) for text in self.texts]

    def remove_phone_numbers(self):
        self.texts = [re.sub(r'994\d{9}', '<phone number>', text) for text in self.texts]

    def remove_private_info(self):
        self.texts = [
            re.sub(r'\d{16}', '<card number>', text) for text in self.texts
        ]
        self.texts = [re.sub(r'\b(AA|AZE)\w{7}', '<identification card>', text) for text in self.texts]

    def clean_text(self):
        self.remove_emojis()
        self.remove_usernames()
        self.remove_phone_numbers()
        self.remove_private_info()
        return self.texts
