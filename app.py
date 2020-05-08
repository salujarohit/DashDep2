import streamlit as st 
import pandas as pd
import numpy as np 



def main():
	
	st.title("Org Health Dashboard")


	activities = ["Revenue Forecasting", "Sales Activity Correlations"]

	choice = st.sidebar.selectbox("Select Activity", activities)




	if choice == 'Revenue Forecasting':
		st.subheader("Revenue Forecasting")

		data = st.file_uploader("Upload Dataset", type = ["csv","txt"])
		
		




	




if __name__ == '__main__':
	main()