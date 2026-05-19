**Multi-Agent AI Property Analytics System (Singapore HDB)**
- A multi-agent AI system for analyzing Singapore HDB resale prices, combining data processing, ML predictions, and LLM-based reasoning based on resale flats registered after 2017.

- Data Source: https://data.gov.sg/datasets?query=resale+flat+prices&resultId=d_2d5ff9ea31397b66239f245f57751537

**The system is designed as a multi-layered pipeline:**

1.Data Layer: Loads and cleans HDB resale data (CSV open source).
2.Agent Layer: Multi-agent design for modular analysis.
3.ML Layer: XGBoost-based prediction for future resale prices.
4.LLM Layer: Local LLM (Ollama, e.g., llama3) converts numeric results into natural language insights.
5.Visualization Layer: Charts, tables, and interactive Streamlit UI.

**The system is designed as a multi-layered pipeline:**
1.Data Layer: Loads and cleans HDB resale data (CSV open source).
2.Agent Layer: Multi-agent design for modular analysis.
3.ML Layer: XGBoost-based prediction for future resale prices.
4.LLM Layer: Local LLM (Ollama, e.g., llama3) converts numeric results into natural language insights.
5.Visualization Layer: Charts, tables, and interactive Streamlit UI.

**Pipeline Flow:**

Data Agent → retrieves HDB resale data
Trend Agent → finds trends: rising towns, highest blocks
Prediction Agent → forecasts prices 1 year ahead
Insight Agent → translates numbers into plain-language insights
Streamlit → displays charts, JSON, AI-generated insights

**Libraries and Stack**

Core Python: pandas, numpy
Machine Learning: scikit-learn, xgboost
AI / LLM: Ollama (local), requests
Visualization: matplotlib, folium (optional), streamlit-folium
Web App: streamlit

**Open Source Models and Data**
Ollama (llama3 or similar open-weight model)
Role: LLM agent for insights
Advantage: Offline, open-weight, privacy-preserving
HDB Resale Dataset (CSV)
Role: Core structured data for analysis and ML
License: Open-source / publicly available

**sg-property-agent/**
│
├── agents/
│   ├── __init__.py
│   ├── data_agent.py        # Loads and cleans HDB CSV
│   ├── trend_agent.py       # Finds trends, highest towns/blocks
│   ├── prediction_agent.py  # XGBoost-based price predictions
│   ├── insight_agent.py     # LLM agent for human-readable insights
│
├── data/
│   └── resale.csv           # Open-source dataset
│
├── app.py                   # Main Streamlit web app
├── app_chatbot.py           # Optional chatbot interface
├── requirements.txt         # All Python dependencies
└── README.md
