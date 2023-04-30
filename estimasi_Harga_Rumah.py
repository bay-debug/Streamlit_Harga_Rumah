import pickle
import streamlit as st

model = pickle.load(open('estimasi_Harga_Rumah.sav', 'rb'))

st.title('Estimasi Harga Perumahan ')

bedrooms = st.number_input('Input Kamar Tidur')
bathrooms = st.number_input('Input Kamar Mandi')
floors = st.number_input('Input Lantai')
grade = st.number_input('Input Grade')
condition = st.number_input('Input nilai kondisi rumah')
view = st.number_input('Input nilai pemandangan')
waterfront = st.number_input('Input nilai kondisi lingkungan')


predict = ''

if st.button('Estimasi Harga Rumah'):
    predict = model.predict(
        [[bedrooms, bathrooms, floors,grade,condition,view,waterfront]]
    )
    st.write ('Estimasi harga 1 Unit Rumah ($): ', predict)
    st.write ('Estimasi harga 1 Unit Rumah IDR (Rp) :', predict*19000)