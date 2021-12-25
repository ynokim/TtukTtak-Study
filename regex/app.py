import re

text_list = []
address_list = []
count = 0

# 맨 앞의 두 글자로 코인의 주소 특정
btc_pattern = r"^bc.{0,42}$"              #r"^bc"
eth_pattern = r"^0x.{0,42}$"              #r"^0x"
rip_pattern = r"^rU|^rs|^ra|^.{0,34}$"              #r"^rU|^ra|^rs"

# address.txt 파일에 있는 원본 주소 리스트에 추가
with open("address.txt", "r") as file:
    while True:
        text_line = file.readline()
        text_line = text_line.strip()
        text_list.append(text_line)
        if not text_line:
            file.close()
            break
        count += 1

# address.txt 파일에서 주소를 특정하고 특정 주소가 일치할 시 그 주소의 코인 이름 리스트에 추가
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

    # 결과갑 출력
    for i in range(0, count):
        print("%s 주소의 코인은 다음과 같습니다: %s" % (text_list[i], address_list[i]))

# /^bc/