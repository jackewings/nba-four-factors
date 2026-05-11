import streamlit as st

from utils.data import load_teams_14_23, load_teams_24
from utils.plots import plot_team_bar


st.set_page_config(page_title="NBA Four Factors Analysis", layout="wide")


st.title("NBA Four Factors Analysis")
st.caption("A portfolio project exploring how the Four Factors relate to wins and playoff success (2014–2024).")

teams_14_23 = load_teams_14_23()
teams_24 = load_teams_24()

# --- Tabs ---
tab1, tab2, tab3 = st.tabs([
    "Background & Visuals",
    "Project Walkthrough",
    "More & Contact"
])

# --- Tab 1: Background & Visuals ---
with tab1:
    st.title("NBA Four Factors: Background & Exploratory Visuals")
    st.markdown(
        """
**What are the Four Factors?**

The NBA Four Factors are a set of team-level statistics commonly used in basketball analytics to explain *why* teams win:

- **Effective Field Goal Percentage (eFG%)**: Adjusts FG% to account for the added value of 3-point shots.
- **Turnover Percentage (TOV%)**: Percent of possessions that end in a turnover (lower is better).
- **Offensive Rebound Percentage (ORB%)**: Percent of available offensive rebounds a team gets.
- **Free Throw Rate (FT/FGA)**: Free throws made per 100 field goal attempts.

**What inspired this project**

I wanted a portfolio project that combines sports + statistics and answers a real “basketball analytics” question with measurable evidence.

**Main goal**

Use modern NBA team data (2014–2023) to test whether the Four Factors are statistically significant predictors of:

- Regular-season wins (regression)
- Playoff appearance (classification)
"""
    )

    st.caption("Charts use team-season data from the 2014–2023 seasons and show averages by team.")

    selected_chart = st.selectbox(
        "Select a chart",
        [
            "Average wins (2014–2023)",
            "Average eFG% (2014–2023)",
            "Average TOV% (2014–2023)",
            "Average ORB% (2014–2023)",
            "Average FT/FGA (2014–2023)",
        ],
    )

    if selected_chart == "Average wins (2014–2023)":
        st.subheader("Average wins by team")
        st.pyplot(
            plot_team_bar(
                teams_14_23,
                value_col="w",
                title="Average Regular-Season Wins by Team (2014–2023)",
                y_label="Average wins",
                y_lim=(25, 55),
                sort_ascending=False,
            )
        )

    elif selected_chart == "Average eFG% (2014–2023)":
        st.subheader("Average eFG% by team")
        st.pyplot(
            plot_team_bar(
                teams_14_23,
                value_col="e_fg_percent",
                title="Average Effective Field Goal Percentage (eFG%) by Team (2014–2023)",
                y_label="Average eFG%",
                y_lim=(48, 55),
                sort_ascending=False,
            )
        )

    elif selected_chart == "Average TOV% (2014–2023)":
        st.subheader("Average TOV% by team")
        st.pyplot(
            plot_team_bar(
                teams_14_23,
                value_col="tov_percent",
                title="Average Turnover Percentage (TOV%) by Team (2014–2023)",
                y_label="Average TOV%",
                y_lim=(11, 14),
                sort_ascending=True,
            )
        )

    elif selected_chart == "Average ORB% (2014–2023)":
        st.subheader("Average ORB% by team")
        st.pyplot(
            plot_team_bar(
                teams_14_23,
                value_col="orb_percent",
                title="Average Offensive Rebound Percentage (ORB%) by Team (2014–2023)",
                y_label="Average ORB%",
                y_lim=(20, 26),
                sort_ascending=False,
            )
        )

    elif selected_chart == "Average FT/FGA (2014–2023)":
        st.subheader("Average FT/FGA by team")
        st.pyplot(
            plot_team_bar(
                teams_14_23,
                value_col="ft_fga",
                title="Average Free Throw Rate (FT/FGA) by Team (2014–2023)",
                y_label="Average FT/FGA (per 100 FGA)",
                y_lim=(18, 23),
                sort_ascending=False,
            )
        )

