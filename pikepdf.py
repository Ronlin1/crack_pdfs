import pikepdf
from tqdm import tqdm

# Empty password list
passwords = []

# Contain passwords in text file
password_text_file = "wordlist.txt"

# Iterate through each line
# and store in passwords list
for line in open(password_text_file, errors="ignore"):
    passwords.append(line.strip())

# iterate over passwords
for password in tqdm(passwords, "Cracking PDF File"):
    try:

        # open PDF file and check each password
        with pikepdf.open("IOT.pdf", password = password) as p:

            # If password is correct, break the loop
            print("[+] Password found:", password)
            break

    # If password will not match, it will raise PasswordError
    except pikepdf._qpdf.PasswordError as e:

        # if password is wrong, continue the loop
        continue
