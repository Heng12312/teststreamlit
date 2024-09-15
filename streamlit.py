import streamlit as st

#set the app title
st.title('My First Steamlit App')

#set the app subtitle
st.write('Welcome to My Streamlit App hello o3234243')

#this is how you "write"
st.write("This is a text")

#adding a button
st.button("reset", type="primary")
if st.button("Say hello"):
    st.write("Why Hello there")
    st.balloons()
else:
    st.write("Goodbye!")
    
    
    
with st.echo():
    st.write("Code will be executed and printed")