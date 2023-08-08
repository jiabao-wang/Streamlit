import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.header('st.Swrite\n Day5 JiabaoWang')
# example1 
st.write('Hello, *world!* :sunglasses')

# example2
st.write(1234)

# example3 
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,12,14,16]
})
st.write(df)

# Example4 
st.write('Below is a DataFrame:',df,'Above is a DataFrame')

# Example5
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c']
)
st.write(c)
