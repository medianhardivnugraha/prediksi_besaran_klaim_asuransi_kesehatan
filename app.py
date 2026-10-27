import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.title("Welcome to Streamlit")
st.write('This website is created using Streamlit')

if 'value' not in st.session_state:
    st.session_state['value'] = 0

if st.button("Increment"):
    st.session_state['value'] += 1

if st.button("Decrement"):
    st.session_state['value'] -= 1

st.write(f"Counter: {st.session_state['value']}")

st.header('Masukkan Identitas Diri Anda!')
age_input = st.number_input('Masukkan umur ')
bmi_input = st.number_input('Masukkan BMI ')
children_input = st.number_input('Masukkan jumlah anak ')
sex_input = st.radio('Jenis kelamin ', ['Laki-laki','Perempuan'])
smoker_input = st.radio('Merokok? ', ['Ya','Tidak'])
region_input = st.radio('Wilayah Tempat Tinggal', ['Northeast','Northwest','Southeast','Southwest']).lower()


if 'model' not in st.session_state:
    st.session_state['model'] = pickle.load(open('rf_model_charges.sav', 'rb'))

if(sex_input == 'Laki-laki'):
    sex_input = 'male'
else:
    sex_input = 'female'

if(smoker_input == 'Ya'):
    smoker_input = 'yes'
else:
    smoker_input = 'no'

if st.button('Prediksi Harga'):
    data_dict = {'age' : age_input, 'bmi' : bmi_input, 'children' : children_input, 'sex' : sex_input, 'smoker' : smoker_input, 'region' : region_input}
    data = pd.DataFrame(data_dict, index=[0])

    # st.write(data) # buat debugging
    result = st.session_state['model'].predict(data)
    st.write(f'Perkiraan biaya rumah sakit Anda adalah: ${result[0]}')
else:
    st.write('Masukkan data diri Anda lalu tekan tombol Prediksi Harga dan model akan memprediksi biaya rumah sakit Anda!')