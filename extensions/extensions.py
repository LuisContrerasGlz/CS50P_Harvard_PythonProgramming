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