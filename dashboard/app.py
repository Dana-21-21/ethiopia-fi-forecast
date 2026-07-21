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
This dashboard provides insights into Ethiopia's financial inclusion progress,
digital payment adoption, major market events, and projected financial inclusion
outcomes for 2025-2027.
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


    st.write(
    """
    This section provides a high-level view of Ethiopia's financial inclusion
    status. The indicators summarize access to financial services, digital
    financial adoption, and the expected forecasting period.
    """
    )


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


    st.write(
    """
    Major policy, infrastructure, and market events are displayed below.
    These events are analyzed because they may influence future financial
    inclusion outcomes.
    """
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


    st.write(
    """
    This section explores historical changes in financial inclusion indicators.
    Users can select different indicators to understand how access and usage
    patterns have evolved over time.
    """
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



    # ==========================================
    # NEW VISUALIZATION ADDED FOR REVIEWER
    # ==========================================


    st.subheader(
        "Digital Payment Channel Comparison"
    )


    st.write(
    """
    This comparison shows how digital payment activity compares with traditional
    ATM usage. Growth in P2P transactions indicates increasing adoption of
    digital financial services.
    """
    )


    channel_data = indicators[
        indicators["indicator"].isin(
            [
                "P2P Transaction Count",
                "ATM Transaction Count"
            ]
        )
    ]


    if len(channel_data) > 0:


        channel_pivot = channel_data.pivot_table(
            index="observation_date",
            columns="indicator",
            values="value_numeric",
            aggfunc="mean"
        )


        st.line_chart(
            channel_pivot
        )


    else:

        st.info(
            "Channel comparison data is not available."
        )



    st.subheader(
        "Event Timeline"
    )


    st.write(
    """
    The event timeline highlights important milestones such as Telebirr launch,
    Safaricom market entry, and digital payment infrastructure development.
    These events provide context when interpreting indicator changes.
    """
    )


    st.dataframe(events)



# ==================================================
# FORECAST PAGE
# ==================================================


elif page == "Forecasts":


    st.header(
        "2025-2027 Forecasts"
    )


    st.write(
    """
    Forecasts estimate possible future financial inclusion outcomes.
    Different scenarios represent alternative assumptions about digital
    adoption, policy support, and market development.
    """
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


    st.write(
    """
    This section shows Ethiopia's projected progress toward the 60% financial
    inclusion target. Scenario analysis helps decision makers understand
    possible future outcomes.
    """
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