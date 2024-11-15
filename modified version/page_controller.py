# conda activate chat-with-website
import streamlit as st

Server = st.Page(
    page="views/server.py",
    title="Server",
    icon=":material/account_circle:",
)

Alice = st.Page(
    page="views/Alice.py",
    title="Alice's Control Page",
    icon=":material/account_circle:",
    default=True,  # default means the first page
)
Eve = st.Page(
    page="views/Eve.py",
    title="Eve's Control Page",
    icon=":material/account_circle:",
)

pg = st.navigation(pages=[Server, Alice, Eve])

pg.run()
