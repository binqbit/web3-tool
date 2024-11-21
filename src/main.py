import os
import pyperclip
import dotenv

dotenv.load_dotenv()

import ethereum


def get_param(name):
    for i in range(len(os.sys.argv)):
        if os.sys.argv[i] == name:
            value = ""
            for j in range(i + 1, len(os.sys.argv)):
                if os.sys.argv[j].startswith("--"):
                    break
                value += os.sys.argv[j] + " "
            value = value.strip()
            if value:
                return value
    return None

cmd = get_param("--cmd")
network = get_param("--network")
private_key = get_param("--private-key")
data = pyperclip.paste().strip()

if cmd == "sign_message":
    signed_message = ethereum.sign_message(data, private_key)
    pyperclip.copy(signed_message)

elif cmd == "sign_tx":
    signed_tx = ethereum.sign_tx(data, private_key, network)
    pyperclip.copy(signed_tx)

elif cmd == "send_tx":
    hash = ethereum.send_tx(data, private_key, network)
    pyperclip.copy(hash)

elif cmd == "call_tx":
    result = ethereum.call_tx(data, network)
    pyperclip.copy(result)

else:
    print("Invalid Command")
    os.system(f"pause")