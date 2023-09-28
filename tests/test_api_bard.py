from bardapi import Bard
import os
os.environ['_BARD_API_KEY']=""

Bard().get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
