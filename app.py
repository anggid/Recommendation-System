# -*- coding: utf-8 -*-


import numpy as np
from joblib import dump, load
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

# app=Flask(__name__)
#Swagger(app)

pickle_in = open("svd.joblib","rb")
svd=load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: customer_id
        in: query
        type: number
        required: true
      - name: product_id
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=svd.predict([[customer_id,product_id]])
    print(prediction)
    return prediction



def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Customer Recommendation Product</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    customer_id = st.text_input("Customer ID","Type Here")
    product_id = st.text_input("Product ID","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(customer_id,product_id)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Anggi Dwifiani")

if __name__=='__main__':
    main()
    
    
    
