# Day6: decode the message by finding the first 4 sequential unique characters
UID_LEN = 14
with open('./msg', 'r') as lines:
    for line in lines:
        msg = line.strip()

    
        for i in range(UID_LEN, len(msg)):
            substr = msg[i-UID_LEN:i]
            detect = 1

            for char in substr:
                detect = detect * substr.count(char)

            if detect == 1:
                print("Unique message code at offset <{}> detected: [{}]".format(substr, i))
            
            #if (substr.count(msg[i]) == 1) and (substr.count(msg[i-1]) == 1) and (substr.count(msg[i-2]) == 1) and (substr.count(msg[i-3]) == 1):
                #print("Unique elf code detected: [{}]".format(msg[i-3:i+1]))
                #print("Message begins at offset {}".format(i+1))
                #break