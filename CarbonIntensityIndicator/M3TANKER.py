import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time



model = pickle.load(open('CIIApp/CarbonIntensityIndicator/modeltankernew.sav', 'rb'))

def app():
    st.image('oiltanker.jpg')
    st.subheader('Enter Vessel Data')
    
   # FUNCTION
    def user_report(): 
      global dwt
      global speed
      global distance
      dwt = st.number_input('Enter Deadweight (Tonnes)', min_value = 5000.0, max_value = 400000.0, step= 0.1)
      speed = st.number_input('Enter Average speed (Knots)', min_value = 5.0, max_value = 20.0, step = 0.1)
      loa = st.number_input('Enter Length Overall (M)', min_value = 100, max_value = 400)
      beam = st.number_input('Enter Beam (M)', min_value = 5.0, max_value = 70.0, step= 0.1)
      draft = st.number_input('Enter Draft (M)', min_value = 2.0, max_value = 20.0, step = 0.1)
      power = st.number_input('Enter Main Engine Output Power (KW)', min_value = 900.0, max_value = 85000.0, step = 0.1)
      distance = st.number_input('Enter Annual Distance Travelled (nm)',min_value = 10000.0, max_value = 100000.0, step = 0.1)
      
      

      user_report_data = {
          'dwt':dwt,
          'speed':speed,
          'loa':loa,
          'beam':beam,
          'draft':draft,
          'power':power,
          'distance': distance,
      }
      
      report_data = pd.DataFrame(user_report_data, index=[0])
      return report_data
  
      
    user_data = user_report()
    FC = np.round((model.predict(user_data)),2)
    
    
    
    Fuel_type = [ 'HFO','MDO/MGO','LFO']
    type_of_fuel = st.selectbox('Fuel Type', Fuel_type)
    
    
    if type_of_fuel == 'MGO/MDO':
        carbonemission = np.round((FC*3.206),2)
    elif type_of_fuel == 'HFO':
        carbonemission = np.round((FC*3.114),2)
    elif type_of_fuel == 'LFO':
        carbonemission = np.round((FC*3.151),2)
    
    
    
   
    
    
    # Calculate attained CII 
    CIIattained = np.round(((carbonemission/(distance*dwt))*10**6),2)
    
    
     #Calculate CII reference 
    a = 5247
    c = 0.610
    
    CIIref = a*(dwt**-c)
    
   
    
    #Caluclate CII required
    years = ['2023', '2024',"2025","2026"]
    year = st.selectbox("Select Year for CII Calculation",years)
    
    
    
    if year == '2023':
        CIIrequired = np.round((((100-5)/100)*CIIref),2)
    elif year == '2024':
        CIIrequired = np.round((((100-7)/100)*CIIref),2)
    elif year == '2025':
        CIIrequired = np.round(((100-9)/100)*CIIref,2)
    elif year == '2026':
        CIIrequired = np.round(((100-11)/100)*CIIref,2)
    
    

    #CII dd Vectors for Container Vessel
    
    d1 = 0.82
    d2 = 0.93
    d3 = 1.08
    d4 = 1.28
    supboundary= CIIrequired-((1-d1)*10)
    lowerboundary = CIIrequired-((1-d2)*10)
    upperboundary = CIIrequired +((d3-1)*10)
    inferiorboundary = CIIrequired+((d4-1)*10)
    
    
    if st.button("Predict CII"):
        with st.spinner('Predicting...'):
            time.sleep(2)
   
    
        st.subheader("Results:")
        st.markdown("Predicted Annual Fuel Consumption: " + str(FC[0]) +' Tonnes')
        st.markdown("Predicted Annual C02 Emission: "+ str(carbonemission[0]) + ' Tonnes')
        st.markdown("CII attained: " + str(CIIattained[0]))
        st.markdown("CII required: " + str(CIIrequired))
        
        
        if (CIIattained >= CIIrequired and CIIattained<=upperboundary):
            st.header("Rating: C")
        elif (CIIattained >= upperboundary and CIIattained <= inferiorboundary):
            st.header("Rating: D")
        elif (CIIattained >=inferiorboundary):
            st.header("Rating: E")
        elif (CIIattained <= CIIrequired and CIIattained >= lowerboundary):
            st.header("Rating: C")
        elif (CIIattained <= lowerboundary and CIIattained >=supboundary):
            st.header("Rating: B")
        else:
            st.header("Rating: A")
            
            
            
            
        #2023
        CIIrequired2023 = ((100-5)/100)*CIIref
        
        supboundary2023 = CIIrequired2023 -((1-d1)*10)
        lowerboundary2023 = CIIrequired2023 -((1-d2)*10)
        upperboundary2023 = CIIrequired2023 +((d3-1)*10)
        inferiorboundary2023 = CIIrequired2023 +((d4-1)*10)
        
        if (CIIattained >= CIIrequired2023 and CIIattained<=upperboundary2023):
            Rating2023 = 'C'
        elif (CIIattained >= upperboundary2023 and CIIattained <= inferiorboundary2023):
            Rating2023 = 'D'
        elif (CIIattained >=inferiorboundary2023):
            Rating2023 = 'E'
        elif (CIIattained <= CIIrequired2023 and CIIattained >= lowerboundary2023):
            Rating2023 = 'C'
        elif (CIIattained <= lowerboundary2023 and CIIattained >=supboundary2023):
            Rating2023 = 'B'
        else:
            Rating2023 = 'A' 
       
        #2024
        CIIrequired2024 = ((100-7)/100)*CIIref
        
        supboundary2024 = CIIrequired2024 -((1-d1)*10)
        lowerboundary2024 = CIIrequired2024 -((1-d2)*10)
        upperboundary2024 = CIIrequired2024 +((d3-1)*10)
        inferiorboundary2024 = CIIrequired2024 +((d4-1)*10)
        
        if (CIIattained >= CIIrequired2024 and CIIattained<=upperboundary2024):
            Rating2024 = 'C'
        elif (CIIattained >= upperboundary2024 and CIIattained <= inferiorboundary2024):
            Rating2024 = 'D'
        elif (CIIattained >=inferiorboundary2024):
            Rating2024 = 'E'
        elif (CIIattained <= CIIrequired2024 and CIIattained >= lowerboundary2024):
            Rating2024 = 'C'
        elif (CIIattained <= lowerboundary2024 and CIIattained >=supboundary2024):
            Rating2024 = 'B'
        else:
            Rating2024 = 'A'
            
            
        #2025
        CIIrequired2025 = ((100-9)/100)*CIIref
        
        supboundary2025 = CIIrequired2025 -((1-d1)*10)
        lowerboundary2025 = CIIrequired2025 -((1-d2)*10)
        upperboundary2025 = CIIrequired2025 +((d3-1)*10)
        inferiorboundary2025 = CIIrequired2025 +((d4-1)*10)
        
        if (CIIattained >= CIIrequired2025 and CIIattained<=upperboundary2025):
            Rating2025 = 'C'
        elif (CIIattained >= upperboundary2025 and CIIattained <= inferiorboundary2025):
            Rating2025 = 'D'
        elif (CIIattained >=inferiorboundary2025):
            Rating2025 = 'E'
        elif (CIIattained <= CIIrequired2025 and CIIattained >= lowerboundary2025):
            Rating2025 = 'C'
        elif (CIIattained <= lowerboundary2025 and CIIattained >=supboundary2025):
            Rating2025 = 'B'
        else:
            Rating2025 = 'A'
        
       
        #2026
        CIIrequired2026 = ((100-11)/100)*CIIref
        
        supboundary2026 = CIIrequired2026 -((1-d1)*10)
        lowerboundary2026 = CIIrequired2026 -((1-d2)*10)
        upperboundary2026 = CIIrequired2026 +((d3-1)*10)
        inferiorboundary2026 = CIIrequired2026 +((d4-1)*10)
        
        if (CIIattained >= CIIrequired2026 and CIIattained<=upperboundary2026):
            Rating2026 = 'C'
        elif (CIIattained >= upperboundary2026 and CIIattained <= inferiorboundary2026):
            Rating2026 = 'D'
        elif (CIIattained >=inferiorboundary2026):
            Rating2026 = 'E'
        elif (CIIattained <= CIIrequired2026 and CIIattained >= lowerboundary2026):
            Rating2026 = 'C'
        elif (CIIattained <= lowerboundary2026 and CIIattained >=supboundary2026):
            Rating2026 = 'B'
        else:
            Rating2026 = 'A'
        
    
        
        data = {
            
            '2023': [str(CIIattained[0]),str(np.round((CIIrequired2023),2)),Rating2023],
            '2024': [str(CIIattained[0]),str(np.round((CIIrequired2024),2)),Rating2024],
            '2025': [str(CIIattained[0]),str(np.round((CIIrequired2025),2)),Rating2025],
            '2026': [str(CIIattained[0]),str(np.round((CIIrequired2026),2)),Rating2026],
        
            }
        
        
        
        df = pd.DataFrame(data)
        df.index =['CII Attained', 'CII Required','Rating']
        
        st.dataframe(df)
        
        def graph():
            year = [2023,2024,2025,2026]

            upper = [upperboundary2023,upperboundary2024,upperboundary2025,upperboundary2026]
            inferior = [inferiorboundary2023,inferiorboundary2024,inferiorboundary2025,inferiorboundary2026]
            lower = [lowerboundary2023,lowerboundary2024,lowerboundary2025,lowerboundary2026]
            superior = [supboundary2023,supboundary2024,supboundary2025,supboundary2026]
            req = [CIIrequired2023,CIIrequired2024,CIIrequired2025,CIIrequired2026]
            attained =[CIIattained,CIIattained,CIIattained,CIIattained]
            
            
            
            
            plt.plot(year,req,linestyle='dashed',alpha =1, color = 'black', label = 'CII Required')
            plt.scatter(year,attained,alpha =1,s=8, label = 'CII Attained')
            
            
          
            plt.plot(year,superior,alpha=1, marker= 'o', markersize = 3,color = 'darkgreen', label = 'A Rating Threshold')
            plt.plot(year,lower,alpha=1,marker= 'o', markersize = 3, color = 'palegreen', label = 'B Rating Threshold')
            plt.plot(year,upper,alpha=1,marker= 'o', markersize = 3,color = 'orange', label = 'C Rating Threshold')
            plt.plot(year,inferior,alpha =1,marker= 'o', markersize = 3, color = 'red', label = 'D Rating Threshold')
           



            
            
            
            plt.plot(year,req,linestyle='dashed',alpha =1, color = 'black', label = 'CII Required')
            plt.plot(year,attained,alpha =1,marker= 'o', markersize = 3,label = 'CII Attained')
            
            
           
            
            
            plt.xticks(np.arange(min(year), max(year)+1, 1))
            
            
            
            
            
            plt.legend( bbox_to_anchor=(0,-0.12,1,0), loc = 'best', ncol=3, borderaxespad=0 )
                          
        

            plt.ylabel('CII')
            plt.xlabel('Year')
            
            
        k = graph()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(k)
    
    


