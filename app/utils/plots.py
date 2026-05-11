from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_team_bar(
    data: pd.DataFrame,
    *,
    value_col: str,
    title: str,
    y_label: str,
    y_lim=None,
    sort_ascending: bool = False,
):
    plotted = (
        data.groupby("abbreviation")[value_col]
        .mean()
        .sort_values(ascending=sort_ascending)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(14, 5))
    sns.barplot(
        data=plotted,
        x="abbreviation",
        y=value_col,
        hue="abbreviation",
        palette="coolwarm_r",
        ax=ax,
        legend=False,
    )
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel("Team")
    ax.set_ylabel(y_label)
    if y_lim is not None:
        ax.set_ylim(*y_lim)

    ax.tick_params(axis="x", labelrotation=45)
    for label in ax.get_xticklabels():
        label.set_horizontalalignment("right")

    fig.tight_layout()
    return fig
