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

# load model 
def load_prediction_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def main():
	
	st.title("Org Health Dashboard")


	menu = ["Revenue Forecasting", "Sales Activity Correlations", "About"]

	choices = st.sidebar.selectbox("Options", menu)

	if choices == 'Revenue Forecasting':
		st.subheader("Revenue Forecasting using Sales Energy")

		month_choice = st.selectbox("Select the Amount of Sales Energy for Forecasting", ["Previous Month","Previous 2 Months","Previous 3 Months"])
		if month_choice == "Previous Month":

			meetings_sales_competence = st.number_input("Meetings Organized by Futuricians with Sales Competence")
			meeting_tc_sales = st.number_input("Meetings Sales Competence with Top Clients ")
			meeting_regarding_TC = st.number_input("Meetings Regarding Top Clients")
			client_meeting_energy = st.number_input("M2 Recipts : Client Negotiations")
			taxi_energy = st.number_input("M2 Recipts : Taxi ")
			travel_parking_energy = st.number_input("M2 Recipts : Travel and Parking")

			sample_data = [meetings_sales_competence,meeting_tc_sales,meeting_regarding_TC,client_meeting_energy,taxi_energy,travel_parking_energy]

			pred_data = np.array(sample_data).reshape(1,-1)


			#model_choice = st.selectbox("Make Prediction using Mothly Activity",["Last Month's Activity"])
			
			if st.button("Predict"):
				#if model_choice == "Last Month's Activity":
				predictor = load_prediction_model("svr_t6.pkl")
				prediction = predictor.predict(pred_data)
				#st.write(prediction)
				

				final_result = "{:.2f}".format(float(prediction))
				st.success(final_result)





	if choices == 'Sales Activity Correlations':
		st.subheader('Sales Activity Correlations')

	if choices == 'About':
		st.subheader('About')






	#if choice == 'Revenue Forecasting':
		#st.subheader("Revenue Forecasting")

		#data = st.file_uploader("Upload Dataset", type = ["csv","txt"])
		
		




	




if __name__ == '__main__':
	main()