# Banking System

This is a simple Python program that simulates a basic banking system. Users can deposit money, withdraw money, and view their account balance. All transactions are logged in a "transactions.txt" file.

**Demo:** [View the Demo on Google Colab](https://colab.research.google.com/drive/16Ay-RMIagrjMXZQAYAq20kZrFnW1EOiI?usp=sharing)

## Table of Contents

- [Classes](#classes)
- [Sample Usage](#sample-usage)

## Classes

### Banking

- The `Banking` class represents a basic bank account.
- It has the following methods:
  - `__init__(self, amount)`: Initializes a new bank account with the given initial amount and creates a "transactions.txt" file to log transactions.
  - `current_amount(self)`: Prints the current balance.
  - `deposit(self, deposit)`: Deposits the specified amount into the account and logs the transaction.
  - `withdraw(self, withdraw)`: Withdraws the specified amount from the account if sufficient funds are available and logs the transaction.

### MyBank

- The `MyBank` class inherits from the `Banking` class.
- It is used to create instances of bank accounts with additional functionality.

## Sample Usage

Here's an example of how to use the banking system:

1. Create a bank account with an initial balance (in the code it's set to $1000).

```python
acc = MyBank(1000)
```

2. Follow the on-screen prompts to deposit, withdraw, or exit the banking system.
