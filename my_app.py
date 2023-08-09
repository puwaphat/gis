#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings


st.set_page_config(page_title="Transformer Recommender", page_icon="🌿", layout='centered', initial_sidebar_state="collapsed")

def load_model(modelfile):
    loaded_model = pickle.load(open(modelfile, 'rb'))
    return loaded_model

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Transformer Recommendation  🌱 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1,col2  = st.columns([2,2])
    
    with col1: 
        with st.expander(" ℹ️ Information", expanded=True):
            st.write("""
            Transformer recommendation is one of the most important aspects of precision power. It is based on a number of factors. Precision power seeks to define these criteria on a site-by-site basis in order to address TR selection issues. Precision power systems aren't all created equal. 
            However, in PEA, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss.

            """)
        '''
        ## How does it work ❓ 
        Complete all the parameters and the machine learning model will predict the most suitable transformer to plan in a particular area based on various parameters
        '''


    with col2:
        st.subheader(" Find out the most suitable Transformer to recommend in your area 👨‍🌾")
        Load_peak = st.number_input("Load", 1,10000)
        Ia = st.number_input("Current Phase A", 1,10000)
        Ib = st.number_input("Current Phase B", 1,10000)
        Ic = st.number_input("Current Phase C",1,10000)
        Min_V_peak = st.number_input("Minimun Voltage",1,10000)

        feature_list = [Load_peak, Ia, Ib, Ic, Min_V_peak]
        single_pred = np.array(feature_list).reshape(1,-1)
        
        if st.button('Predict'):

            loaded_model = load_model('model.pkl')
            prediction = loaded_model.predict(single_pred)
            col1.write('''
            ## Results 🔍 
            ''')
            col1.success(f"{prediction.item().title()} are recommended by the A.I for your area.")
      #code for html ☘️ 🌾 🌳 👨‍🌾  🍃

    st.warning("Note: This A.I application is for educational/demo purposes only and cannot be relied upon. Check the source code [here](https://github.com/puwaphat/gis)")
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
    main()

