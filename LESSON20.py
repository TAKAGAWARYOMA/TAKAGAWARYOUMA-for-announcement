import streamlit as st#streamlitをstとしてインポートしている
from PIL import Image#PIL(画像を使えるようにするオブジェクト)をインポートした

st.title("dot-labo発表用アプリ")#画面に表示するコード
st.caption("これはdot-laboの発表のために髙川稜真が作ったwebアプリです")#画面に表示するコード
st.subheader("自己紹介")#captionと同じように画面に表示できるコード
st.text("指名：髙川稜真")#captionと同じように画面に表示できるコード
st.text("年齢:12歳")
st.text("所属校:dot-labo神宮前校")

code = '''
import streamlit as st#streamlitをstとしてインポートしている
from PIL import Image#PIL(画像を使えるようにするオブジェクト)をインポートした

st.title("dot-labo発表用アプリ")#画面に表示するコード
st.caption("これはdot-laboの発表のために髙川稜真が作ったwebアプリです")#画面に表示するコード
st.subheader("自己紹介")#captionと同じように画面に表示できるコード
st.text("指名：髙川稜真")#captionと同じように画面に表示できるコード
st.text("年齢:12歳")
st.text("所属校:dot-labo神宮前校")

#画像
st.text("これはdot-laboのロゴです。")#画面に文字を表示する
image=Image.open("dot-labo.png")#変数imageを定義する
st.image(image,width=200)#画像を表示する

# テキストボックス

name=st.text_input("名前")#変数nameを定義している
print(name)#変数nameを表示する

#ボタン
submit_btn=st.button("送信")#変数submit_btnを定義する
cancel_btn=st.button("キャンセル")#変数cancel_btnを定義する
print(f'submit_but:{submit_btn}')#送信ボタンを表示している
print(f'cancel:{cancel_btn}')#キャンセルボタンを表示している
'''
st.code(code,language="python")

#画像
st.text("これはdot-laboのロゴです。")#画面に文字を表示する
image=Image.open("dot-labo.png")#変数imageを定義する
st.image(image,width=200)#画像を表示する

# #動画
# st.text("これは僕が学習した動画です。")
# video_file=open("https://www.youtube.com/watch?v=4nsTce1Oce8","rb")
# video_bytes=video_file.read()
# st.video(video_bytes)

# テキストボックス

name=st.text_input("名前")#変数nameを定義している
print(name)#変数nameを表示する

#ボタン
submit_btn=st.button("送信")#変数submit_btnを定義する
cancel_btn=st.button("キャンセル")#変数cancel_btnを定義する
print(f'submit_but:{submit_btn}')#送信ボタンを表示している
print(f'cancel:{cancel_btn}')#キャンセルボタンを表示している
