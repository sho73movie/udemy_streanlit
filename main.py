import streamlit as st
import time

st.title('Streamlit 超入門')
# st.write('DataFrame')
#プログレスバーの表示

st.write('プレグレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

###
left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
###

###
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容3')
###

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns = ['a','b','c'],
# )

# st.line_chart(df)
# # 線の中を塗りつぶしたのが　area_chart
# st.area_chart(df)

# #棒グラフ
# st.bar_chart(df)

# #東京付近をマッピング 緯度、経度の順
# df2 = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns = ['lat','lon'],
# )
# st.map(df2)
# writeには引数がない
# st.write(df)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたが好きな数字は、',option, 'です'

# text = st.text_input(
#     'あなたの趣味を教えてください。'
# )
# 'あなたの趣味:',text

#condition = st.slider('あなたの今の調子は?',0,100,50)
# 'コンディション:',condition

#サイドバーの追加
#condition1 = st.sidebar.slider('あなたの今の調子は?',0,100,50)
#'コンディション:',condition1






# チェックボックスにチェックを入れたらimageが表示される
# if st.checkbox('show Image'):
#     #ファイルのパス　\を\\にする　または、r"文字列"　R"文字列"とする。
#     img = Image.open("C:\\Users\\sn112\\Python\\webapi\\sample.jpg")
#     # img = Image.open(r"C:\Users\sn112\Python\webapi\sample.jpg")
#     st.image(img, caption = 'cat', use_column_width = True)



# st.dataframe(df.style.highlight_max(axis = 0), width = 1000 , height = 1000)
#静的な表を表示させたいときは　table
# st.table(df.style.highlight_max(axis = 0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """