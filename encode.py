print("I can help you write an encrypted message to your friend")

message = input("Enter your message: ")
key = int(input("Enter the key: "))
message = list(message)

for i in range(len(message)):
    if message[i].isupper():
        message[i] = chr((((ord(message[i]) - 65) + key) % 26) + 65)
    else:
        message[i] = chr((((ord(message[i]) - 97) + key) % 26) + 97)

message = ''.join(message)
print("The cipher message is: ", message)
