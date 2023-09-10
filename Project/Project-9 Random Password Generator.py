import random
from string import punctuation, ascii_letters, digits
symbols = ascii_letters + digits + punctuation
scr = random.SystemRandom()
Password = "".join(scr.sample(symbols, 10))
print(Password)
