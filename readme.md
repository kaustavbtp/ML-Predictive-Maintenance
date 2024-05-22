# Activate python Environment
python -m venv env-PM1
.\env-PM1\Scripts\activate

# To install all the required python Packages/modules
pip install -r requirements.txt

# Optional -  To install individual python Packages/Modules
pip install <module/package Name>

# Optional - To display any Install Python Package/Modules details
pip show <package_name>

# Generate ML Model and get the accuracy in terminal
go to the backend directory using  --> CD 
execute below command:
python ml_training.py


# Activate the FastAPIs
uvicorn app:app --reload

# Validate the APIs and Try Out
http://127.0.0.1:8000/docs


# To run Streamlit UI
Streamlit run <fileName>.py

