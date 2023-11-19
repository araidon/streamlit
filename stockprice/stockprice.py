import streamlit as st
import yfinance as yf # yahoo finance
import pandas as pd
import altair as alt

tickers = {
    "oracle": "ORCL",
    "Meta": "META",
    "apple": "AAPL",
    "google": "GOOGL",
    "microsoft": "MSFT",
    "amazon": "AMZN"
}

st.title('株価取得アプリ')

st.sidebar.write("""
# 株価
こちらは株価可視化ツールです。以下のオプションから表示日数を指定してください。
""")

st.sidebar.write("""
## 表示日数選択
""")

days = st.sidebar.slider("日数",1, 300, 20,)

st.write(f"""
## 過去 **{days}** 日間の株価情報
""")

@st.cache_data
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers:

        tkr = yf.Ticker(tickers[company]) # 株価を取得する
        hist = tkr.history(period=f"{days}d") #days日分を取得

        #hist_orcl.index.strftime("%d %B %Y") #日付のフォーマット変更、機能していなそうなのでコメントアウト
        hist = hist[["Close"]] #終値のみを取得
        hist.columns = [company] #カラム名を会社名に
        hist = hist.T #行列入れ替え
        hist.index.name = "Name"

        df = pd.concat([df, hist]) # dfにマージ
    return df


st.sidebar.write("""
## 株価の範囲指定
""")
ymin, ymax = st.sidebar.slider(
    "範囲を指定してください",
    0.0, 3000.0, (0.0, 400.0), step=10.0
)

df = get_data(days, tickers)

companies = st.multiselect(
    "会社名を選択してください",
    list(df.index),
    ["oracle","amazon","google"]
)
if not companies:
    st.error("少なくとも1社は選んでください。")
else:
    data = df.loc[companies]
    st.write("### 株価（USD）", data.sort_index())

    data = data.T.reset_index()
    data = pd.melt(data, id_vars=['Date']).rename(
        columns={"value": "Stock Prices(USD)"}
    )
    chart = (
        alt.Chart(data)
        .mark_line(opacity=0.8, clip=True)
        .encode(
            x ="Date:T",
            y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin,ymax])),
            color="Name:N"
        )
    )
    st.altair_chart(chart, use_container_width=True) #グラフ表示
