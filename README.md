# Smartphone Recommendation App

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Skills Takeaway](#skills-takeaway)
- [Domain](#domain)
- [Problem Statement](#problem-statement)
- [Business Use Cases](#business-use-cases)
- [Installation](#installation)
- [Usage](#usage)
- [Formulas Used](#formulas-used)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Smartphone Recommendation App is designed to recommend smartphones based on sentiment analysis of reviews collected from Flipkart.
This project leverages web scraping, data parsing, sentiment analysis, and data visualization techniques to generate data-driven product recommendations.

## Features
- **Web Scraping**: Extract product reviews from Flipkart using Selenium, Beautiful Soup, and requests.
- **Data Parsing and Structuring**: Process and structure data for analysis.
- **Sentiment Analysis**: Analyze customer reviews to determine sentiment.
- **Data Visualization**: Create visual representations of data using Matplotlib, Seaborn, and Plotly.
- **LangChain**: Use LangChain with Hugging Face for generating product recommendations.

## Skills Takeaway
- Web Scraping
- Data Parsing and Structuring
- Sentiment Analysis
- Data Visualization
- Python Programming
- LangChain

## Domain
- E-commerce
- Data Science
- Machine Learning
- Deep Learning
- LLM
- NLP

## Problem Statement
The goal of this project is to develop an automated system for collecting and analyzing product reviews from Flipkart. By leveraging web scraping techniques and sentiment analysis, the project aims to generate data-driven product recommendations.

## Business Use Cases
- **E-commerce Platforms**: Enhance product recommendation engines by incorporating sentiment analysis of customer reviews.
- **Market Research Firms**: Analyze consumer sentiment towards various products to inform business strategies.
- **Retail Companies**: Monitor customer feedback to improve product offerings and customer satisfaction.
- **Business Intelligence Tools**: Integrate with dashboards to provide real-time insights on product performance based on customer reviews.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/SaravananPT/Flipkart-Web-Scrapping-and-Sentimental-Analysis-using-langchain.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Flipkart-Web-Scrapping-and-Sentimental-Analysis-using-langchain
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Ensure your dataset with smartphone reviews is available at the specified path.
2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
3. Navigate to the app in your web browser and explore the features:
    - **Homepage**: Overview and key details about the project.
    - **Dashboard**: Visualizations and summaries of the data.
    - **Question Section**: Ask specific questions and get recommendations based on sentiment analysis.

## Formulas Used
- **Polarity Score:** `polarity_score = row['Polarity_Score']`
- **Subjectivity Score:** `subjectivity_score = row['Subjectivity_Score']`
- **Negative Score:** `negative_score = row['Negative_Score']`
- **Gunning Fog Index:** `gunning_fog_index = row['Gunning_Fog_Index']`
- **Overall Score:** `overall_score = (W_p * polarity_score) - (W_s * subjectivity_score) - (W_n * negative_score) - (W_g * gunning_fog_index)`
- **Average Score:** `average_scores = {phone: sum(scores) / len(scores) for phone, scores in phone_scores.items()}`

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
