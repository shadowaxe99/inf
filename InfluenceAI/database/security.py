```python
from cryptography.fernet import Fernet
from InfluenceAI.backend.utils import DATABASE_URI

class DatabaseSecurity:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        cipher_text = self.cipher_suite.encrypt(data.encode())
        return cipher_text

    def decrypt_data(self, cipher_text):
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

    def secure_database_connection(self):
        encrypted_uri = self.encrypt_data(DATABASE_URI)
        return encrypted_uri

    def retrieve_database_connection(self, encrypted_uri):
        decrypted_uri = self.decrypt_data(encrypted_uri)
        return decrypted_uri
```