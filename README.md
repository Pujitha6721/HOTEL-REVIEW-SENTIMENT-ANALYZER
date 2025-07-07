
#  Hotel Review Sentiment Analyzer

This project analyzes hotel customer reviews using AI-powered Natural Language Processing (NLP) to detect sentiment (Positive, Negative, Neutral) and identify specific service-related topics such as room service, food quality, and staff behavior. It helps hotel managers gain structured insights and improve service quality.

---

##  Project Objectives

- Automatically classify hotel reviews into sentiment categories
- Identify and tag service-related topics from guest feedback
- Summarize reviews into structured reports for decision-making
- Help hotel managers understand areas of strength and improvement

---

## 🛠 Tools & Technologies Used

| Category             | Tools / Technologies                            |
|----------------------|--------------------------------------------------|
| Programming Language | Python                                           |
| Libraries            | pandas, IBM WML SDK                              |
| AI Model             | FLAN-T5 (via IBM watsonx.ai)                     |
| Platform             | IBM Watson Prompt Lab                            |
| Cloud Storage        | IBM Cloud Object Storage (COS)                  |
| IDE                  | Google Colab                                     |

---





##  Methodology

1. Data Collection  
   - Collected hotel reviews in `.xlsx` format with a single column named `review`.

2. Few-shot Prompt Setup  
   - Provided example reviews and labels to guide the model using prompt templates.

3. Model Initialization  
   - Used `google/flan-t5-xxl` via IBM watsonx.ai to perform sentiment and topic classification.

4. Review Analysis  
   - Each review passed through the model to get both sentiment and service-related topics

5. Post-processing 
   - Extracted sentiment and topic separately from model output and saved final data into Excel.

---

##  Sample Output Columns

- Sentiment: Positive, Negative, Neutral
- Topics: Food Quality, Room Cleanliness, Staff Behavior, etc.

---

## Features

- Automates large-scale review analysis
- Identifies both emotions and specific services mentioned
- Reduces manual effort and improves accuracy
- Easily exportable results for reporting

---

##  Future Enhancements

- Add visual dashboards for hotel managers
- Use multilingual models to analyze global reviews
- Include rating predictions or star classifications

---


## Acknowledgements

- IBM watsonx.ai and Watson Prompt Lab for providing access to powerful AI models
- VIT-AP University for encouraging AI-based innovation

