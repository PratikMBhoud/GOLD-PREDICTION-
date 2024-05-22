# importing necessary libraries
import pickle
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# load the model
gold = pickle.load(open('deployment.pkl', 'rb'))


def gold_(input_data):
    # Convert the date string to a pandas Timestamp object
    date = pd.Timestamp(input_data)
    # Now you can use the date in your prediction
  
    prediction = gold.predict({'time':input_data})
    return prediction[0]  # Extract only the predicted price

def main():
    # Page configuration
    st.set_page_config(page_title='Gold price prediction', layout='centered')
    
    st.title('Gold price prediction')

    # Input for start date
    start_date = st.date_input("Select the start date", value=datetime(2024, 5, 1))
    from datetime import  time
    # When 'Predict' is clicked, make the prediction and display it
    if st.button("Predict"):
        if start_date:  # Check if start_date is not empty
            # Define the end date as one year from the start date
            end_date = datetime.combine(start_date, time.min)
            
            start_date = (datetime(2024, 5, 1))
                             
           
            diff= end_date - start_date
            newdate = 773 + int(diff.days) + 1
            predictions=[]
            dates=[]
            
            # for i in range(773, newdate):
            #     print(i)
            #     pred = gold_(i)
            #     print(pred)
            #     pred_new = np.exp(pred)
            #     predictions.append(pred_new)
            
            pred = gold_(newdate)
            pred_new = np.exp(pred)
            predictions.append(pred_new)
          
            # Create a DataFrame to display the predictions
            dates = pd.date_range(start=start_date, end=end_date, freq='D')
            
            print(dates)
            prediction_df = pd.DataFrame({'Date': end_date, 'Predicted Price': predictions})

            # Display the DataFrame
            st.write("Predicted gold prices :")
            st.dataframe(prediction_df)

        else:
            st.warning("Please select a valid start date")

if __name__ == "__main__":
    main()
