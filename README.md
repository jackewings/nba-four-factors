## NBA Four Factors Analysis

A portfolio project exploring how the NBA's Four Factors relate to team wins and playoff success (2014–2024).

---

### Overview

This project investigates whether the "Four Factors" of basketball — Effective Field Goal Percentage (eFG%), Turnover Percentage (TOV%), Offensive Rebound Percentage (ORB%), and Free Throw Rate (FT/FGA) — are statistically significant predictors of NBA team wins and playoff appearances in the modern era.

The analysis is presented as an interactive [Streamlit](https://streamlit.io/) web app, with:
- **Background & Visuals:** Explanation of the Four Factors and interactive charts by team
- **Project Walkthrough:** Step-by-step breakdown of the data pipeline, modeling, and results
- **More & Contact:** Links to notebooks, LinkedIn, and GitHub

---

### Features

- 📊 **Interactive Visuals:** Explore team-level averages for wins and each Four Factor (2014–2023)
- 🏆 **Statistical Modeling:** Multiple linear regression (wins) and logistic regression (playoff prediction)
- 📈 **Significance Testing:** t-test and z-test to compare models against baselines
- 📚 **Transparent Workflow:** All data cleaning, EDA, and modeling steps are documented and reproducible
- 🌐 **Deployed App:** Ready to run locally or deploy to Streamlit Community Cloud

---

### Data Source

- [Kaggle: NBA, ABA & BAA Stats](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats) (team-level season summaries, via Basketball Reference)

---

### App Structure

```
nba-four-factors/
├── app/
│   ├── main.py           # Streamlit app entrypoint
│   └── utils/            # Data loading and plotting helpers
├── data/
│   └── processed/        # Cleaned CSVs used by the app
│   └── raw/              # Raw data from Kaggle
├── notebooks/
│   ├── data_cleaning_eda.ipynb
│   └── hypothesis_testing.ipynb
├── pyproject.toml        # Project dependencies
└── README.md
```

---

### Quickstart

1. **Clone the repo:**
	```bash
	git clone https://github.com/jackewings/nba-four-factors.git
	cd nba-four-factors
	```

2. **Install dependencies:**
	(Recommended: use [uv](https://github.com/astral-sh/uv) or pip)
	```bash
	uv pip install -r requirements.txt
	# or
	pip install -r requirements.txt
	```

3. **Run the app locally:**
	```bash
	uv run streamlit run app/main.py
	# or
	streamlit run app/main.py
	```

4. **Explore the notebooks:**
	- [Data Cleaning + EDA](notebooks/data_cleaning_eda.ipynb)
	- [Hypothesis Testing](notebooks/hypothesis_testing.ipynb)

---

### Deployment

You can deploy this app for free on [Streamlit Community Cloud](https://streamlit.io/cloud) or similar platforms. Make sure to include the `data/processed/` CSVs in your repo.

---

### Contact & Links

- **App repo:** [github.com/jackewings/nba-four-factors](https://github.com/jackewings/nba-four-factors)
- **LinkedIn:** [Jack Ewings](https://www.linkedin.com/in/jack-ewings-profile/)
- **Notebooks:** [Data Cleaning + EDA](https://github.com/jackewings/nba-four-factors/blob/main/notebooks/data_cleaning_eda.ipynb) | [Hypothesis Testing](https://github.com/jackewings/nba-four-factors/blob/main/notebooks/hypothesis_testing.ipynb)

---

### License

This project is for educational and portfolio use. Data is provided by third-party sources (see above).
