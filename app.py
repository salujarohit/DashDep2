#Main Packages
import streamlit as st 
import os 
import joblib 

#ML Packages 
import pandas as pd
import numpy as np 

#Data Viz Packages 
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
#SHAP
import shap
shap.initjs()


# load model 
def load_prediction_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def load_shap_object(shap_file):
	shap_object = joblib.load(open(os.path.join(shap_file),"rb"))
	return shap_object


def main():
	
	st.title("Org Health Dashboard")


	menu = ["Revenue Forecasting", "Sales Activity Correlations", "About"]

	choices = st.sidebar.selectbox("Options", menu)

	if choices == 'Revenue Forecasting':
		st.subheader("Revenue Forecasting using Sales Energy")

		month_choice = st.selectbox("Select the Amount of Sales Energy for Forecasting", ["Previous Month","Previous 2 Months","Previous 3 Months"])
		if month_choice == "Previous Month":

			st.write("*Default Sales Energy below is from 31-12-2018*")

			meetings_sales_competence = st.number_input("Meetings Organized by Futuricians with Sales Competence",0.564	)
			meeting_tc_sales = st.number_input("Meetings Sales Competence with Top Clients ",0.549)
			meeting_regarding_TC = st.number_input("Meetings Regarding Top Clients",0.607)
			client_meeting_energy = st.number_input("M2 Recipts : Client Negotiations",0.840)
			taxi_energy = st.number_input("M2 Recipts : Taxi ",0.560)
			travel_parking_energy = st.number_input("M2 Recipts : Travel and Parking",0.630)
			effective_hours = st.number_input("Enter Effective FTE Hours",67606.50)


			sample_data = [meetings_sales_competence,meeting_tc_sales,meeting_regarding_TC,client_meeting_energy,taxi_energy,travel_parking_energy]


			pred_data = np.array(sample_data).reshape(1,-1)

			series_name = ['Meetings Sales Competence','Meeting  Sales Comptence with Top Clients','Meeting Regarding Top Clients','M2:Client Negotiations','M2:Taxi','M2: Travel and Parking']
			pred_data_series = pd.Series(sample_data, index = series_name)

			#st.write(pred_data_series)




			#model_choice = st.selectbox("Make Prediction using Mothly Activity",["Last Month's Activity"])
			
			if st.button("Predict"):
				#if model_choice == "Last Month's Activity":
				predictor = load_prediction_model("svr_t6.pkl")
				prediction = predictor.predict(pred_data)
				#st.write(prediction)

				effective_hours = np.array([effective_hours])
				final_result = prediction * effective_hours

				
				final_result = ("{:.2f}".format(float(final_result)))
				st.write("Predicted Reveue after Six Months")
				st.success(final_result)


				#SHAP Explainability

				shap_object = load_shap_object("explainer_t6")
				shap_values = shap_object.shap_values(pred_data)
				#st.write(shap_values)

				shap.force_plot(shap_object.expected_value, shap_values, pred_data_series, matplotlib=True, figsize=(15, 3), text_rotation=20)
				st.pyplot()







	if choices == 'Sales Activity Correlations':
		st.subheader('Sales Activity Correlations')

	if choices == 'About':
		st.subheader('About')






	#if choice == 'Revenue Forecasting':
		#st.subheader("Revenue Forecasting")

		#data = st.file_uploader("Upload Dataset", type = ["csv","txt"])
		
		




	




if __name__ == '__main__':
	main()