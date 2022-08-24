################################################
#
#   BTCMiner / bruteforcer / checker made by LizardX2 
#
#   contact for issues or improvements;
#
#   Telegram: @LizardX2 link: t.me/LizardX2
#
#################################################
from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hdwallet.utils import generate_mnemonic
from typing import Optional
from colorama import Fore
import json, requests, os, ctypes, os.path
from datetime import datetime
from time import sleep

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

if os.path.isfile('config.json'):
    pass
else:
    clear()
    print(f"{Fore.RED}The config.json file is missing or its not in the same path!{Fore.RESET}")
    exiting = input("")
    exit()

with open('config.json') as config_file:
    data = json.load(config_file)

    b_config_strenght = data["settings"]["bruteforcer"]["strenght"]
    b_config_language = data["settings"]["bruteforcer"]["language"]
    b_config_passphere = data["settings"]["bruteforcer"]["passphere"]

    c_config_file = data["settings"]["checker"]["filename"]

    config_failed = data["settings"]["general"]["failed"]
    config_success = data["settings"]["general"]["success"]
    config_address = data["settings"]["general"]["addresstype"]

    api_url = data["settings"]["general"]["api"]["api_url"]
    api_get_data = data["settings"]["general"]["api"]["api_get_data"]
    api_get_balance = data["settings"]["general"]["api"]["api_get_balance"]
    api_get_recieved = data["settings"]["general"]["api"]["api_get_recieved"]
    config_file.close()

