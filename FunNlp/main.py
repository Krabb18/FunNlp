from tokenizer import Tokenizer

tokenizer = Tokenizer()
tokenizer.build_vocab("https://example-files.online-convert.com/document/txt/example.txt", fromWeb=True)

enc = tokenizer.encode("The names are also used to refer")
dec = tokenizer.decode(enc)

#tokenizer.test("https://example-files.online-convert.com/document/txt/example.txt")

print(enc)
print(dec)