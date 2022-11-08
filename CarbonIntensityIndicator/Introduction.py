import streamlit as st



st.title('Introduction to CII') 

st.image(('CarbonIntensityIndicator/vessel.jpg'))
st.markdown("The IMO, set a Greenhouse Gas Reduction Strategy in 2018. One of the goals is to achieve a reduction in carbon intensity of 40% by 2030 with the level at 2008 being the baseline. In 2021, the IMO introdiced CII, a strategy to cut down the shipping industry's carbon footprint. This new strategy will put increasing pressure on all industry actors and require ship owners to report their sustainable operations annually The Carbon Intensity Indicator (CII) is a rating system for ships that the International Maritime Organization (IMO) developed. This will be a mandatory measure under MARPOL Annex VI, which comes into force in 2023. ")

col1, col2 = st.columns([1,1])
col1.markdown("CII requirements will take effect for all cargo, RoPax and cruise vessels above 5,000 GT and trading internationally. The CII measures how efficiently a ship transports goods or passengers and is given in grams of CO2 emitted per cargo-carrying capacity and nautical mile. The ship is then given an annual rating ranging from A to E, whereby the rating thresholds will become increasingly stringent towards 2030. The required CII will be reduced by a further 2% each year relative to the baseline set in 2019")
col2.image('rating.png')
  

  
st.image('cii.jpg')
