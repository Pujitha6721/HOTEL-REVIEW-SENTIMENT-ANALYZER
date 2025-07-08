

# 1. Install Required Libraries (Run in Colab)
!pip install ibm-watson-machine-learning pandas --upgrade

# 2. Import Libraries
import pandas as pd
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning import APIClient

# 3. Ask User for API Key and Project ID
api_key = input("Enter your IBM Cloud API Key: ")
project_id = input("Enter your IBM Cloud Project ID: ")

# 4. Set IBM Credentials
wml_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": api_key
}
client = APIClient(wml_credentials)
client.set.default_project(project_id)

# 5. Load Review Dataset
df = pd.read_excel("/content/hotel_reviews.xlsx")  # Make sure file path is correct
df.dropna(subset=['review'], inplace=True)
print("Sample Data:", df.head())

# 6. Prompt Template for Multi-Label Classification
few_shot_prompt = """
Classify the following hotel review by sentiment and extract relevant service topics mentioned.
Return result as: Sentiment: [Positive/Negative/Neutral], Topics: [comma-separated tags]

Examples:
Review: The room was clean and the food was delicious.
Sentiment: Positive, Topics: room cleanliness, food quality

Review: The air conditioning was broken and no one helped.
Sentiment: Negative, Topics: room condition, service responsiveness
"""

# 7. Initialize Foundation Model
model_id = "google/flan-t5-xxl"
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 60,
    "stop_sequences": []
}
gen_model = Model(model_id=model_id, params=parameters, credentials=wml_credentials, project_id=project_id)

# 8. Define Classifier Function
def analyze_review(text):
    prompt = few_shot_prompt + f"\n\nReview: {text}\nSentiment:"
    try:
        result = gen_model.generate(prompt)
        if 'generated_text' in result:
            return result['generated_text'].strip()
        else:
            print("Missing output for:", text)
            return "Unknown"
    except Exception as e:
        print("Error:", e)
        return "Error"

# 9. Run Analysis
print("Analyzing reviews...")
df['Analysis'] = df['review'].apply(analyze_review)

# 10. Split Sentiment and Topics from Output
def split_result(analysis):
    try:
        parts = analysis.split(", Topics:")
        sentiment = parts[0].replace("Sentiment:", "").strip()
        topics = parts[1].strip() if len(parts) > 1 else ""
        return pd.Series([sentiment, topics])
    except:
        return pd.Series(["Unknown", ""])

df[['Sentiment', 'Topics']] = df['Analysis'].apply(split_result)

# 11. Export Results
df.to_excel("hotel_review_analysis_output.xlsx", index=False)
print("Results saved to hotel_review_analysis_output.xlsx")
