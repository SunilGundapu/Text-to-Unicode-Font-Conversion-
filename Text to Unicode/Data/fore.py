import pdftotext

# Load your PDF
with open("1.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# How many pages?
print(len(pdf))

# Iterate over all the pages
for char in pdf[1]:
    print(str(char), char)
