def sanitize_message(message,  command_name,prefix='-'):
    return message.replace(prefix + command_name, '')
