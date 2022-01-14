import fitz  # this is PyMuPDF

# doc1 = "IOT.pdf"
with open("IOT.pdf", 'r+') as doc1:
    doc = fitz.Document(doc1)

# the document should be password protected
assert doc.needsPass

# print(doc.permissions)

# decrypt the document
if not doc.authenticate("pass"):
    print('cannot decrypt the document')
