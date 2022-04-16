if "load" in st.session_state:
    load = st.session_state.load
else:
    load = None




# if "dataset" in st.session_state:
#     dataset = st.session_state.dataset
# else:
#     dataset = None

# def load_datasets(dataset):
#     import pandas as pd
#     df = pd.read_csv(dataset)
#     return df

# if dataset is not None:
#     df = load_datasets(dataset)
#     st.write(df)