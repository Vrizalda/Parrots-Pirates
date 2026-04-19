import streamlit as st
st.title("¿Se quedan loros volando?")
piratas = st.number_input("número de piratas", min_value=1, value=3)
loros = st.number_input("total de loros", min_value=0, value=5)
loros_en_el_cielo = max(loros - piratas * 2, 0)
if loros > piratas * 2:
    if loros_en_el_cielo == 1:
        st.error("El cielo es verde 🦜 Hay 1 loro en el cielo")
    else:
        st.error(f"El cielo es verde 🦜 Hay {loros_en_el_cielo} loros en el cielo")
else:
    st.success("Todos descansan, por hoy...")
