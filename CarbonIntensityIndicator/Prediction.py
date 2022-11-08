import streamlit as st
from Multiapp import MultiApp
import  M1BULKCARRIER, M2CONTAINER, M3TANKER# import your app modules here
from streamlit_option_menu import option_menu




choose = option_menu(None,["Introduction", "CII Prediction", "About"],orientation = 'horizontal')

if choose == "CII Prediction":
    app = MultiApp()


    # Add all your application here
    app.add_app("Bulk Carrier", M1BULKCARRIER.app)
    app.add_app("Container Ship", M2CONTAINER.app)
    app.add_app("Tanker", M3TANKER.app)
    
    
    

    # The main app
    app.run()

elif choose == "Introduction":
        st.title('Introduction to CII') 

        st.image(('CarbonIntensityIndicator/vessel.jpg'))
        st.markdown("The IMO, set a Greenhouse Gas Reduction Strategy in 2018. One of the goals is to achieve a reduction in carbon intensity of 40% by 2030 with the level at 2008 being the baseline. In 2021, the IMO introdiced CII, a strategy to cut down the shipping industry's carbon footprint. This new strategy will put increasing pressure on all industry actors and require ship owners to report their sustainable operations annually The Carbon Intensity Indicator (CII) is a rating system for ships that the International Maritime Organization (IMO) developed. This will be a mandatory measure under MARPOL Annex VI, which comes into force in 2023. ")

        col1, col2 = st.columns([1,1])
        col1.markdown("CII requirements will take effect for all cargo, RoPax and cruise vessels above 5,000 GT and trading internationally. The CII measures how efficiently a ship transports goods or passengers and is given in grams of CO2 emitted per cargo-carrying capacity and nautical mile. The ship is then given an annual rating ranging from A to E, whereby the rating thresholds will become increasingly stringent towards 2030. The required CII will be reduced by a further 2% each year relative to the baseline set in 2019. Vessels that achieve an D rating, or a E rating for three consecutive years, need to implement a ‘Corrective Action Plan’ to ensure they achieve at least a C rating the following year. ")
        col2.image('CarbonIntensityIndicator/rating.png',caption='CII Rating')
          
        st.image('CarbonIntensityIndicator/cii.jpg',caption='CII required values to get increasing stringent')
        
        with st.expander("References"):
            st.write("""
                https://www.dnv.com/maritime/insights/topics/CII-carbon-intensity-indicator/index.html""")
            st.write("https://marine-digital.com/article_cii")
                     
            
            
                         
                         
            
            
    
        


elif choose == "About":
    st.title("About Application")
    
    st.markdown("The CII Prediction tool has been build to allow shipowners/ship operators to predict CII rating of their fleet by utilizing machine learning. Historical data of the global fleet, consisting of over 10,000 vessels have been extracted to predict  fuel consumption of various ship types. The algorithm is built using random forest regressor. The CII predictor tool is build based on IMO resolutions MEPC.352(78), MEPC.353(78) and MEPC.354(78) and does not take into account for 2022 interim guidelines on correction factors and voyage adjustments for CII calculations. ")


