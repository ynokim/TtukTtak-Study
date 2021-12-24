import re

text_list = []
address_list = []
count = 0

btc_pattern = r"^bc"
eth_pattern = r"^0x"
rip_pattern = r"^rU"

with open("address.txt", "r") as file:
    while True:
        text_line = file.readline()
        text_line = text_line.strip()
        text_list.append(text_line)
        if not text_line:
            file.close()
            break
        count += 1

with open("address.txt", "r") as file:
    for line in file:
        if re.search(btc_pattern, line):
            """btc_output = re.search(btc_pattern, line)
            address_list.append(btc_output.group())"""
            btc_output = "BITCOIN"
            address_list.append(btc_output)
        elif re.search(eth_pattern, line):
            """eth_output = re.search(eth_pattern, line)
            address_list.append(eth_output.group())"""
            eth_output = "ETHERIUM"
            address_list.append(eth_output)
        elif re.search(rip_pattern, line):
            """rip_output = re.search(rip_pattern, line)
            address_list.append(rip_output.group())"""
            rip_output = "RIPPLE"
            address_list.append(rip_output)
        else:
            output_nothing = "주소 타입의 특정이 불가합니다."
            address_list.append(output_nothing)
            pass

    for i in range(0, count):
        print("%s 주소의 코인은 다음과 같습니다: %s" % (text_list[i], address_list[i]))


# /^bc/