def center(var:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2

    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

def ui():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW(f"BITCOIN BRUTEFORCER / CHECKER | Made by @LizardX2 on Telegram") 
    font = """
                ▄▄▄▄   ▄▄▄█████▓ ▄████▄    █████▒▒█████   ██▀███   ▄████▄  ▓█████  ██▀███  
                ▓█████▄ ▓  ██▒ ▓▒▒██▀ ▀█  ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒
                ▒██▒ ▄██▒ ▓██░ ▒░▒▓█    ▄ ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   ▓██ ░▄█ ▒
                ▒██░█▀  ░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄  
                ░▓█  ▀█▓  ▒██▒ ░ ▒ ▓███▀ ░░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒░██▓ ▒██▒
                ░▒▓███▀▒  ▒ ░░   ░ ░▒ ▒  ░ ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░
                ▒░▒   ░     ░      ░  ▒    ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░
                ░    ░   ░      ░         ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░     ░░   ░ 
                ░               ░ ░                 ░ ░     ░     ░ ░         ░  ░   ░     
                    ░          ░                                 ░                        """
    faded = ''
    red = 0
    for line in font.splitlines():
        faded += (f"\033[38;2;{red};10;230m{line}\033[0m\n")
        if not red == 255:
            red += 10
            if red > 110:
                red = 255
    print(center(faded))
    print(center(f'{Fore.LIGHTYELLOW_EX}\ngithub.com/LizardX2 Version 1.0 | Telegram: @LizardX2\n{Fore.RESET}'))

def errorfile():
    clear()
    print(f"{Fore.RED}[!] FATAL ERROR! A text file in the directory is missing, please make sure the files: {config_failed} | {config_success} | {c_config_file} are there, or are in the same path! {Fore.RESET}")
    print("\n\n\n\n\n\n\n\n")
    exiting = input(f"{Fore.LIGHTRED_EX}[!] Press enter to exit... {Fore.RESET}")
    exit()

ui()
settings = input(f"{Fore.YELLOW}[?]{Fore.RESET} {Fore.LIGHTWHITE_EX}Make a choice between Checker and Bruteforcer [C] - [B] > {Fore.RESET}")

def main():
    if settings.lower() == "b":
        if os.path.isfile(config_failed) or os.path.isfile(config_success) or os.path.isfile(c_config_file):
            pass
        else:
            errorfile()
        print("\n")
        print(f"{Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTWHITE_EX}Saving failed seeds on >> {Fore.LIGHTYELLOW_EX}{config_failed}{Fore.RESET}")
        print(f"{Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTWHITE_EX}Saving successful seeds on >> {Fore.LIGHTYELLOW_EX}{config_success}{Fore.RESET}")
        print(f"{Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTWHITE_EX}Type of addresses >> {Fore.LIGHTYELLOW_EX}{config_address}{Fore.RESET}")
        print(f"{Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTWHITE_EX}Language >> {Fore.LIGHTYELLOW_EX}{b_config_language}{Fore.RESET}")
        print(f"{Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTWHITE_EX}Strenght >> {Fore.LIGHTYELLOW_EX}{b_config_strenght}{Fore.RESET}")
        sleep(2)
        print("\n")
        STRENGTH: int = b_config_strenght
        LANGUAGE: str = b_config_language
        PASSPHRASE: Optional[str] = b_config_passphere
        s = requests.Session()
        while True:
            now_time = datetime.now()
            current = now_time.strftime("%H:%M:%S")
            MNEMONIC: str = generate_mnemonic(language=LANGUAGE, strength=STRENGTH)
            hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)
            hdwallet.from_mnemonic(mnemonic=MNEMONIC, language=LANGUAGE, passphrase=PASSPHRASE)
            btc_address = hdwallet.dumps()['addresses'][config_address]
            btc_wif = hdwallet.dumps()['wif']
            btc_seed = hdwallet.dumps()['mnemonic']
            btc_entropy = hdwallet.dumps()['entropy']
            btc_privatekey = hdwallet.dumps()['private_key']
            get_info = s.get(f"{api_url}/{btc_address}").json()
            balance = get_info[api_get_data][api_get_balance]
            all_time_balance = get_info[api_get_data][api_get_recieved]
            if str(balance) == "0" or str(all_time_balance) == "0":
                fail = open(config_failed, "a")
                fail.write(f"{btc_address} | {balance}$ | {all_time_balance}$ | {btc_seed} | {btc_privatekey} | {btc_entropy} | {btc_wif} \n")
                fail.close()
            elif str(balance) != "0" or str(all_time_balance) != "0":
                valid = open(config_success, "a")
                valid.write(f"{btc_address} | {balance}$ | {all_time_balance}$ | {btc_seed} | {btc_privatekey} |  {btc_entropy} | {btc_wif} \n")
                valid.close()
            print(f"{Fore.LIGHTBLACK_EX}[{current}]{Fore.RESET} {Fore.YELLOW}{btc_address}{Fore.RESET} {Fore.LIGHTBLACK_EX}|{Fore.RESET} {Fore.LIGHTGREEN_EX}BAL: {balance}${Fore.RESET} {Fore.LIGHTBLACK_EX}|{Fore.RESET} {Fore.LIGHTWHITE_EX}SEED: {btc_seed}{Fore.RESET} {Fore.LIGHTBLACK_EX}|{Fore.RESET} {Fore.LIGHTRED_EX}PRIV: {btc_privatekey}{Fore.RESET} {Fore.LIGHTBLACK_EX}| {Fore.RESET}{Fore.BLUE}{b_config_strenght}{Fore.RESET}")

    elif settings.lower() == "c":
        if os.path.isfile(config_failed) or os.path.isfile(config_success) or os.path.isfile(c_config_file):
            pass
        else:
            errorfile()
        print("\n")
        print(f"{Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTWHITE_EX}Saving failed seeds on >> {Fore.LIGHTYELLOW_EX}{config_failed}{Fore.RESET}")
        print(f"{Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTWHITE_EX}Saving successful seeds on >> {Fore.LIGHTYELLOW_EX}{config_success}{Fore.RESET}")
        print(f"{Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTWHITE_EX}Checking from file >> {Fore.LIGHTYELLOW_EX}{c_config_file}{Fore.RESET}")
        print(f"{Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTWHITE_EX}Type of address >> {Fore.LIGHTYELLOW_EX}{config_address}{Fore.RESET}")
        sleep(2)
        print("\n")
        with open(c_config_file) as f:
            data = f.read().splitlines()
            for custom_mnemonic in data:
                now_time = datetime.now()
                current = now_time.strftime("%H:%M:%S")
                hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)
                hdwallet.from_mnemonic(mnemonic=custom_mnemonic)
                btc_address = hdwallet.dumps()['addresses'][config_address]
                btc_wif = hdwallet.dumps()['wif']
                btc_seed = hdwallet.dumps()['mnemonic']
                btc_entropy = hdwallet.dumps()['entropy']
                btc_privatekey = hdwallet.dumps()['private_key']
                get_info = requests.get(f"{api_url}/{btc_address}").json()
                balance = get_info[api_get_data][api_get_balance]
                all_time_balance = get_info[api_get_data][api_get_recieved]
                if str(balance) == "0" or str(all_time_balance) == "0":
                    fail = open(config_failed, "a")
                    fail.write(f"{btc_address} | {balance}$ | {all_time_balance}$ | {btc_seed} | {btc_privatekey} | {btc_entropy} | {btc_wif} \n")
                    fail.close()
                elif str(balance) != "0" or str(all_time_balance) != "0":
                    valid = open(config_success, "a")
                    valid.write(f"{btc_address} | {balance}$ | {all_time_balance}$ | {btc_seed} | {btc_privatekey} |  {btc_entropy} | {btc_wif} \n")
                    valid.close()
                print(f"{Fore.LIGHTBLACK_EX}[{current}]{Fore.RESET} {Fore.YELLOW}{btc_address}{Fore.RESET} {Fore.LIGHTBLACK_EX}|{Fore.RESET} {Fore.LIGHTGREEN_EX}BAL: {balance}${Fore.RESET} {Fore.LIGHTBLACK_EX}|{Fore.RESET} {Fore.LIGHTWHITE_EX}SEED: {btc_seed}{Fore.RESET} {Fore.LIGHTBLACK_EX}|{Fore.RESET} {Fore.LIGHTRED_EX}PRIV: {btc_privatekey}{Fore.RESET} {Fore.LIGHTBLACK_EX}| {Fore.RESET}{Fore.BLUE}{b_config_strenght}{Fore.RESET}")
    elif settings.lower() != "c" or settings.lower() != "b":
        print(f"{Fore.RED}[x] The choice must be between C or B! Aborting...{Fore.RESET}")
        exiting = input("")
        exit()
    else:
        print(f"{Fore.GREEN}Well thats weird, contact @LizardX2 on Telegram for help{Fore.RESET}")
        exiting = input("")
        exit()
main()
