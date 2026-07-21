import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ==============================
# PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    layout="wide"
)


# ==============================
# LOAD DATA
# ==============================


@st.cache_data
def load_data():

    indicators = pd.read_csv(
        "dashboard/data/indicators.csv"
    )

    forecast = pd.read_csv(
        "dashboard/data/forecast.csv"
    )

    events = pd.read_csv(
        "dashboard/data/events.csv"
    )


    indicators["observation_date"] = pd.to_datetime(
        indicators["observation_date"]
    )

    events["observation_date"] = pd.to_datetime(
        events["observation_date"]
    )


    return indicators, forecast, events



indicators, forecast, events = load_data()



# ==============================
# TITLE
# ==============================


st.title(
    "Ethiopia Financial Inclusion Dashboard"
)


st.write(
"""
This dashboard provides insights into Ethiopia's financial
inclusion progress, digital payment adoption, event impacts,
and 2025-2027 projections.
"""
)



# ==============================
# SIDEBAR
# ==============================


page = st.sidebar.selectbox(
    "Navigation",
    [
        "Overview",
        "Trends",
        "Forecasts",
        "Inclusion Projection"
    ]
)



# ==================================================
# OVERVIEW PAGE
# ==================================================


if page == "Overview":


    st.header("Financial Inclusion Overview")


    ownership = indicators[
        indicators["indicator_code"]
        ==
        "ACC_OWNERSHIP"
    ]


    mobile_money = indicators[
        indicators["indicator_code"]
        ==
        "ACC_MM_ACCOUNT"
    ]



    col1, col2, col3 = st.columns(3)



    with col1:

        if len(ownership)>0:

            latest = ownership.sort_values(
                "observation_date"
            ).iloc[-1]["value_numeric"]

            st.metric(
                "Account Ownership",
                f"{latest}%"
            )


    with col2:

        if len(mobile_money)>0:

            latest_mm = mobile_money.sort_values(
                "observation_date"
            ).iloc[-1]["value_numeric"]


            st.metric(
                "Mobile Money Accounts",
                f"{latest_mm}%"
            )



    with col3:

        st.metric(
            "Forecast Horizon",
            "2025-2027"
        )




    st.subheader(
        "Key Events"
    )


    st.dataframe(
        events
    )



# ==================================================
# TRENDS PAGE
# ==================================================


elif page == "Trends":


    st.header(
        "Financial Inclusion Trends"
    )


    selected_indicator = st.selectbox(

        "Choose Indicator",

        indicators["indicator"].unique()

    )



    data = indicators[
        indicators["indicator"]
        ==
        selected_indicator
    ]



    fig, ax = plt.subplots(figsize=(10,5))


    ax.plot(
        data["observation_date"],
        data["value_numeric"],
        marker="o"
    )


    ax.set_title(
        selected_indicator
    )


    ax.set_xlabel(
        "Year"
    )


    ax.set_ylabel(
        "Value"
    )


    plt.xticks(rotation=45)


    st.pyplot(fig)



    st.subheader(
        "Event Timeline"
    )


    st.dataframe(events)



# ==================================================
# FORECAST PAGE
# ==================================================


elif page == "Forecasts":


    st.header(
        "2025-2027 Forecasts"
    )


    scenario = st.selectbox(

        "Select Scenario",

        [
            "base",
            "optimistic",
            "pessimistic"
        ]

    )


    fig, ax = plt.subplots(
        figsize=(10,5)
    )


    ax.plot(

        forecast["year"],

        forecast[scenario],

        marker="o"

    )


    ax.set_title(

        f"{scenario.title()} Scenario Forecast"

    )


    ax.set_xlabel(
        "Year"
    )


    ax.set_ylabel(
        "Financial Inclusion (%)"
    )


    st.pyplot(fig)



    st.subheader(
        "Forecast Table"
    )


    st.dataframe(
        forecast
    )



# ==================================================
# PROJECTION PAGE
# ==================================================


elif page == "Inclusion Projection":


    st.header(
        "Progress Toward 60% Inclusion Target"
    )


    target = 60


    latest_forecast = forecast.iloc[-1]


    value = latest_forecast["base"]



    progress = value / target



    st.progress(
        min(progress,1)
    )



    st.write(

        f"""
        Projected inclusion rate in 2027:

        **{value:.2f}%**

        Target:

        **{target}%**

        """
    )



    st.subheader(
        "Scenario Comparison"
    )


    st.bar_chart(

        forecast.set_index("year")
        [
            [
                "optimistic",
                "base",
                "pessimistic"
            ]
        ]

    )



# ==============================
# DOWNLOAD DATA
# ==============================


st.sidebar.subheader(
    "Download Data"
)


csv = indicators.to_csv(
    index=False
)



st.sidebar.download_button(

    label="Download Indicators",

    data=csv,

    file_name="financial_inclusion_data.csv",

    mime="text/csv"

)