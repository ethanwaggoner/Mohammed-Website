import re

def is_spam(*args):
    email_regex = r'(?i)\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    url_regex = (
        r'(?i)\b((?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#/%=~_|$?!:,.])'
        r'+(?:\([-A-Z0-9+&@#/%=~_|$?!:,.]*\)|[A-Z0-9+&@#/%=~_|$])'
    )

    for content in args:
        if content and (re.search(email_regex, content) or re.search(url_regex, content)):
            return True
    return False
