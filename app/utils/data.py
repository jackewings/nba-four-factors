from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st


def _repo_root() -> Path:
    # app/utils/data.py -> parents[2] is repo root
    return Path(__file__).resolve().parents[2]


@st.cache_data
def load_teams_14_23() -> pd.DataFrame:
    return pd.read_csv(_repo_root() / "data" / "processed" / "teams_14_23.csv")


@st.cache_data
def load_teams_24() -> pd.DataFrame:
    return pd.read_csv(_repo_root() / "data" / "processed" / "teams_24.csv")
