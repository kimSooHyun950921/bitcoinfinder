from bs4 import BeautifulSoup
from langdetect import detect
from langdetect import lang_detect_exception
import re

class LanguageDetector():

    def __init__(self, raw_html):
      self.raw_html = raw_html

    def remove_tag_from_html(self):
      #print(self.raw_html)
      style = re.compile('<style.*?>.*?</style>', re.DOTALL)
      remove_style = re.sub(style, '', self.raw_html)
      
      script = re.compile('<script.*?>.*?</script>', re.DOTALL)
      remove_script = re.sub(script, '', remove_style)
      
      tag = re.compile('<.*?>', re.DOTALL)
      remove_tag = re.sub(tag, '', remove_script)

      comment = re.compile('<!.*?>', re.DOTALL)
      import_msg = re.compile('@import url(.*?);', re.DOTALL)

      cleantext_without_comment = re.sub(comment, '', remove_tag)
      cleantext = re.sub(import_msg, '', cleantext_without_comment)
      cleantext = re.sub(style, '', cleantext)

      cleantext = cleantext.replace('\n','')
      return cleantext

    def lang_detect(self):
      try:
        html_word = self.remove_tag_from_html()
        lang = detect(html_word)
        return lang

      except lang_detect_exception.LangDetectException  as e:
        print(e)
        return None
      
      
      
