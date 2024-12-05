#! bin/python3 env

# Set to either 'encrypt' or 'decrypt'.
mode = input('What fo u want to do [e]ncrypt or [d]ecrypt ? ')

# The string to be encrypted/decrypted:
message = input('telling me : ')

# The encryption/decryption key:
key = input('key : ')

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def caeserCipher(massage,key,mode) :
     # Store the encrypted/decrypted form of the message:
    translated = ''
    for symbol in message:
         # Note: Only symbols in the SYMBOLS string can be encrypted/decrypte
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            # Perform encryption/decryption
            if mode == 'encrypt' or mode == 'e':
                    translatedIndex = symbolIndex + key
            elif mode == 'decrypt' or mode == 'd':
                translatedIndex = symbolIndex - key
             # Handle wraparound, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Output the translated string:
    return ('telling you :',translated)
#start
if key :
    print(caeserCipher(message,int(key),mode))
else :
    for key in range(len(SYMBOLS)) :
        print(f'${key} : ${caeserCipher(message,key,mode)}')
      
