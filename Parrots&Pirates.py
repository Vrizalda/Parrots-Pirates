import streamlit as st
st.title("¿Se quedan loros volando?")
piratas= st.number_input("número de piratas", min_value= 1, value= 4)
loros= st.number_input("total de loros", min_value= 0, value= 5)
loros_por_pirata= loros // piratas
if loros_por_pirata > 2:
    st.error("El cielo es verde")
else:
    st.success("Todos descansan, por hoy...")
