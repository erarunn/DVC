import mlflow
import mlflow.pyfunc
import os

uri_path = mlflow.get_artifact_uri()
print(uri_path)
model_name = 'ElasticnetWineModel'
stage = 'Production'
model=mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{stage}")
print(model)
# logged_model = 'runs:/e5924b7765324fd398ac34f3806dc0e1/model'

# import requests

# # Replace with your Dagshub model URL
# dagshub_model_url = "https://dagshub.com/erarunn/DVC.mlflow/run/e5924b7765324fd398ac34f3806dc0e1/artifact/model"


# #loaded_model = mlflow.pyfunc.load_model("model.pkl")
# #print(loaded_model)
# response = requests.get(dagshub_model_url)
# print(response)
# if response.status_code == 200:
#     with open("model.pkl", "wb") as model_file:
#         model_file.write(response.content)
#         print(model_file)
