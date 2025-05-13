import hashlib
from typing import Union

def get_md5(s: str) -> str:
    """Get md5 string
    
    Args:
        s (str): The string.
    """
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

def get_token(now_timestamp: Union[int, float], api_key: str) -> str:
    """Generate authentication token for API requests.
    
    Args:
        now_timestamp: Current timestamp
        api_key: API key for authentication
        
    Returns:
        Generated authentication token
    """
    return get_md5(str(now_timestamp) + "" + get_md5(api_key))