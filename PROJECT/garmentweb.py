import streamlit as st
 
def calculate_production_time(quantity, minutes_per_garment,workers,efficiency):
 total_work_minutes = quantity * minutes_per_garment
 theoretical_minutes = total_work_minutes /workers
 actual_minutes = theoretical_minutes / (efficiency / 100)
 actual_hours = actual_minutes / 60
 return actual_hours 


st.title("!! Garment production time estimator")

quantity = st.number_input("enter the quantity:", min_value=0)
minutes_per_garment =  st.number_input("enter the minutes per garment:",min_value=0.1)
workers = st.number_input("enter the number or workers:", min_value=0)
efficiency =st.number_input("enter the efficiency in percentage",min_value=0.1)

if st.button("calculate"):
 production_time = calculate_production_time(quantity, minutes_per_garment,workers,efficiency)
 st.write("Estimated production time:", round(production_time,2),"hours")
 

