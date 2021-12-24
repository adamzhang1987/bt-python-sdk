from hashlib import md5

def get_md5(s):
    m = md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

def get_token(now_timestamp, api_key):
    return get_md5(str(now_timestamp) + "" + get_md5(api_key))