from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


password = "kjhkjhkhkjhj"

hash = context.hash(password)
print(hash)

password2 = "kjhkjhkhkjh1"
# verify
result = context.verify(password2, hash)
print(result)