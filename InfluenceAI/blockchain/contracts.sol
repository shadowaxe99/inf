```solidity
pragma solidity >=0.7.0 <0.9.0;

contract InfluenceAIContract {
    address public owner;
    mapping(address => uint256) public balances;

    struct Contract {
        address influencer;
        address brand;
        uint256 amount;
        bool completed;
    }

    Contract[] public contracts;

    event ContractCreated(uint256 contractId, address influencer, address brand, uint256 amount);
    event ContractCompleted(uint256 contractId);

    constructor() {
        owner = msg.sender;
    }

    function createContract(address influencer, address brand, uint256 amount) public {
        require(msg.sender == owner, "Only the owner can create contracts.");
        require(balances[brand] >= amount, "Brand does not have enough funds.");

        balances[brand] -= amount;

        contracts.push(Contract({
            influencer: influencer,
            brand: brand,
            amount: amount,
            completed: false
        }));

        emit ContractCreated(contracts.length - 1, influencer, brand, amount);
    }

    function completeContract(uint256 contractId) public {
        Contract storage contract = contracts[contractId];

        require(msg.sender == contract.brand, "Only the brand involved can complete the contract.");
        require(!contract.completed, "Contract has already been completed.");

        contract.completed = true;
        balances[contract.influencer] += contract.amount;

        emit ContractCompleted(contractId);
    }

    function depositFunds() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdrawFunds(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Not enough funds.");

        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }
}
```