from hashlib import md5

def get_md5(s):
    """Get md5 string
    
    Args:
        s (str): The string.
    """
    m = md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

def get_token(now_timestamp, api_key):
    """Get the token for the request

    Args:
        now_timestamp (int): The timestamp.
        api_key (str): The api key.

    Returns:
        str: The token.
    """
    return get_md5(str(now_timestamp) + "" + get_md5(api_key))