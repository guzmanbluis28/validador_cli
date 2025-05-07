import validators

def is_valid_email(email:str) -> bool:
    return bool(validators.email(email))

def is_valid_url(url: str) -> bool:
    return bool(validators.url(url))
