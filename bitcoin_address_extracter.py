from bs4 import BeautifulSoup
import os
import pandas as pd
import re
from hashlib import sha256

# html 디렉토리를 순회하면서 매일 00시 12시 디렉토리 하나에서 모든 bitcoin address를 추출
# 추출 된 bitcoin address는 하루 단위로 중복 없이 묶여서 보관

# rosettacode btc add validator
digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

# bitcoin address extract methods
# rosettacode btc add validator
def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    return n.to_bytes(length, 'big')


# rosettacode btc add validator
def check_bc(bc):
    bcbytes = decode_base58(bc, 25)
    return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]


def extract_wallet_address(sorce, result_set):
    btc_find = False

    # max length btc add math
    regex = re.compile("([13]{1}[A-HJ-NP-Za-km-z1-9]{25,33})")
    wallet_address_set = regex.findall(sorce)

    if len(wallet_address_set) > 0:
        for wallet_address in wallet_address_set:
            if check_bc(wallet_address) is True:
                btc_find = True
                print("Find btc address : "+wallet_address)
                result_set.append(wallet_address)
    # min length btc add match
    regex_lazy = re.compile("([13]{1}[A-HJ-NP-Za-km-z1-9]{25,33}?)")
    wallet_address_set_lazy = regex_lazy.findall(sorce)

    if len(wallet_address_set_lazy) > 0:
        for wallet_address in wallet_address_set_lazy:
            if check_bc(wallet_address) is True:
                btc_find = True
                print("Find btc address : "+wallet_address)
                result_set.append(wallet_address)
    return btc_find


def bitcoin_extracter(dir_route, dir_name):
    find_wallet_address = []

    all_html_list = os.listdir(dir_route)
    for html_route in all_html_list:
        target_html = open(dir_route+'/'+html_route, 'r')

        html_text = target_html.read()
        btc_find = extract_wallet_address(html_text, find_wallet_address)
        target_html.close()

    # address set to list
    # set으로 정리하기 이전에 기존에 파일에 있던 값도 리스트화 필요
    find_wallet_address = list(set(find_wallet_address))
    return find_wallet_address

    # write address list
    wallet_address_list_output = open(dir_name+'_extract_bitcoin.csv', 'w')
    for address_item in find_wallet_address:
        wallet_address_list_output.write(address_item + "\n")
    wallet_address_list_output.close()


#top_dir_route = '/home/kimsoohyun//shared_dir/html_source_dir'
#dir_name_list = os.listdir(top_dir_route)
#dir_name_list.sort()

#save_dir_route = '/media/lark/extra_storage/onion_link_set/html_171001_to_180327/testing/all_html_extracted_bitcoin_address_sum_by_day/'

#for idx in range( int(len(dir_name_list)/2) ):
#    filename=dir_name_list[idx*2][0:24]+'_extract_address.csv'
#    btc_list00 = bitcoin_extracter(top_dir_route+'/'+dir_name_list[idx*2], dir_name_list[idx*2])
#    btc_list12 = bitcoin_extracter(top_dir_route+'/'+dir_name_list[idx*2+1], dir_name_list[idx*2+1])
 #   btc_list = list(set(btc_list00) | set(btc_list12))
#    with open(save_dir_route + filename,'w') as output:
#        output.write('Bitcoin_address\n')
#        for add in btc_list:
#            output.write(add+'\n')