# --- Tab 2: Project Walkthrough ---
with tab2:
    st.title("Project Walkthrough: From Data to Results")
    st.markdown(
        """
This section documents the full end-to-end workflow, from raw data to results.

Two notebooks in this repo mirror the process:

- **Data cleaning + EDA** (creates the processed CSVs)
- **Hypothesis testing + modeling** (fits models, evaluates on 2024, runs significance tests)
"""
    )

    with st.expander("1) Data source & scope", expanded=True):
        st.markdown(
            """
**Dataset**

Source: [Kaggle — NBA, ABA & BAA Stats](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats)

This project uses **NBA team-level season summaries**.

**Time window**

- Primary analysis window: **2014–2023**
- Holdout test season: **2024**
"""
        )

    with st.expander("2) Data ingestion", expanded=False):
        st.markdown(
            """
The raw CSV was loaded into pandas and filtered to the seasons/rows relevant to the analysis.

Filtering choices:

- keep NBA team rows in the selected seasons
- drop the `League Average` row
"""
        )
        st.code(
            '''
df = pd.read_csv("../data/raw/team_summaries.csv")

teams_14_23 = df[
    (df["season"] >= 2014)
    & (df["season"] < 2024)
    & (df["team"] != "League Average")
].copy()
''',
            language="python",
        )

    with st.expander("3) Cleaning & preprocessing", expanded=False):
        st.markdown(
            """
Key preprocessing steps:

- **Data quality checks**: looked for duplicates and missing values.
- **Playoff labels**: corrected playoff flags for seasons where the raw dataset was inconsistent.
- **Model-ready target**: converted `playoffs` to an integer (1/0).
- **Feature consistency**: scaled `e_fg_percent` and `ft_fga` so the Four Factors are on comparable “percent-like” scales.

Finally, I saved processed outputs so the Streamlit app and modeling notebook can load clean data instantly.
"""
        )
        st.code(
            '''
teams_14_23.to_csv("../data/processed/teams_14_23.csv", index=False)
teams_24.to_csv("../data/processed/teams_24.csv", index=False)
''',
            language="python",
        )

    with st.expander("4) EDA (exploratory data analysis)", expanded=False):
        st.markdown(
            """
In EDA, I focused on two things:

1) understanding the distribution of wins and Four Factors by team
2) sanity-checking that the numbers looked realistic before modeling

The dropdown charts in Tab 1 are a condensed version of that exploration.
"""
        )

    with st.expander("5) Modeling", expanded=False):
        st.markdown(
            """
I built two models because the outcomes are different types:

**A) Predict wins (continuous target)**

- Model: Multiple Linear Regression (OLS)
- Target: `w`

**B) Predict playoffs (binary target)**

- Model: Logistic Regression
- Target: `playoffs` (1/0)

Features for both models:

- `e_fg_percent`, `tov_percent`, `orb_percent`, `ft_fga`

Train/evaluate split:

- Train on 2014–2023
- Evaluate on 2024
"""
        )
        st.code(
            '''
FEATURES = ["e_fg_percent", "tov_percent", "orb_percent", "ft_fga"]

# Wins regression
X_train = teams_14_23[FEATURES]
y_train = teams_14_23["w"]

# Playoff classification
X_train = teams_14_23[FEATURES]
y_train = teams_14_23["playoffs"]
''',
            language="python",
        )

    with st.expander("6) Evaluation + hypothesis testing", expanded=False):
        st.markdown(
            """
I evaluated on the 2024 holdout season using standard metrics.

To strengthen the conclusion, I also compared each model against a simple baseline and ran a statistical test:

- **Wins**: compared absolute errors vs a baseline that predicts the mean wins for every team; used a one-sample t-test on error differences.
- **Playoffs**: compared accuracy vs a baseline; used a proportions z-test.
"""
        )

    with st.expander("7) Results (holdout 2024)", expanded=True):
        st.markdown(
            """
**Wins model**

- RMSE ≈ **11.0**
- $R^2$ ≈ **0.30**
- Baseline comparison (t-test): p-value ≈ **0.034**

**Playoff model**

- Accuracy ≈ **0.83**
- Baseline comparison (z-test): p-value ≈ **0.006**

Overall: in this dataset/time window, the Four Factors show up as statistically significant predictors of both wins and playoff success.
"""
        )

    with st.expander("8) Limitations & future improvements", expanded=False):
        st.markdown(
            """
Limitations:

- Team-season data compresses a lot of information (pace, injuries, roster changes)
- The Four Factors are correlated with each other and with other team metrics
- Expand the test set to multiple seasons for more robust evaluation

Future improvements:

- Evaluate with rolling seasons (time-series style validation)
- Add defensive Four Factors (opponent stats)
- Add calibration/ROC for the playoff classifier
"""
        )

# --- Tab 3: More & Contact ---
with tab3:
    st.title("More & Contact")
    st.markdown("""
- [View the full project repo](https://github.com/jackewings/nba-four-factors)
- Notebooks: [Data Cleaning + EDA](https://github.com/jackewings/nba-four-factors/blob/main/notebooks/data_cleaning_eda.ipynb) | [Hypothesis Testing](https://github.com/jackewings/nba-four-factors/blob/main/notebooks/hypothesis_testing.ipynb)
- [Connect on LinkedIn](https://www.linkedin.com/in/jack-ewings-profile/)
- GitHub: [@jackewings](https://github.com/jackewings)
""")