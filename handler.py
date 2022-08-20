import modules, utils, discord,threading

from utils import colors, messages

""" Command handeling for FlowGen """

def stard():
    amount = input(f"<{colors.blue}/{colors.white}> Threads: ")
    for i in range(int(amount)):
        threading.Thread(target=discord.generate).start()

def commands():

    try:

        utils.clear_with_banner()

        try:

            user_data = input(f"| {colors.blue}{colors.bold}Console{colors.unbold}{colors.white} |: ")

            if 'clear' in user_data.lower():
                utils.clear_with_banner()

            elif 'info' in user_data.lower():
                utils.basic_help()

            elif 'modules' in user_data.lower():
                utils.modules_show()
                
            elif '1' in user_data.lower():
                stard()
        
            elif 'exit' in user_data.lower() or 'quit' in user_data.lower():
                exit(f"\n{messages.title} See you another great time. ;')\n")

        except KeyboardInterrupt:
            print(f"\n{messages.title} Failed..- Read modules again!\n")

    except KeyboardInterrupt:
        exit()