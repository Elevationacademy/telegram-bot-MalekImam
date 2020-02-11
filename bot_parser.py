from bot_help import  dict_commands


def parse_message(msg):
    try:
        command = msg.split()[0][1:]
        if command in dict_commands:
            args = ""
            if len(msg.split()) > 1:
                args = msg.split()[1]
            return dict_commands[command](args)
        else:
            return "Use /help command."
    except:
        return "Error"


