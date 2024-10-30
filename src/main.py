from pydantic import BaseModel
from fastapi import FastAPI
import pickle
import uvicorn

class api_data(BaseModel):
    acousticness : float
    danceability : float
    duration_ms : float
    energy : float
    loudness : float
    speechiness : float
    valence : float
    
app = FastAPI()

@app.get("/")
def home():
    ret = {"res": "API is UP", "error_msg": ""}
    return ret

@app.post("/predict")
def predict (data : api_data):
    data =data.dict()
    acousticness=data['acousticness']
    danceability=data['danceability']
    duration_ms =data['duration_ms']
    energy=data['energy']
    loudness=data['loudness']
    speechiness=data['speechiness']
    valence=data['valence']

    pickle_in = open("fordeploy3.pkl","rb")
    model = pickle.load(pickle_in)
    prediction=model.predict([[acousticness,danceability,duration_ms,energy,loudness,speechiness,valence]])
    return {"Prediction" : prediction[0]}
#    pass

#    return {"message": "Hello World"}

#app = FastAPI()
#pickle_in = open("fordeploy1.pkl","rb")
#model = pickle.load(pickle_in)

#@app.get('/')
#def index():
#    return {'message': 'Spotify Predictor API'}

#@app.post('/Spotify/predict')
#def predict_popu(acousticness,danceability,duration_ms,energy,loudness,speechiness,valence):
#    """
#    this method is for prediction process 
#    takes all the Audio characteristics that we used for modelling and returns the prediction 
#    """
    #try:
    #    prediction = 0
#    pickle_in = open("fordeploy3.pkl","rb")
#    model = pickle.load(pickle_in)
#    prediction=model.predict([[acousticness,danceability,energy,loudness,speechiness,valence]])
#    return {"Prediction" : prediction}
    #print(prediction)
    #except InconsistentVersionWarning as w:
    #    print(w.original_sklearn_version)
#    return prediction

#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=8000)