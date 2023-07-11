import joblib
def predict_output(packet_df, features_df):
    model = joblib.load('ML_model/saved_model.pkl')
    predictions = model.predict(packet_df)
    features_df['result'] = predictions
    features_df.drop(['key'],axis=1, inplace=True)
    return