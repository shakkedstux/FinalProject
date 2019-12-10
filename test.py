piece_size = 4096 # 4 KiB

with open("screen2.jpg", "rb") as in_file, open("screen3.jpg", "wb") as out_file:
    while True:
        piece = in_file.read(piece_size)

        if piece == "":
            break # end of file

        out_file.write(piece)