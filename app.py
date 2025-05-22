import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from sklearn.ensemble import RandomForestClassifier
from joblib import load
from reportlab.pdfgen import canvas

st.set_page_config(page_title="CGP-IA", layout="centered")
st.title("🔍 CGP-IA: Analisi automatica della performance")

# Caricamento modello
model = load("model.joblib")

file = st.file_uploader("📤 Carica un file CSV con KPI", type=["csv"])
if file:
    df = pd.read_csv(file)

    st.subheader("📊 Dati caricati")
    st.dataframe(df)

    if all(col in df.columns for col in ['kpi1', 'kpi2', 'kpi3']):
        X = df[['kpi1', 'kpi2', 'kpi3']]
        df['rischio'] = model.predict(X)

        st.subheader("📉 Analisi del rischio")
        st.bar_chart(df['rischio'].value_counts())

        st.subheader("📍 Enti a rischio")
        rischiosi = df[df['rischio'] == 0]
        st.dataframe(rischiosi[['ente', 'kpi1', 'kpi2', 'kpi3']])

        # Visualizzazione grafico delle feature importance
        st.subheader("📌 Spiegazione del modello")
        st.image("reports/feature_importance.png", caption="Importanza delle variabili", use_column_width=True)

        # PDF dinamico in memoria
        buffer = BytesIO()
        c = canvas.Canvas(buffer)
        c.drawString(100, 800, "Report Performance Generato con CGP-IA")
        y = 760
        for i, row in rischiosi.iterrows():
            c.drawString(100, y, f"{row['ente']} - KPI: {row['kpi1']}, {row['kpi2']}, {row['kpi3']}")
            y -= 20
        c.save()
        buffer.seek(0)
        b64 = base64.b64encode(buffer.read()).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="report_performance.pdf">📥 Scarica Report PDF</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.error("❗ Il file deve contenere le colonne: kpi1, kpi2, kpi3.")
