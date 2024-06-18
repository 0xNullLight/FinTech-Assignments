# Cryptocurrency Wallet
################################################################################

# This file contains the Ethereum transaction functions that you have created throughout this module’s lessons.
# By using import statements, you will integrate this `crypto_wallet.py` Python script
# into the KryptoJobs2Go interface program that is found in the `krypto_jobs.py` file.

################################################################################
# Wallet
import os
import requests
from dotenv import load_dotenv

load_dotenv("sample.env")
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

################################################################################
# Wallet functionality

def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet Object
    wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.from_key(private)

    return account

def get_balance(w3, address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)

    # Convert Wei value to ether
    ether = w3.from_wei(wei_balance, "ether")

    # Return the value in ether
    return ether

def send_transaction(w3, account, to, wage):
    """Send an authorized transaction to the Ganache blockchain."""
    # Set a fallback gas price
    fallback_gas_price = 1000000000  # 1 Gwei

    # Convert eth amount to Wei
    value = w3.to_wei(wage, "ether")

    # Calculate gas estimate
    gasEstimate = w3.eth.estimate_gas(
        {"to": to, "from": account.address, "value": value}
    )

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": fallback_gas_price,
        "nonce": w3.eth.get_transaction_count(account.address),
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transactions
    return w3.eth.send_raw_transaction(signed_tx.rawTransaction)