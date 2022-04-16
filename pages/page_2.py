if "prediksi" in st.session_state:
    prediksi = st.session_state.prediksi
else:
    prediksi = None

def load_prediksi(prediksi):
    import pandas as pd
    df = pd.read_csv(prediksi)
    return df

if prediksi is not None:
    df = load_prediksi(prediksi)
    st.write(df)