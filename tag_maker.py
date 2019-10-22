import csv
import bitcoin_address_extracter as bae
import html_language_detector as hld
import os
 
def read_html(path):
    with os.scandir(path) as it:
      for folder in it:
        if folder.is_dir():
          for html_file in os.scandir(folder):
            if html_file.name.endswith('.html'):
              html_path = path + '/'+ folder.name +'/' + html_file.name
              yield html_path

    
    

def make_tag(html):
    pass


def diff_category(html):
    pass


def check_lang(raw_html):
    file_lang = hld.LanguageDetector(raw_html)
    lang = file_lang.lang_detect()
    return lang


def extract_bitcoin(raw_html):
      bitcoin_list = bae.extract_wallet_address(raw_html)
      return bitcoin_list


def get_onion_address(html):
    pass
 

def write_csv(html):
    '''write_csv: 
       - input : html파일
       - output : data_numofbitcoin.csv
       - onion_address, bit, lang, category, tag
       - DB로 저장할 예정
    '''

       
    pass


def main(args):
    #TODO 1. html file 읽어오기
    #TODO 2. bitcoin 추출하기
    for html in read_html(args.html_path):
      with open(html) as html_file:
        raw_html = html_file.read()
        bit_address = extract_bitcoin(raw_html)
        lang = check_lang(raw_html)

        print(html.split('/')[-1], lang)
#      category = diff_category(html)
#      tag = make_tag(html)

#      write_csv(bit_address, lang, category, tag)
    #TODO 3. bitcoin이 있다면 , 언어 감지하기
    #TODO 4. 카테고리 분류하기


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--html-path','-p',
                        required=True,
                        type=str,
                        help='input collected tor html file')
    args = parser.parse_args()
    main(args)

