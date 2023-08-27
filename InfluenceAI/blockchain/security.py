```python
from web3 import Web3
from eth_account.messages import encode_defunct

class BlockchainSecurity:
    def __init__(self, private_key, blockchain_address):
        self.private_key = private_key
        self.blockchain_address = blockchain_address
        self.web3 = Web3(Web3.HTTPProvider(self.blockchain_address))

    def sign_transaction(self, transaction):
        signed_txn = self.web3.eth.account.sign_transaction(transaction, self.private_key)
        return signed_txn

    def verify_signature(self, message, signature):
        message_hash = encode_defunct(text=message)
        signer = self.web3.eth.account.recover_message(message_hash, signature=signature)
        return signer

    def encrypt_message(self, message, public_key):
        encrypted_message = self.web3.eth.account.encrypt(public_key, message)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = self.web3.eth.account.decrypt(encrypted_message, self.private_key)
        return decrypted_message
```