import streamlit as st
import yfinance as yf # yahoo finance
import pandas as pd

days = 10
tickers = {
    "oracle": "ORCL",
    "Meta": "META",
    "apple": "AAPL",
    "google": "GOOGL",
    "microsoft": "MSFT",
    "amazon": "AMZN"
}

st.title('株価取得アプリ')

st.write("view oracle stock price")

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

df = get_data(days, tickers)
st.write(df)

#st.write(df.plot())
