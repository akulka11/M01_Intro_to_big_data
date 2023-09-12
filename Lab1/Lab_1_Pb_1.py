################################
# Name : Aditya Pradip Kulkarni  #  
# ID : 1330344                   # 
################################
msg = input("Original message: ")

compressed_msg = ""
i = 0

while i < len(msg):
    current_char = msg[i]
    count = 1

    while i + 1 < len(msg) and msg[i] == msg[i + 1]:
        count += 1
        i += 1

    if count > 1:
        compressed_msg += current_char + str(count)
    else:
        compressed_msg += current_char

    i += 1

print("Compressed message:", compressed_msg)
