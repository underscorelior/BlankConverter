from pick import pick
import pyperclip

num_to_zws = {
    "1" : "​",
    "2" : "‌",
    "3" : "­",
    "4" : "͏",
    "5" : "⁭",
    "6" : "⁢",
    "7" : "⁣",
    "8" : "឴",
    "9" : "឵",
    "0" : "؜",
    "space" : "⁤"
}

zwscode_to_num = {
    8203: "1",
    8204: "2",
    173: "3",
    847: "4",
    8301: "5",
    8290: "6",
    8291: "7",
    6068: "8",
    6069: "9",
    1564: "0",
}

# Encodes unicode to zero width space characters 
# takes the unicode code point of each character 
# x converts each number to a zero width space character (mapped in the num_to_zws dictionary)
# then adds a special zero width space character to the end of each "letter" to separate them
def encode():
    userinput = input("Enter text to encode: ")
    output = ""
    for letter in list(userinput):
        l = ord(letter)
        for num in list(str(l)):
            output += num_to_zws[num]
        output += num_to_zws["space"]
    return "Encode", userinput, output
    
# Decodes zero width space characters to their unicode code point
# converts each zero width space character to a number (mapped in the zwscode_to_num dictionary)
# then adds each number and converts it to a unicode character
def decode():
    userinput = input("Enter text to decode: ")
    output = ""
    for i in userinput.split("⁤"):
        temp = ""
        for zws in list(i):
            if zws not in num_to_zws.values():
                continue
            else:
                temp += zwscode_to_num[ord(zws)]
        output += chr(int(temp)) if temp != "" else " "
    return "Decode", userinput, output.rstrip()
            

title = "Please choose an option: "
start_options = ["Encode", "Decode", "Exit"]
loop = True

while loop:
    option, index = pick(start_options, title)

    if index == 0:
        method, userinput, output = encode()
    elif index == 1:
        method, userinput, output = decode()
    else:
        loop = False
        break

    pyperclip.copy(output)
    index = pick(['Press enter to continue...'], f"Mode:{method} \nInput: {userinput} \nOutput has been copied to your keyboard! [{output}]\n\n # Note: The output may look like it isnt zero width, but it is.")
