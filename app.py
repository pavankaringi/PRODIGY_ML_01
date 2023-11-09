import streamlit as st
import pickle

# Load the pre-trained linear regression model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit web app
def main():
    st.title('House Price Prediction')
    
    # Input fields for user to enter values
    sqft_living = st.number_input('Enter Sqft Living:', min_value=0)
    bedrooms = st.number_input('Enter Bedrooms:', min_value=0)
    bathrooms = st.number_input('Enter Bathrooms:', min_value=0)
    sqft_lot = st.number_input('Enter Sqft Lot:', min_value=0)
    floors = st.number_input('Enter Floors:', min_value=0)
    waterfront = st.number_input('Enter Waterfront (1 for Yes, 0 for No):', min_value=0, max_value=1)
    view = st.number_input('Enter View:', min_value=0)
    condition = st.number_input('Enter Condition:', min_value=0)
    
    # Predict the price when the user clicks the 'Predict' button
    if st.button('Predict'):
        prediction = model.predict([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition]])[0]
        st.success('Predicted Price: $ {:.2f}'.format(prediction))

if __name__ == '__main__':
    main()
