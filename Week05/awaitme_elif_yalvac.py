def awaitme(func):
    """
    Herhangi bir fonksiyonu korutine dönüştüren dekoratör.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
