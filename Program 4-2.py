print("ORIGINAL MESSAGE")
print("-----------------")

with open("message.txt", "r") as file:
    content = file.read()
    print(content)
    characterNum = len(content)
    words = content.split()
    wordCount = len(content)
    letter = content.count("e")

print("\nTEXT ANALYSIS")
print("-----------------")
print("Number of Characters: ", characterNum)
print("Number of Words: ", wordCount)
print("\nUppercase version\n", content.upper())
print("\nLowercase version\n", content.lower())
print("\nCount of letter 'e': ", letter)

cipherShiftValue = int(input("Enter Caesar Cipher Shift Value: "))

print("\nENCRYPTED MESSAGE")
print("-----------------")
newContent = ""

for ch in content:
    ordValue = ord(ch)
    cipherValue = ordValue + cipherShiftValue
    if cipherValue > ord('z'):
        cipherValue = ord('a') + cipherShiftValue - (ord('z') - ordValue + 1)
    newContent += chr(cipherValue)

with open("encrypted_message.text", "x") as file:
    file.write(newContent)
    print(newContent)