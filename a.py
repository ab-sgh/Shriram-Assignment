import pickle
try:
    le = pickle.load(open('encoder.pkl', 'rb'))
    print("LabelEncoder loaded successfully")
    print("LabelEncoder type:", type(le))
    print("LabelEncoder attributes:", dir(le))
except Exception as e:
    print("Error loading LabelEncoder:", e)