import streamlit as st

# OSS 중간 시험 결과
OSS_Score = [80, 70, 55 ,30 , 3, 3, 1, 0]

st.write("# OSS 중간 시험 결과")
st.write("## 몬헌 신작내놔")
st.write("### 캡콤 폭파시키기전에")

OSS_Score

st.bar_chart(OSS_Score)