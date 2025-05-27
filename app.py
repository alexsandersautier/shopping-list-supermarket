import streamlit as st
import pandas as pd
from service import system

st.set_page_config(
    page_title=f'{system.currenty_date}',
    page_icon='🛍️'
)

if "current_product" not in st.session_state:
    st.session_state["current_product"] = ""
if "current_list" not in st.session_state:
    st.session_state["current_list"] = []

def adicionar_item():
    produto = st.session_state["current_product"]
    if produto:
        st.session_state["current_list"].append({"Produto": produto, "Quantidade": 0.0, "Preço": 0.00})
        st.session_state["current_product"] = ""


st.header(f'Nossas compras de {system.currenty_date}')

st.text_input('Digite qual produto deseja adicionar na lista', key="current_product")

st.button('Adicionar', on_click=adicionar_item)



if st.session_state["current_list"]:
    df = pd.DataFrame(st.session_state["current_list"])
else:
    df = pd.DataFrame(columns=["Produto", "Quantidade", "Preço"])

edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic")

try:
    edited_df["Quantidade"] = pd.to_numeric(edited_df["Quantidade"], errors="coerce").fillna(0)
    edited_df["Preço"] = pd.to_numeric(edited_df["Preço"], errors="coerce").fillna(0)
    total = (edited_df["Quantidade"] * edited_df["Preço"]).sum()
except KeyError:
    total = 0

st.markdown(f"### Total: R$ {total:.2f}")