import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline (includes preprocessing)
model = joblib.load("model_ai_jobs.joblib")

st.title("AI Job Salary Predictor (2025)")
st.write("Select job attributes to predict the estimated salary:")

# Input dropdowns
job_title = st.selectbox("Job Title", ['AI Research Scientist', 'AI Software Engineer', 'AI Specialist', 'NLP Engineer', 'AI Consultant', 'AI Architect', 'Principal Data Scientist', 'Data Analyst', 'Autonomous Systems Engineer', 'AI Product Manager', 'Machine Learning Engineer', 'Data Engineer', 'Research Scientist', 'ML Ops Engineer', 'Robotics Engineer', 'Head of AI', 'Deep Learning Engineer', 'Data Scientist', 'Machine Learning Researcher', 'Computer Vision Engineer'])
experience_level = st.selectbox(
            "Experience Level", 
            ["EN", "MI", "SE", "EX"], 
            help="EN: Entry-Level, MI: Mid-Level, SE: Senior-Level, EX: Executive" 
            )
employment_type = st.selectbox(
            "Employment Type",
            ["FT", "PT", "CT", "FL"],
            help="FT: Full-Time, PT: Part-Time, CT: Contract, FL: Freelance"
            )

company_location = st.selectbox("Company Location", ["US", "DE", "ES", "IN", "GB", "FR", "CA", "AU", "BR", "Other"],help= "US: United States, DE: Germany, ES: Spain, IN: India, GB: Great Britain, FR: France, CA: Canada, AU: Australia, BR: Brazil, Other: Other Countries")
company_size = st.selectbox("Company Size", ["S", "M", "L"], help="S: Small, M: Medium, L: Large")
employee_residence = st.selectbox("Employee Residence", ["US", "DE", "ES", "IN", "GB", "FR", "CA", "AU", "BR", "Other"],help= "US: United States, DE: Germany, ES: Spain, IN: India, GB: Great Britain, FR: France, CA: Canada, AU: Australia, BR: Brazil, Other: Other Countries")
remote_ratio = st.selectbox("Remote Ratio", [0, 50, 100], help="0: No Remote Work, 50: Hybrid, 100: Fully Remote")
education_required = st.selectbox("Education Required", ["None", "Bachelor", "Master", "PhD"])

industry = st.selectbox("Industry", [
    "Technology", "Finance", "Healthcare", "Education", "Retail",
    "Manufacturing", "Consulting", "Energy", "Other"])
years_experience = st.slider(
    "Years of Experience", 
    min_value=1, 
    max_value=19, 
    value=5, 
    step=1, 
)



# Create dataframe for prediction
input_data = pd.DataFrame({
    "job_title": [job_title],
    "experience_level": [experience_level],
    "employment_type": [employment_type],
    "company_location": [company_location],
    "company_size": [company_size],
    "employee_residence": [employee_residence],
    "remote_ratio": [remote_ratio],
    "education_required": [education_required],
    "years_experience": [years_experience],
    "industry": [industry]
})

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.subheader("Predicted Salary:")
    st.write(f"${prediction[0]:,.2f}")

