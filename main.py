import streamlit as st
import time

st.title('Streamlit 超入門')

# st.write('Display Image')

# if st.checkbox('Show Image'):
#   img = Image.open('sample.jpg')
#   st.image(img, caption='テスト画像', use_column_width=True)


st.write('プログレスバーの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

'Done!!'



left_column, right_column = st.columns(2)
button = left_column.button('左カラムにボタン')

if button:
  right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')
expander1.write('問い合わせ内容を書く')
expander1.write('問い合わせ内容を書く')







