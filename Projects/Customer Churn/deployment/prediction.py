import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model


# Load All Files

model_pipeline = joblib.load('final_pipeline.pkl')
model_ann = load_model('best_model.hf')

def run():
    
    with st.form ('key=churn'):
        st.write('### Input the Data')

        user_id                         = st.text_input ('User ID')
        age                             = st.number_input ('Age', min_value = 10, max_value = 100, value=20, step=1)
        gender                          = st.radio ('Gender', ('Male', 'Female'), index=1, help ='Gender')
        region_category                 = st.radio ('Region Category', ('City', 'Village', 'Town'), index=1, help ='Region you lives')
        membership_category             = st.radio ('Membership Category', ('No Membership', 'Basic Membership', 'Silver Membership', 'Premium Membership', 'Gold Membership', 'Platinum Membership'), index=1, help ='Membership you have')
        st.markdown('---')

        joining_date                    = st.date_input ('Join Date', help ='When you join')
        joined_through_referral         = st.radio ('Join From Referral', ('Yes', 'No'), index=1, help ='Join from referral or not')
        preferred_offer_types           = st.radio ('Preferred Offer Types', ('Without Offers', 'Credit/Debit Card Offers', 'Gift Vouchers/Coupons'), index=1, help ='Which offer you preferred')
        medium_of_operation             = st.radio ('Medium of Operation', ('Desktop', 'Smartphone', 'Both'), index=1, help ='Device you use')
        internet_option                 = st.radio ('Medium of Operation', ('Wi-Fi', 'Fiber_Optic', 'Mobile_Data'), index=1, help ='Internet you use')
        st.markdown('---')

        last_visit_time                 = st.time_input ('Last Visit Time')
        days_since_last_login           = st.number_input ('Days Since Last Login', min_value = 0,value=0, step=1)  
        avg_time_spent                  = st.number_input ('Average Time Spent', min_value = 0.00, format="%.2f")
        avg_transaction_value           = st.number_input ('Average Transaction Value', min_value = 0.00, format="%.2f")
        avg_frequency_login_days        = st.number_input ('Average Frequency Login Days', min_value = 0,value=0, step=1)  
        points_in_wallet                = st.number_input ('Points in Wallet', min_value = 0.00, format="%.2f")
        st.markdown('---')

        used_special_discount           = st.radio ('Used Special Discount', ('Yes', 'No'), index=1, help ='Used special discount or not')
        offer_application_preference    = st.radio ('Offer Application Preference', ('Yes', 'No'), index=1, help ='Offer application preference or not')
        past_complaint                  = st.radio ('Past Complaint', ('Yes', 'No'), index=1, help ='Past complaint or not')
        st.markdown('---')

        complaint_status                = st.selectbox ('Complaint Status', ('No Information Available', 'Not Applicable', 'Unsolved', 'Solved','Solved in Follow-up'), index=1, help ='Complaint Status')
        feedback                        = st.selectbox ('Feedback', ('Poor Website', 'Poor Customer Service', 'Too many ads', 'Poor Product Quality', 'No reason specified','Products always in Stock', 'Reasonable Price', 'Quality Customer Care', 'User Friendly Website'), index=1, help ='Feedback')       
       
        submitted = st.form_submit_button('Predict')    

    data_inf = {
        'user_id': user_id, 
        'age': age, 
        'gender': gender, 
        'region_category': region_category, 
        'membership_category': membership_category,
        'joining_date': joining_date, 
        'joined_through_referral': joined_through_referral, 
        'preferred_offer_types': preferred_offer_types,
        'medium_of_operation': medium_of_operation, 
        'internet_option': internet_option, 
        'last_visit_time': last_visit_time,
        'days_since_last_login': days_since_last_login, 
        'avg_time_spent': avg_time_spent, 
        'avg_transaction_value': avg_transaction_value,
        'avg_frequency_login_days': avg_frequency_login_days, 
        'points_in_wallet': points_in_wallet, 
        'used_special_discount': used_special_discount,
        'offer_application_preference': offer_application_preference, 
        'past_complaint': past_complaint, 
        'complaint_status': complaint_status,
        'feedback': feedback
    }
 
    data = pd.DataFrame([data_inf])
    st.dataframe(data)

    if submitted: 
        data_inf_transform = model_pipeline.transform(data)
        y_pred_inf = model_ann.predict(data_inf_transform)
        y_pred_inf = np.where(y_pred_inf >= 0.5, 1, 0)
        if y_pred_inf == 0:
            st.write('# Is it gonna churn? \nNope')
        else:
            st.write('# Is it gonna churn? \nYes')

if __name__ == '__main__':
    run()