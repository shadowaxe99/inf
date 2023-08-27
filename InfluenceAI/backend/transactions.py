```python
import stripe
from models import TransactionSchema
from utils import DATABASE_URI

stripe.api_key = API_KEYS['STRIPE']

def process_payment(transaction):
    try:
        customer = stripe.Customer.create(
            email=transaction['email'],
            source=transaction['token']
        )

        charge = stripe.Charge.create(
            customer=customer.id,
            amount=transaction['amount'],
            currency='usd',
            description=transaction['description']
        )

        save_transaction(transaction, charge.id)

        return charge

    except Exception as e:
        return str(e)

def save_transaction(transaction, charge_id):
    transaction_db = TransactionSchema(charge_id=charge_id, **transaction)
    transaction_db.save_to_db(DATABASE_URI)

def get_transactions():
    return TransactionSchema.get_all(DATABASE_URI)
```