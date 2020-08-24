import hashlib


def hashmake(file_name):
    with open(file_name) as f:
        for line in f:
            hash_return = hashlib.md5(line.encode(encoding="utf-8")).hexdigest()
            yield hash_return


for item in hashmake('result.txt'):
    print(item)
