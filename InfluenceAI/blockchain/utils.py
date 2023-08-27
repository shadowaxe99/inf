```python
from web3 import Web3

# Connect to Ethereum blockchain
web3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_ADDRESS))

def create_contract(contract_interface):
    """
    Create a new smart contract.
    """
    contract = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    return contract

def deploy_contract(contract, arguments, account):
    """
    Deploy a smart contract.
    """
    tx_hash = contract.constructor(*arguments).transact({'from': account})
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt

def interact_with_contract(contract_address, contract_interface, function_name, arguments, account):
    """
    Interact with a deployed smart contract.
    """
    contract = web3.eth.contract(address=contract_address, abi=contract_interface['abi'])
    tx_hash = getattr(contract.functions, function_name)(*arguments).transact({'from': account})
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt

def get_contract_events(contract_address, contract_interface, event_name):
    """
    Get events from a deployed smart contract.
    """
    contract = web3.eth.contract(address=contract_address, abi=contract_interface['abi'])
    events = contract.events[event_name].get_all_entries()
    return events
```