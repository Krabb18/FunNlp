from tokenizer import Tokenizer
from funcs import pad_sequence

tokenizer = Tokenizer()
tokenizer.build_vocab("https://example-files.online-convert.com/document/txt/example.txt", fromWeb=True)

enc = tokenizer.encode("The names are also used to refer")
enc2 = tokenizer.encode("John Doe is sometimes used to refer to a typical male in other contexts as")

l = [enc, enc2]

#dec = tokenizer.decode(enc)

#tokenizer.test("https://example-files.online-convert.com/document/txt/example.txt")
s_new = pad_sequence(l, "UNK")
print(s_new)
#print(enc)
#print(dec)