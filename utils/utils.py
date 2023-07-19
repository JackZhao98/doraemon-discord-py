def sanitize_message(message,  command_name, prefix='-', aliases=[]):
    """Remove command prefix and command name from message"""
    if message.startswith(prefix + command_name):
        return message.replace(prefix + command_name, '').strip()
    else:
        for alias in aliases:
            if message.startswith(prefix + alias):
                return message.replace(prefix + alias, '').strip()
    return message.strip()
