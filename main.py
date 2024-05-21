import requests, os
from colorama import Fore

os.system("cls")

def send_message(webhook, message):
    payload = {
        'content': message,
        'username': "YOUR USERNAME",
        'avatar_url': "YOUR WEBHOOK AVATER"
    }
    response = requests.post(webhook, json=payload)
    if response.status_code == 204:
        print(f"{Fore.LIGHTRED_EX}SUCCSES {Fore.LIGHTWHITE_EX}Message Send! -> {Fore.LIGHTBLACK_EX}({response.status_code})")
    else:
        print(f"{Fore.RED}ERROR {Fore.LIGHTWHITE_EX}FAILED! -> {Fore.LIGHTBLACK_EX}({response.status_code})")

def main():
    print(f'''{Fore.RED} 
██╗   ███╗███████╗ ██████╗ ███████╗ ██████╗ 
████╗ ████║██╔════╝██╔═████╗╚════██║██╔═████╗
██╔████╔██║█████╗  ██║██╔██║    ██╔╝██║██╔██║
██║╚██╔╝██║██╔══╝  ████╔╝███║   ██╔╝ ████╔╝██║
██║ ╚═╝ ██║███████╗╚██████╔╝   ██║  ╚██████╔╝
╚═╝     ╚═╝╚══════╝ ╚═════╝    ╚═╝   ╚═════╝ 
{Fore.WHITE}------------------------------------------------------------------------------------
{Fore.RED}gg./me070 |  gg./me070 |  gg./me070 |  gg./me070 |  gg./me070
{Fore.WHITE}------------------------------------------------------------------------------------
    ''')
    webhook = input(f"{Fore.RESET}[{Fore.WHITE}>{Fore.RESET}] Enter Webhook: ")
    message = input(f"{Fore.RESET}[{Fore.WHITE}>{Fore.RESET}] Enter Message To Spam: ")
    while True:
        send_message(webhook, message)

main()
