# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip

# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

files = input("File name: ").lower().strip()

if files.endswith(".gif"):
    print("image/gif")
elif files.endswith(".jpg"):
    print("image/jpeg")
elif files.endswith(".jpeg"):
    print("image/jpeg")
elif files.endswith(".png"):
    print("image/png")
elif files.endswith(".pdf"):
    print("application/pdf")
elif files.endswith(".txt"):
    print("text/plain")
elif files.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")