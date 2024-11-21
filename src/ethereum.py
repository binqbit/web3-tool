import json
import os
from web3 import Web3
from eth_account.messages import encode_defunct

ETH_PRIVATE_KEY = os.getenv("ETH_PRIVATE_KEY")
ETH_LOCALNET_RPC_URL = os.getenv("ETH_LOCALNET_RPC_URL", "http://localhost:8545")
ETH_TESTNET_RPC_URL = os.getenv("ETH_TESTNET_RPC_URL")
PRIVATE_KEYS = {}

private_keys = os.getenv("PRIVATE_KEYS")
if private_keys:
    private_keys = private_keys.split(",")
    for private_key in private_keys:
        private_key = private_key.split(":")
        if len(private_key) == 2:
            PRIVATE_KEYS[private_key[0].strip()] = private_key[1].strip()

def get_network(network = None):
    if network:
        if network == 'localnet':
            return Web3(Web3.HTTPProvider(ETH_LOCALNET_RPC_URL))
        elif network == 'testnet':
            return Web3(Web3.HTTPProvider(ETH_TESTNET_RPC_URL))
        else:
            return Web3(Web3.HTTPProvider(network))
    return Web3(Web3.HTTPProvider(ETH_LOCALNET_RPC_URL))

def get_private_key(key = None):
    if key:
        key_from_name = PRIVATE_KEYS.get(key)
        if key_from_name:
            return key_from_name
        else:
            return key
    return ETH_PRIVATE_KEY

def sign_message(data, key=None):
    web3 = get_network()
    private_key = get_private_key(key)
    try:
        message = encode_defunct(text=data)
        signed_message = web3.eth.account.sign_message(message, private_key=private_key)
        return signed_message.signature.hex()
    except Exception as e:
        print(f"Error Signing Message: {str(e)}")
        print(f"Message: {data}")
        os.system(f"pause")
        return None

def sign_tx(tx, key=None, network = None):
    private_key = get_private_key(key)
    web3 = get_network(network)
    try:
        try:
            tx = json.loads(tx)

            if 'nonce' not in tx:
                tx['nonce'] = web3.eth.get_transaction_count(web3.eth.coinbase)

            if 'gas' not in tx:
                tx['gas'] = 2000000

            if 'gasPrice' not in tx:
                tx['gasPrice'] = web3.eth.gas_price

            signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
        except:
            signed_tx = web3.eth.account.sign_transaction({'rawTransaction': tx}, private_key=private_key)

        return signed_tx.rawTransaction.hex()
    except Exception as e:
        print(f"Error Signing Transaction: {str(e)}")
        print(f"Transaction: {tx}")
        os.system(f"pause")
        return None

def send_tx(tx, key=None, network = None):
    private_key = get_private_key(key)
    web3 = get_network(network)
    try:
        try:
            tx = json.loads(tx)

            if 'nonce' not in tx:
                tx['nonce'] = web3.eth.get_transaction_count(web3.eth.coinbase)

            if 'gas' not in tx:
                tx['gas'] = 2000000

            if 'gasPrice' not in tx:
                tx['gasPrice'] = web3.eth.gas_price

            signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
        except:
            signed_tx = web3.eth.account.sign_transaction({'rawTransaction': tx}, private_key=private_key)

        hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return hash.hex()
    except Exception as e:
        print(f"Error Sending Transaction: {str(e)}")
        print(f"Transaction: {tx}")
        os.system(f"pause")
        return None

def call_tx(tx, network = None):
    web3 = get_network(network)
    try:
        return web3.eth.call(tx)
    except Exception as e:
        print(f"Error Calling Transaction: {str(e)}")
        print(f"Transaction: {tx}")
        os.system(f"pause")
        return None