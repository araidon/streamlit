import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')

with st.empty():
    for seconds in range(100):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(0.01)
    #st.write("✔️ 1 minute over!")
    st.empty()
#st.balloons()

st.write("view progress bar")
"start"

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

"done"
















# st.write('Input Widgets')

# left_column, right_column = st.columns(2)
# button = left_column.button("left column")
# if button == True:
#     right_column.write("Here is the right column")

# option = st.sidebar.text_input("What's your favolite")

# option = st.selectbox(
#     "あなたが好きな数字を教えてください",
#     list(range(1,11))
# )
# st.write("Your favolite is ", option)

# slider = st.sidebar.slider("What's your condition?", 0, 100, 50, 25)
# st.write("Your Condition:", slider)

expander1 = st.expander("ask you 1")
expander1.write("write here")
expander2 = st.expander("ask you 2")
expander2.write("write here")

# checkboxで表示可否
# if st.checkbox('Show Image'):
#     # 画像を表示させる
#     img = Image.open('Cute Cat Grooming Logo.png')
#     st.image(img, caption='cute cat', use_column_width=True)



st.write('DataFrame')

#　表を書き込み
df = pd.DataFrame(
#    '1列目': [1, 2, 3,4],
#    '2列目': [50,20,30,40]
    np.random.rand(20,3),
   columns=['a','b','c']
#緯度経度（新宿付近）
    # np.random.rand(100,2)/[50, 50] + [35.69, 139.70], 
    # columns=['lat','lon']

)
#st.dataframe(df.style.highlight_max(axis=0)) #動的テーブル
#st.table(df.style.highlight_max(axis=0)) #静的テーブル
# st.line_chart(df) # 折れ線グラフ
# st.area_chart(df) # 折れ線+面グラフ
# st.bar_chart(df) # 棒グラフ
# st.map(df, size=20, color='#0044ff') #地図チャート






















# magic commands
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

