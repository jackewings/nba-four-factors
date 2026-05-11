import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, precision_score, recall_score, confusion_matrix

st.set_page_config(page_title="NBA Four Factors Analysis", layout="wide")


# --- Load Clean Processed Data ---
@st.cache_data
def load_teams_14_23():
    return pd.read_csv("data/processed/teams_14_23.csv")

@st.cache_data
def load_teams_24():
    return pd.read_csv("data/processed/teams_24.csv")

teams_14_23 = load_teams_14_23()
teams_24 = load_teams_24()

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["Dashboard", "Writeup", "Notebook"])

with tab1:
    st.title("NBA Four Factors: Dashboard")
    st.write("Explore the relationship between the Four Factors and team success in the NBA (2014-2024).")

    viz = st.selectbox(
        "Select a visualization:",
        [
            "Average Wins per Team",
            "Average EFG% per Team",
            "Average Turnover% per Team",
            "Average Offensive Rebound% per Team",
            "Average Free Throw Rate per Team",
            "Confusion Matrix (Playoff Prediction)"
        ]
    )

    if viz == "Average Wins per Team":
        teams_avg_wins = teams_14_23.groupby("abbreviation")["w"].mean().sort_values(ascending=False).reset_index()
        fig, ax = plt.subplots(figsize=(12, 4))
        sns.barplot(data=teams_avg_wins, x="abbreviation", y="w", palette="coolwarm_r", ax=ax)
        ax.set_ylim(25, 55)
        ax.set_title("Average Wins per Season by Team")
        st.pyplot(fig)

    elif viz == "Average EFG% per Team":
        teams_avg_efg = teams_14_23.groupby("abbreviation")["e_fg_percent"].mean().sort_values(ascending=False).reset_index()
        fig, ax = plt.subplots(figsize=(12, 4))
        sns.barplot(data=teams_avg_efg, x="abbreviation", y="e_fg_percent", palette="coolwarm_r", ax=ax)
        ax.set_ylim(48, 55)
        ax.set_title("Average EFG% by Team")
        st.pyplot(fig)

    elif viz == "Average Turnover% per Team":
        teams_avg_tov = teams_14_23.groupby("abbreviation")["tov_percent"].mean().sort_values(ascending=True).reset_index()
        fig, ax = plt.subplots(figsize=(12, 4))
        sns.barplot(data=teams_avg_tov, x="abbreviation", y="tov_percent", palette="coolwarm_r", ax=ax)
        ax.set_ylim(11, 14)
        ax.set_title("Average Turnover% by Team")
        st.pyplot(fig)

    elif viz == "Average Offensive Rebound% per Team":
        teams_avg_orb = teams_14_23.groupby("abbreviation")["orb_percent"].mean().sort_values(ascending=False).reset_index()
        fig, ax = plt.subplots(figsize=(12, 4))
        sns.barplot(data=teams_avg_orb, x="abbreviation", y="orb_percent", palette="coolwarm_r", ax=ax)
        ax.set_ylim(20, 26)
        ax.set_title("Average Offensive Rebound% by Team")
        st.pyplot(fig)

    elif viz == "Average Free Throw Rate per Team":
        teams_avg_ftr = teams_14_23.groupby("abbreviation")["ft_fga"].mean().sort_values(ascending=False).reset_index()
        fig, ax = plt.subplots(figsize=(12, 4))
        sns.barplot(data=teams_avg_ftr, x="abbreviation", y="ft_fga", palette="coolwarm_r", ax=ax)
        ax.set_ylim(18, 23)
        ax.set_title("Average Free Throw Rate by Team")
        st.pyplot(fig)

    elif viz == "Confusion Matrix (Playoff Prediction)":
        # Logistic regression model
        X = teams_14_23[["e_fg_percent", "tov_percent", "orb_percent", "ft_fga"]]
        X = sm.add_constant(X)
        y = teams_14_23["playoffs"]
        logit = sm.Logit(y, X).fit(disp=0)
        X_test = teams_24[["e_fg_percent", "tov_percent", "orb_percent", "ft_fga"]]
        X_test = sm.add_constant(X_test)
        y_test = teams_24["playoffs"]
        y_pred_probs = logit.predict(X_test)
        y_pred_classes = np.where(y_pred_probs > 0.8, 1, 0)
        conf_mat = confusion_matrix(y_test, y_pred_classes)
        fig, ax = plt.subplots()
        sns.heatmap(conf_mat, annot=True, fmt="d", cmap="Blues", xticklabels=["No Playoffs", "Playoffs"], yticklabels=["No Playoffs", "Playoffs"], ax=ax)
        ax.set_title("Confusion Matrix for Playoff Prediction (2024)")
        ax.set_ylabel("Actual")
        ax.set_xlabel("Predicted")
        st.pyplot(fig)
        st.write(f"Accuracy: {accuracy_score(y_test, y_pred_classes):.2f}")
        st.write(f"Precision: {precision_score(y_test, y_pred_classes):.2f}")
        st.write(f"Recall: {recall_score(y_test, y_pred_classes):.2f}")

with tab2:
    st.title("Project Writeup & Findings")
    st.markdown("""
**Objective:**  
To determine if the NBA Four Factors (effective field goal %, turnover %, offensive rebound %, and free throw rate) are significant predictors of team wins and playoff appearances.

**Methods:**  
- Multi Linear Regression for wins
- Logistic Regression for playoff prediction
- Statistical tests (t-test, z-test) to compare model vs. baseline

**Key Results:**  
- The Four Factors explain about 30% of the variance in team wins (R² = 0.30).
- All Four Factors are statistically significant predictors (p < 0.05).
- Logistic regression correctly predicted playoff status for 83% of teams in 2024.
- Both models outperformed their baselines at the 5% significance level.

**Conclusion:**  
The Four Factors are significant predictors of NBA team success and should be used for performance analysis and prediction.

---
For more details, see the full notebook below.
""")

with tab3:
    st.title("Full Notebook & Code")
    st.markdown("""
- [View the full project on GitHub](https://github.com/jackewings/nba-four-factors/tree/main)
""")