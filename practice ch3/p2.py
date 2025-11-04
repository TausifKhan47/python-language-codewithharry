letter='''Dear <|NAME|>,
          you are selected!
          <|Date|>'''

print(letter.replace("<|NAME|>","Harry").replace("<|Date|>","25 aug 2056"))