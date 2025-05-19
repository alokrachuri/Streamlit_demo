import streamlit as st
'''                                           
st.title("Title")
st.write("st.write")
data = st.text_input("write the text")
st.download_button("Download file",data)
'''
st.title("Title")
st.header("Header",divider=False)
st.subheader("subheader",divider=False)
st.markdown("here is a :book:")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")
col1,col2 = st.columns(2,gap="large")
with col1:
    x=st.slider("choose an x value",1,10)
with col2:
    st.write("The value of :red[*x*] is",x)