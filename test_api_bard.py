from bardapi import Bard
import os
os.environ['_BARD_API_KEY']="bAijrgGMJ3o0bofe_H5tRG9Y2GbyPXHZcntCoUXAtTksD3BYe1HE4inGBmtTnmb8QnyRvA."

Bard().get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
