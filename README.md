# CGP-IA – Intelligenza Artificiale per la Valutazione della Performance nella PA

CGP-IA è una web application sviluppata in Python con Streamlit per supportare il **Ciclo di Gestione della Performance (CGP)** nella Pubblica Amministrazione, integrando tecniche di **intelligenza artificiale**, **valutazione automatica dei rischi**, e **reportistica digitale**.

## 🚀 Funzionalità principali

- 📥 Upload CSV con KPI degli enti
- 🤖 Analisi predittiva automatica con modello Random Forest
- 📉 Identificazione enti a rischio
- 📌 Visualizzazione dell’importanza delle variabili (trasparenza AI)
- 📝 Generazione di report PDF scaricabili
- 🌐 Interfaccia web accessibile via browser

## 📦 Contenuto del progetto

- `app.py`: Interfaccia web Streamlit
- `model.joblib`: Modello IA già addestrato
- `data/kpi_input.csv`: Dataset di esempio
- `reports/feature_importance.png`: Grafico variabili
- `scripts/train_model.py`: Codice per addestramento IA
- `requirements.txt`: Librerie necessarie per il deploy

## ▶️ Esecuzione locale

```bash
pip install -r requirements.txt
streamlit run app.py
