# Web3 Tool

### Description
A simple and convenient tool for testing Web3 functions such as signature of data, transactions, execution, and so on.

### Install
```bash
pip install -r requirements.txt
```

### Parameters
- `--admin`: This parameter is needed to provide access to the correct work if it is launched through the left software. `Optional`
- `--cmd`: The command that will be executed. `Required`
    - `sign_message`: Sign the message.
    - `sign_tx`: Sign the transaction.
    - `send_tx`: Send the transaction.
    - `call_tx`: Call the transaction and get the result.
- `--network`: The network to which the command will be executed. `Optional`
- `--private-key`: The private key that will be used to sign the data. `Optional`

### Environment Variables
- `ETH_PRIVATE_KEY`: The default private key that will be used to sign the data.
- `ETH_LOCALNET_RPC_URL`: The local network RPC URL.
- `ETH_TESTNET_RPC_URL`: The test network RPC URL.
- `PRIVATE_KEYS`: A list of private keys that will be used to sign the data.

### Keyring
- Create `.env` file in the root directory.
- Add the following lines to the file:
    ```env
    PRIVATE_KEYS = private_key_name1:private_key1, private_key_name1:private_key1
    ```

### Example Of Use
- Sign the data:
    ```bash
    web3-tool --cmd sign_message --private-key your_private_key
    ```

- Send the transaction:
    ```bash
    web3-tool --cmd send_tx --private-key your_private_key
    ```

### How To Use
- Install the requirements.
- Add this path to the system PATH variable.
- Create a new shortcut on your desktop.
- Open the shortcut properties.
- Add the command to the target field: `web3-tool --cmd sign_message --private-key private_key_name`.
- Add keys shortcuts to run this file.
- When you call this program, it automatically signs or performs the transaction that is in the exchange buffer, and there it saves the result.