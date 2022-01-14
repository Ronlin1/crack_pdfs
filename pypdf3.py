import PyPDF3
pdffile= open('IOT.pdf', 'rb')

pdfreader= PyPDF3.PdfFileReader(pdffile)

try:
    # print decryption outcome as 1 if successful and 0 otherwise
    pdfreader.decrypt('password')
except NotImplementedError as errMsg:
	print(pdfreader, 'can not be decrypted on error message', errMsg)
	pdffile.close()
