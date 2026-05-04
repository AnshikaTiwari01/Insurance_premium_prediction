import pickle
import pandas as pd

#import the ml model
with open('model/model.pkl','rb') as f:
   model = pickle.load(f)
#ML FLow
MODEL_VERSION='1.0.0'

#get class labels from model (import for matching ptob to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input:dict):
   input_df=pd.DataFrame([user_input])

   output=model.predict(input_df)[0]

   #getting prob for all the classes
   probabilities=model.predict_proba(input_df)[0]
   confidence=max(probabilities)

   #Create Mapping :{class_name:probability}
   class_probs=dict(zip(class_labels,map(lambda p:round(p,4), probabilities)))

   return{
      "predicted_category":output,
      "confidence":round(confidence,4),
      "class_probabilities":class_probs
   }  