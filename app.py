import streamlit as st
import matplotlib.pyplot as plt

from agents.data_agent import DataAgent
from agents.trend_agent import TrendAgent
from agents.insight_agent import InsightAgent
from agents.prediction_agent import PredictionAgent

st.title("Resale Property Prices from 2017")

town = st.text_input("Enter town (optional)")

data_agent = DataAgent()
trend_agent = TrendAgent()
insight_agent = InsightAgent()
pred_agent = PredictionAgent()

if st.button("Run Analysis"):

    # ---------------- LOAD DATA ----------------
    df = data_agent.get_data(town)

    if df.empty:
        st.error("No data found. Try another town or remove filter.")
        st.stop()

    st.write("Rows loaded:", len(df))

    # ---------------- CHART ----------------
    st.subheader("📈 Price Trend")

    fig, ax = plt.subplots()
    ax.plot(df["month"], df["resale_price"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Price")

    st.pyplot(fig)

    st.write("DEBUG: chart done")

    # ---------------- TREND ----------------
    trends = trend_agent.analyze(df)
    st.subheader("📊 Trends")
    st.json(trends)

    st.write("DEBUG: trend done")

    # ---------------- INSIGHT ----------------
    st.subheader("🧠 Insight")

    insight = insight_agent.explain(trends)
    st.write(insight)

    st.write("DEBUG: insight done")

    # ---------------- PREDICTION ----------------
    st.subheader("🔮 Prediction")

    future_price = pred_agent.predict(df)
    st.write(f"Estimated Price (1 year): ${future_price:,.0f}")

    st.write("DEBUG: prediction done")