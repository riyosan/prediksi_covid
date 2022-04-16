import streamlit as st
import streamlit_book as stb
import os, re, glob, cv2, numpy as np

# Set wide display
st.set_page_config(layout="wide")

# Set shared sidebar
st.sidebar.markdown("## Shared Sidebar")

split_size = st.sidebar.slider('Rasio Pembagian Data (% Untuk Data Latih)', 10, 90, 80, 5)
st.session_state.split_size = split_size
jumlah_fitur = st.sidebar.slider('jumlah pilihan fitur (Untuk Data Latih)', 5, 47, 20, 5)
st.session_state.jumlah_fitur = jumlah_fitur
parameter_n_estimators = st.sidebar.slider('Number of estimators (n_estimators)', 10, 100, 50, 10)
st.session_state.parameter_n_estimators = parameter_n_estimators
tetangga = st.sidebar.slider('Jumlah K (KNN)', 11, 101, 55, 11)
st.session_state.tetangga = tetangga
dataset = st.sidebar.file_uploader("Unggah File CSV", type=['csv'])
st.session_state.dataset = dataset
prediksi = st.sidebar.file_uploader("Unggah File prediksi CSV", type=['csv'])
st.session_state.prediksi = prediksi
load = st.sidebar.button('Press to use Example Dataset')
st.session_state.load = load
if load:
	dirs = os.listdir('/content/drive/MyDrive/covid/COVID-19-master/x_ray')
	label = 0
	im_arr = []
	lb_arr = []
	X = []
	y = []
	for i in dirs: #loop all directory
	    count = 0
	    for pic in glob.glob('/content/drive/MyDrive/covid/COVID-19-master/x_ray/'+i+'/*'):
	        im = cv2.imread(pic)
	        im = cv2.resize(im,(70,70))
	        im = np.array(im)
	        count = count + 1
	        X.append(im)
	        y.append(label)
	        if(count <= 10):
	            im_arr.append({str(i):im})
	    st.write("Jumlah "+str(i)+" : "+str(count))
	    label = label + 1
	    lb_arr.append(i)
	X = np.array(X)
	y = np.array(y);
# Set multipage
# save_answers = False
stb.set_chapter_config(path="pages/"
                       # save_answers=save_answers,
                       )
# stb.set_chapter_config(path='pages', toc=False, button='top', button_previous='⬅️', button_next='➡️', button_refresh='🔄', on_load_header=None, on_load_footer=None, save_answers=False)