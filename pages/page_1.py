import os, re, glob, cv2, numpy as np
load = st.sidebar.button('Press to use Example Dataset')
st.session_state.load = load
if "state" not in st.session_state:
  st.session_state.state = False
if load or st.session_state.state:
  st.session_state.state = True
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
      st.write("Jumlah dataset"+str(i)+" : "+str(count))
      label = label + 1
      lb_arr.append(i)
  X = np.array(X)
  y = np.array(y);
  import matplotlib.pyplot as plt
  plt.imshow(X[0])
  fig, axs = plt.subplots(2, 5, figsize=(20,10))
  cnt = 0
  row = 0
  col = 0
  for i in im_arr:
    for key, value in i.items():
      if(cnt==5):
        row = row + 1
        col = 0
        cnt = 0
      axs[row, col].imshow(value)
      axs[row, col].set_title(key)
      cnt = cnt + 1
      col = col + 1
  plt.show
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.pyplot()

  # PREPROCESSING
  from sklearn.model_selection import train_test_split
  # from keras.utils import to_categorical
  from tensorflow.keras.utils import to_categorical
  from sklearn.metrics import classification_report
  from sklearn.metrics import confusion_matrix
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
  X_train = X_train.astype('float32') #set x_train data type as float32
  X_test = X_test.astype('float32') #set x_test data type as float32
  X_train /= 255 #change x_train value between 0 - 1 
  X_test /= 255 #change x_test value between 0 - 1 
  y_train = to_categorical (y_train, 2) #change label to binary / categorical: [1 0 0 0] = 0, [0 1 0 0] = 1, so on
  y_test = to_categorical (y_test, 2) #change label to binary / categorical
