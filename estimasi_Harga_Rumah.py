import pickle
import streamlit as st

model = pickle.load(open('estimasi_Harga_Rumah.sav', 'rb'))

st.title('Estimasi Harga Perumahan ')

bedrooms = st.number_input('Input Kamar Tidur')
bathrooms = st.number_input('Input Kamar Mandi')
floors = st.number_input('Input Lantai')


predict = ''

if st.button('Estimasi Harga Rumah'):
    predict = model.predict(
        [[bedrooms, bathrooms, floors]]
    )
    st.write ('Estimasi harga 1 Unit Rumah ($): ', predict)
    st.write ('Estimasi harga 1 Unit Rumah IDR (Rp) :', predict*19000)