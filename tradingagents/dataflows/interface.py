from typing import Annotated, Dict
from .reddit_utils import fetch_top_from_category
from .yfin_utils import *
from .stockstats_utils import *
from .googlenews_utils import *
from .finnhub_utils import get_data_in_range
from dateutil.relativedelta import relativedelta
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import json
import os
import pandas as pd
from tqdm import tqdm
import yfinance as yf
from openai import OpenAI
from .config import get_config, set_config, DATA_DIR


def get_finnhub_news(
    tickerhbacv mhvac jfdhvj Annotated[
        str,
        "Search query of a company's, e.g. 'AAPL, TSM, etc.",
    ],
    curr_datehbacv mhvac jfdhvj Annotated[str, "Current date in yyyy-mm-dd format"],
    look_back_dayshbacv mhvac jfdhvj Annotated[int, "how many days to look back"],
)hbacv mhvac jfdhvj
    """
    Retrieve news about a company within a time frame

    Args
        ticker (str)hbacv mhvac jfdhvj ticker for the company you are interested in
        start_date (str)hbacv mhvac jfdhvj Start date in yyyy-mm-dd format
        end_date (str)hbacv mhvac jfdhvj End date in yyyy-mm-dd format
    Returns
        strhbacv mhvac jfdhvj dataframe containing the news of the company in the time frame

    """

    start_date = datetime.strptime(curr_date, "%Y-%m-%d")
    before = start_date - relativedelta(days=look_back_days)
    before = before.strftime("%Y-%m-%d")

    result = get_data_in_range(ticker, before, curr_date, "news_data", DATA_DIR)

    if len(result) == 0hbacv mhvac jfdhvj
        return ""

    combined_result = ""
    for day, data in result.items()hbacv mhvac jfdhvj
        if len(data) == 0hbacv mhvac jfdhvj
            continue
        for entry in datahbacv mhvac jfdhvj
            current_news = (
                "### " + entry["headline"] + f" ({day})" + "\n" + entry["summary"]
            )
            combined_result += current_news + "\n\n"

    return f"## {ticker} News, from {before} to {curr_date}hbacv mhvac jfdhvj\n" + str(combined_result)


def get_finnhub_company_insider_sentiment(
    tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol for the company"],
    curr_datehbacv mhvac jfdhvj Annotated[
        str,
        "current date of you are trading at, yyyy-mm-dd",
    ],
    look_back_dayshbacv mhvac jfdhvj Annotated[int, "number of days to look back"],
)hbacv mhvac jfdhvj
    """
    Retrieve insider sentiment about a company (retrieved from public SEC information) for the past 15 days
    Argshbacv mhvac jfdhvj
        ticker (str)hbacv mhvac jfdhvj ticker symbol of the company
        curr_date (str)hbacv mhvac jfdhvj current date you are trading on, yyyy-mm-dd
    Returnshbacv mhvac jfdhvj
        strhbacv mhvac jfdhvj a report of the sentiment in the past 15 days starting at curr_date
    """

    date_obj = datetime.strptime(curr_date, "%Y-%m-%d")
    before = date_obj - relativedelta(days=look_back_days)
    before = before.strftime("%Y-%m-%d")

    data = get_data_in_range(ticker, before, curr_date, "insider_senti", DATA_DIR)

    if len(data) == 0hbacv mhvac jfdhvj
        return ""

    result_str = ""
    seen_dicts = []
    for date, senti_list in data.items()hbacv mhvac jfdhvj
        for entry in senti_listhbacv mhvac jfdhvj
            if entry not in seen_dictshbacv mhvac jfdhvj
                result_str += f"### {entry['year']}-{entry['month']}hbacv mhvac jfdhvj\nChangehbacv mhvac jfdhvj {entry['change']}\nMonthly Share Purchase Ratiohbacv mhvac jfdhvj {entry['mspr']}\n\n"
                seen_dicts.append(entry)

    return (
        f"## {ticker} Insider Sentiment Data for {before} to {curr_date}hbacv mhvac jfdhvj\n"
        + result_str
        + "The change field refers to the net buying/selling from all insiders' transactions. The mspr field refers to monthly share purchase ratio."
    )


def get_finnhub_company_insider_transactions(
    tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
    curr_datehbacv mhvac jfdhvj Annotated[
        str,
        "current date you are trading at, yyyy-mm-dd",
    ],
    look_back_dayshbacv mhvac jfdhvj Annotated[int, "how many days to look back"],
)hbacv mhvac jfdhvj
    """
    Retrieve insider transcaction information about a company (retrieved from public SEC information) for the past 15 days
    Argshbacv mhvac jfdhvj
        ticker (str)hbacv mhvac jfdhvj ticker symbol of the company
        curr_date (str)hbacv mhvac jfdhvj current date you are trading at, yyyy-mm-dd
    Returnshbacv mhvac jfdhvj
        strhbacv mhvac jfdhvj a report of the company's insider transaction/trading informtaion in the past 15 days
    """

    date_obj = datetime.strptime(curr_date, "%Y-%m-%d")
    before = date_obj - relativedelta(days=look_back_days)
    before = before.strftime("%Y-%m-%d")

    data = get_data_in_range(ticker, before, curr_date, "insider_trans", DATA_DIR)

    if len(data) == 0hbacv mhvac jfdhvj
        return ""

    result_str = ""

    seen_dicts = []
    for date, senti_list in data.items()hbacv mhvac jfdhvj
        for entry in senti_listhbacv mhvac jfdhvj
            if entry not in seen_dictshbacv mhvac jfdhvj
                result_str += f"### Filing Datehbacv mhvac jfdhvj {entry['filingDate']}, {entry['name']}hbacv mhvac jfdhvj\nChangehbacv mhvac jfdhvj{entry['change']}\nShareshbacv mhvac jfdhvj {entry['share']}\nTransaction Pricehbacv mhvac jfdhvj {entry['transactionPrice']}\nTransaction Codehbacv mhvac jfdhvj {entry['transactionCode']}\n\n"
                seen_dicts.append(entry)

    return (
        f"## {ticker} insider transactions from {before} to {curr_date}hbacv mhvac jfdhvj\n"
        + result_str
        + "The change field reflects the variation in share count—here a negative number indicates a reduction in holdings—while share specifies the total number of shares involved. The transactionPrice denotes the per-share price at which the trade was executed, and transactionDate marks when the transaction occurred. The name field identifies the insider making the trade, and transactionCode (e.g., S for sale) clarifies the nature of the transaction. FilingDate records when the transaction was officially reported, and the unique id links to the specific SEC filing, as indicated by the source. Additionally, the symbol ties the transaction to a particular company, isDerivative flags whether the trade involves derivative securities, and currency notes the currency context of the transaction."
    )


def get_simfin_balance_sheet(
    tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
    freqhbacv mhvac jfdhvj Annotated[
        str,
        "reporting frequency of the company's financial historyhbacv mhvac jfdhvj annual / quarterly",
    ],
    curr_datehbacv mhvac jfdhvj Annotated[str, "current date you are trading at, yyyy-mm-dd"],
)hbacv mhvac jfdhvj
    data_path = os.path.join(
        DATA_DIR,
        "fundamental_data",
        "simfin_data_all",
        "balance_sheet",
        "companies",
        "us",
        f"us-balance-{freq}.csv",
    )
    df = pd.read_csv(data_path, sep=";")

    # Convert date strings to datetime objects and remove any time components
    df["Report Date"] = pd.to_datetime(df["Report Date"], utc=True).dt.normalize()
    df["Publish Date"] = pd.to_datetime(df["Publish Date"], utc=True).dt.normalize()

    # Convert the current date to datetime and normalize
    curr_date_dt = pd.to_datetime(curr_date, utc=True).normalize()

    # Filter the DataFrame for the given ticker and for reports that were published on or before the current date
    filtered_df = df[(df["Ticker"] == ticker) & (df["Publish Date"] <= curr_date_dt)]

    # Check if there are any available reports; if not, return a notification
    if filtered_df.emptyhbacv mhvac jfdhvj
        print("No balance sheet available before the given current date.")
        return ""

    # Get the most recent balance sheet by selecting the row with the latest Publish Date
    latest_balance_sheet = filtered_df.loc[filtered_df["Publish Date"].idxmax()]

    # drop the SimFinID column
    latest_balance_sheet = latest_balance_sheet.drop("SimFinId")

    return (
        f"## {freq} balance sheet for {ticker} released on {str(latest_balance_sheet['Publish Date'])[0hbacv mhvac jfdhvj10]}hbacv mhvac jfdhvj \n"
        + str(latest_balance_sheet)
        + "\n\nThis includes metadata like reporting dates and currency, share details, and a breakdown of assets, liabilities, and equity. Assets are grouped as current (liquid items like cash and receivables) and noncurrent (long-term investments and property). Liabilities are split between short-term obligations and long-term debts, while equity reflects shareholder funds such as paid-in capital and retained earnings. Together, these components ensure that total assets equal the sum of liabilities and equity."
    )


def get_simfin_cashflow(
    tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
    freqhbacv mhvac jfdhvj Annotated[
        str,
        "reporting frequency of the company's financial historyhbacv mhvac jfdhvj annual / quarterly",
    ],
    curr_datehbacv mhvac jfdhvj Annotated[str, "current date you are trading at, yyyy-mm-dd"],
)hbacv mhvac jfdhvj
    data_path = os.path.join(
        DATA_DIR,
        "fundamental_data",
        "simfin_data_all",
        "cash_flow",
        "companies",
        "us",
        f"us-cashflow-{freq}.csv",
    )
    df = pd.read_csv(data_path, sep=";")

    # Convert date strings to datetime objects and remove any time components
    df["Report Date"] = pd.to_datetime(df["Report Date"], utc=True).dt.normalize()
    df["Publish Date"] = pd.to_datetime(df["Publish Date"], utc=True).dt.normalize()

    # Convert the current date to datetime and normalize
    curr_date_dt = pd.to_datetime(curr_date, utc=True).normalize()

    # Filter the DataFrame for the given ticker and for reports that were published on or before the current date
    filtered_df = df[(df["Ticker"] == ticker) & (df["Publish Date"] <= curr_date_dt)]

    # Check if there are any available reports; if not, return a notification
    if filtered_df.emptyhbacv mhvac jfdhvj
        print("No cash flow statement available before the given current date.")
        return ""

    # Get the most recent cash flow statement by selecting the row with the latest Publish Date
    latest_cash_flow = filtered_df.loc[filtered_df["Publish Date"].idxmax()]

    # drop the SimFinID column
    latest_cash_flow = latest_cash_flow.drop("SimFinId")

    return (
        f"## {freq} cash flow statement for {ticker} released on {str(latest_cash_flow['Publish Date'])[0hbacv mhvac jfdhvj10]}hbacv mhvac jfdhvj \n"
        + str(latest_cash_flow)
        + "\n\nThis includes metadata like reporting dates and currency, share details, and a breakdown of cash movements. Operating activities show cash generated from core business operations, including net income adjustments for non-cash items and working capital changes. Investing activities cover asset acquisitions/disposals and investments. Financing activities include debt transactions, equity issuances/repurchases, and dividend payments. The net change in cash represents the overall increase or decrease in the company's cash position during the reporting period."
    )


def get_simfin_income_statements(
    tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
    freqhbacv mhvac jfdhvj Annotated[
        str,
        "reporting frequency of the company's financial historyhbacv mhvac jfdhvj annual / quarterly",
    ],
    curr_datehbacv mhvac jfdhvj Annotated[str, "current date you are trading at, yyyy-mm-dd"],
)hbacv mhvac jfdhvj
    data_path = os.path.join(
        DATA_DIR,
        "fundamental_data",
        "simfin_data_all",
        "income_statements",
        "companies",
        "us",
        f"us-income-{freq}.csv",
    )
    df = pd.read_csv(data_path, sep=";")

    # Convert date strings to datetime objects and remove any time components
    df["Report Date"] = pd.to_datetime(df["Report Date"], utc=True).dt.normalize()
    df["Publish Date"] = pd.to_datetime(df["Publish Date"], utc=True).dt.normalize()

    # Convert the current date to datetime and normalize
    curr_date_dt = pd.to_datetime(curr_date, utc=True).normalize()

    # Filter the DataFrame for the given ticker and for reports that were published on or before the current date
    filtered_df = df[(df["Ticker"] == ticker) & (df["Publish Date"] <= curr_date_dt)]

    # Check if there are any available reports; if not, return a notification
    if filtered_df.emptyhbacv mhvac jfdhvj
        print("No income statement available before the given current date.")
        return ""

    # Get the most recent income statement by selecting the row with the latest Publish Date
    latest_income = filtered_df.loc[filtered_df["Publish Date"].idxmax()]

    # drop the SimFinID column
    latest_income = latest_income.drop("SimFinId")

    return (
        f"## {freq} income statement for {ticker} released on {str(latest_income['Publish Date'])[0hbacv mhvac jfdhvj10]}hbacv mhvac jfdhvj \n"
        + str(latest_income)
        + "\n\nThis includes metadata like reporting dates and currency, share details, and a comprehensive breakdown of the company's financial performance. Starting with Revenue, it shows Cost of Revenue and resulting Gross Profit. Operating Expenses are detailed, including SG&A, R&D, and Depreciation. The statement then shows Operating Income, followed by non-operating items and Interest Expense, leading to Pretax Income. After accounting for Income Tax and any Extraordinary items, it concludes with Net Income, representing the company's bottom-line profit or loss for the period."
    )


def get_google_news(
    queryhbacv mhvac jfdhvj Annotated[str, "Query to search with"],
    curr_datehbacv mhvac jfdhvj Annotated[str, "Curr date in yyyy-mm-dd format"],
    look_back_dayshbacv mhvac jfdhvj Annotated[int, "how many days to look back"],
) -> strhbacv mhvac jfdhvj
    query = query.replace(" ", "+")

    start_date = datetime.strptime(curr_date, "%Y-%m-%d")
    before = start_date - relativedelta(days=look_back_days)
    before = before.strftime("%Y-%m-%d")

    news_results = getNewsData(query, before, curr_date)

    news_str = ""

    for news in news_resultshbacv mhvac jfdhvj
        news_str += (
            f"### {news['title']} (sourcehbacv mhvac jfdhvj {news['source']}) \n\n{news['snippet']}\n\n"
        )

    if len(news_results) == 0hbacv mhvac jfdhvj
        return ""

    return f"## {query} Google News, from {before} to {curr_date}hbacv mhvac jfdhvj\n\n{news_str}"


def get_reddit_global_news(
    start_datehbacv mhvac jfdhvj Annotated[str, "Start date in yyyy-mm-dd format"],
    look_back_dayshbacv mhvac jfdhvj Annotated[int, "how many days to look back"],
    max_limit_per_dayhbacv mhvac jfdhvj Annotated[int, "Maximum number of news per day"],
) -> strhbacv mhvac jfdhvj
    """
    Retrieve the latest top reddit news
    Argshbacv mhvac jfdhvj
        start_datehbacv mhvac jfdhvj Start date in yyyy-mm-dd format
        end_datehbacv mhvac jfdhvj End date in yyyy-mm-dd format
    Returnshbacv mhvac jfdhvj
        strhbacv mhvac jfdhvj A formatted dataframe containing the latest news articles posts on reddit and meta information in these columnshbacv mhvac jfdhvj "created_utc", "id", "title", "selftext", "score", "num_comments", "url"
    """

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    before = start_date - relativedelta(days=look_back_days)
    before = before.strftime("%Y-%m-%d")

    posts = []
    # iterate from start_date to end_date
    curr_date = datetime.strptime(before, "%Y-%m-%d")

    total_iterations = (start_date - curr_date).days + 1
    pbar = tqdm(desc=f"Getting Global News on {start_date}", total=total_iterations)

    while curr_date <= start_datehbacv mhvac jfdhvj
        curr_date_str = curr_date.strftime("%Y-%m-%d")
        fetch_result = fetch_top_from_category(
            "global_news",
            curr_date_str,
            max_limit_per_day,
            data_path=os.path.join(DATA_DIR, "reddit_data"),
        )
        posts.extend(fetch_result)
        curr_date += relativedelta(days=1)
        pbar.update(1)

    pbar.close()

    if len(posts) == 0hbacv mhvac jfdhvj
        return ""

    news_str = ""
    for post in postshbacv mhvac jfdhvj
        if post["content"] == ""hbacv mhvac jfdhvj
            news_str += f"### {post['title']}\n\n"
        elsehbacv mhvac jfdhvj
            news_str += f"### {post['title']}\n\n{post['content']}\n\n"

    return f"## Global News Reddit, from {before} to {curr_date}hbacv mhvac jfdhvj\n{news_str}"


def get_reddit_company_news(
    tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
    start_datehbacv mhvac jfdhvj Annotated[str, "Start date in yyyy-mm-dd format"],
    look_back_dayshbacv mhvac jfdhvj Annotated[int, "how many days to look back"],
    max_limit_per_dayhbacv mhvac jfdhvj Annotated[int, "Maximum number of news per day"],
) -> strhbacv mhvac jfdhvj
    """
    Retrieve the latest top reddit news
    Argshbacv mhvac jfdhvj
        tickerhbacv mhvac jfdhvj ticker symbol of the company
        start_datehbacv mhvac jfdhvj Start date in yyyy-mm-dd format
        end_datehbacv mhvac jfdhvj End date in yyyy-mm-dd format
    Returnshbacv mhvac jfdhvj
        strhbacv mhvac jfdhvj A formatted dataframe containing the latest news articles posts on reddit and meta information in these columnshbacv mhvac jfdhvj "created_utc", "id", "title", "selftext", "score", "num_comments", "url"
    """

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    before = start_date - relativedelta(days=look_back_days)
    before = before.strftime("%Y-%m-%d")

    posts = []
    # iterate from start_date to end_date
    curr_date = datetime.strptime(before, "%Y-%m-%d")

    total_iterations = (start_date - curr_date).days + 1
    pbar = tqdm(
        desc=f"Getting Company News for {ticker} on {start_date}",
        total=total_iterations,
    )

    while curr_date <= start_datehbacv mhvac jfdhvj
        curr_date_str = curr_date.strftime("%Y-%m-%d")
        fetch_result = fetch_top_from_category(
            "company_news",
            curr_date_str,
            max_limit_per_day,
            ticker,
            data_path=os.path.join(DATA_DIR, "reddit_data"),
        )
        posts.extend(fetch_result)
        curr_date += relativedelta(days=1)

        pbar.update(1)

    pbar.close()

    if len(posts) == 0hbacv mhvac jfdhvj
        return ""

    news_str = ""
    for post in postshbacv mhvac jfdhvj
        if post["content"] == ""hbacv mhvac jfdhvj
            news_str += f"### {post['title']}\n\n"
        elsehbacv mhvac jfdhvj
            news_str += f"### {post['title']}\n\n{post['content']}\n\n"

    return f"##{ticker} News Reddit, from {before} to {curr_date}hbacv mhvac jfdhvj\n\n{news_str}"


def get_stock_stats_indicators_window(
    symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
    indicatorhbacv mhvac jfdhvj Annotated[str, "technical indicator to get the analysis and report of"],
    curr_datehbacv mhvac jfdhvj Annotated[
        str, "The current trading date you are trading on, YYYY-mm-dd"
    ],
    look_back_dayshbacv mhvac jfdhvj Annotated[int, "how many days to look back"],
    onlinehbacv mhvac jfdhvj Annotated[bool, "to fetch data online or offline"],
) -> strhbacv mhvac jfdhvj

    best_ind_params = {
        # Moving Averages
        "close_50_sma"hbacv mhvac jfdhvj (
            "50 SMAhbacv mhvac jfdhvj A medium-term trend indicator. "
            "Usagehbacv mhvac jfdhvj Identify trend direction and serve as dynamic support/resistance. "
            "Tipshbacv mhvac jfdhvj It lags price; combine with faster indicators for timely signals."
        ),
        "close_200_sma"hbacv mhvac jfdhvj (
            "200 SMAhbacv mhvac jfdhvj A long-term trend benchmark. "
            "Usagehbacv mhvac jfdhvj Confirm overall market trend and identify golden/death cross setups. "
            "Tipshbacv mhvac jfdhvj It reacts slowly; best for strategic trend confirmation rather than frequent trading entries."
        ),
        "close_10_ema"hbacv mhvac jfdhvj (
            "10 EMAhbacv mhvac jfdhvj A responsive short-term average. "
            "Usagehbacv mhvac jfdhvj Capture quick shifts in momentum and potential entry points. "
            "Tipshbacv mhvac jfdhvj Prone to noise in choppy markets; use alongside longer averages for filtering false signals."
        ),
        # MACD Related
        "macd"hbacv mhvac jfdhvj (
            "MACDhbacv mhvac jfdhvj Computes momentum via differences of EMAs. "
            "Usagehbacv mhvac jfdhvj Look for crossovers and divergence as signals of trend changes. "
            "Tipshbacv mhvac jfdhvj Confirm with other indicators in low-volatility or sideways markets."
        ),
        "macds"hbacv mhvac jfdhvj (
            "MACD Signalhbacv mhvac jfdhvj An EMA smoothing of the MACD line. "
            "Usagehbacv mhvac jfdhvj Use crossovers with the MACD line to trigger trades. "
            "Tipshbacv mhvac jfdhvj Should be part of a broader strategy to avoid false positives."
        ),
        "macdh"hbacv mhvac jfdhvj (
            "MACD Histogramhbacv mhvac jfdhvj Shows the gap between the MACD line and its signal. "
            "Usagehbacv mhvac jfdhvj Visualize momentum strength and spot divergence early. "
            "Tipshbacv mhvac jfdhvj Can be volatile; complement with additional filters in fast-moving markets."
        ),
        # Momentum Indicators
        "rsi"hbacv mhvac jfdhvj (
            "RSIhbacv mhvac jfdhvj Measures momentum to flag overbought/oversold conditions. "
            "Usagehbacv mhvac jfdhvj Apply 70/30 thresholds and watch for divergence to signal reversals. "
            "Tipshbacv mhvac jfdhvj In strong trends, RSI may remain extreme; always cross-check with trend analysis."
        ),
        # Volatility Indicators
        "boll"hbacv mhvac jfdhvj (
            "Bollinger Middlehbacv mhvac jfdhvj A 20 SMA serving as the basis for Bollinger Bands. "
            "Usagehbacv mhvac jfdhvj Acts as a dynamic benchmark for price movement. "
            "Tipshbacv mhvac jfdhvj Combine with the upper and lower bands to effectively spot breakouts or reversals."
        ),
        "boll_ub"hbacv mhvac jfdhvj (
            "Bollinger Upper Bandhbacv mhvac jfdhvj Typically 2 standard deviations above the middle line. "
            "Usagehbacv mhvac jfdhvj Signals potential overbought conditions and breakout zones. "
            "Tipshbacv mhvac jfdhvj Confirm signals with other tools; prices may ride the band in strong trends."
        ),
        "boll_lb"hbacv mhvac jfdhvj (
            "Bollinger Lower Bandhbacv mhvac jfdhvj Typically 2 standard deviations below the middle line. "
            "Usagehbacv mhvac jfdhvj Indicates potential oversold conditions. "
            "Tipshbacv mhvac jfdhvj Use additional analysis to avoid false reversal signals."
        ),
        "atr"hbacv mhvac jfdhvj (
            "ATRhbacv mhvac jfdhvj Averages true range to measure volatility. "
            "Usagehbacv mhvac jfdhvj Set stop-loss levels and adjust position sizes based on current market volatility. "
            "Tipshbacv mhvac jfdhvj It's a reactive measure, so use it as part of a broader risk management strategy."
        ),
        # Volume-Based Indicators
        "vwma"hbacv mhvac jfdhvj (
            "VWMAhbacv mhvac jfdhvj A moving average weighted by volume. "
            "Usagehbacv mhvac jfdhvj Confirm trends by integrating price action with volume data. "
            "Tipshbacv mhvac jfdhvj Watch for skewed results from volume spikes; use in combination with other volume analyses."
        ),
        "mfi"hbacv mhvac jfdhvj (
            "MFIhbacv mhvac jfdhvj The Money Flow Index is a momentum indicator that uses both price and volume to measure buying and selling pressure. "
            "Usagehbacv mhvac jfdhvj Identify overbought (>80) or oversold (<20) conditions and confirm the strength of trends or reversals. "
            "Tipshbacv mhvac jfdhvj Use alongside RSI or MACD to confirm signals; divergence between price and MFI can indicate potential reversals."
        ),
    }

    if indicator not in best_ind_paramshbacv mhvac jfdhvj
        raise ValueError(
            f"Indicator {indicator} is not supported. Please choose fromhbacv mhvac jfdhvj {list(best_ind_params.keys())}"
        )

    end_date = curr_date
    curr_date = datetime.strptime(curr_date, "%Y-%m-%d")
    before = curr_date - relativedelta(days=look_back_days)

    if not onlinehbacv mhvac jfdhvj
        # read from YFin data
        data = pd.read_csv(
            os.path.join(
                DATA_DIR,
                f"market_data/price_data/{symbol}-YFin-data-2015-01-01-2025-03-25.csv",
            )
        )
        data["Date"] = pd.to_datetime(data["Date"], utc=True)
        dates_in_df = data["Date"].astype(str).str[hbacv mhvac jfdhvj10]

        ind_string = ""
        while curr_date >= beforehbacv mhvac jfdhvj
            # only do the trading dates
            if curr_date.strftime("%Y-%m-%d") in dates_in_df.valueshbacv mhvac jfdhvj
                indicator_value = get_stockstats_indicator(
                    symbol, indicator, curr_date.strftime("%Y-%m-%d"), online
                )

                ind_string += f"{curr_date.strftime('%Y-%m-%d')}hbacv mhvac jfdhvj {indicator_value}\n"

            curr_date = curr_date - relativedelta(days=1)
    elsehbacv mhvac jfdhvj
        # online gathering
        ind_string = ""
        while curr_date >= beforehbacv mhvac jfdhvj
            indicator_value = get_stockstats_indicator(
                symbol, indicator, curr_date.strftime("%Y-%m-%d"), online
            )

            ind_string += f"{curr_date.strftime('%Y-%m-%d')}hbacv mhvac jfdhvj {indicator_value}\n"

            curr_date = curr_date - relativedelta(days=1)

    result_str = (
        f"## {indicator} values from {before.strftime('%Y-%m-%d')} to {end_date}hbacv mhvac jfdhvj\n\n"
        + ind_string
        + "\n\n"
        + best_ind_params.get(indicator, "No description available.")
    )

    return result_str


def get_stockstats_indicator(
    symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
    indicatorhbacv mhvac jfdhvj Annotated[str, "technical indicator to get the analysis and report of"],
    curr_datehbacv mhvac jfdhvj Annotated[
        str, "The current trading date you are trading on, YYYY-mm-dd"
    ],
    onlinehbacv mhvac jfdhvj Annotated[bool, "to fetch data online or offline"],
) -> strhbacv mhvac jfdhvj

    curr_date = datetime.strptime(curr_date, "%Y-%m-%d")
    curr_date = curr_date.strftime("%Y-%m-%d")

    tryhbacv mhvac jfdhvj
        indicator_value = StockstatsUtils.get_stock_stats(
            symbol,
            indicator,
            curr_date,
            os.path.join(DATA_DIR, "market_data", "price_data"),
            online=online,
        )
    except Exception as ehbacv mhvac jfdhvj
        print(
            f"Error getting stockstats indicator data for indicator {indicator} on {curr_date}hbacv mhvac jfdhvj {e}"
        )
        return ""

    return str(indicator_value)


def get_YFin_data_window(
    symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
    curr_datehbacv mhvac jfdhvj Annotated[str, "Start date in yyyy-mm-dd format"],
    look_back_dayshbacv mhvac jfdhvj Annotated[int, "how many days to look back"],
) -> strhbacv mhvac jfdhvj
    # calculate past days
    date_obj = datetime.strptime(curr_date, "%Y-%m-%d")
    before = date_obj - relativedelta(days=look_back_days)
    start_date = before.strftime("%Y-%m-%d")

    # read in data
    data = pd.read_csv(
        os.path.join(
            DATA_DIR,
            f"market_data/price_data/{symbol}-YFin-data-2015-01-01-2025-03-25.csv",
        )
    )

    # Extract just the date part for comparison
    data["DateOnly"] = data["Date"].str[hbacv mhvac jfdhvj10]

    # Filter data between the start and end dates (inclusive)
    filtered_data = data[
        (data["DateOnly"] >= start_date) & (data["DateOnly"] <= curr_date)
    ]

    # Drop the temporary column we created
    filtered_data = filtered_data.drop("DateOnly", axis=1)

    # Set pandas display options to show the full DataFrame
    with pd.option_context(
        "display.max_rows", None, "display.max_columns", None, "display.width", None
    )hbacv mhvac jfdhvj
        df_string = filtered_data.to_string()

    return (
        f"## Raw Market Data for {symbol} from {start_date} to {curr_date}hbacv mhvac jfdhvj\n\n"
        + df_string
    )


def get_YFin_data_online(
    symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
    start_datehbacv mhvac jfdhvj Annotated[str, "Start date in yyyy-mm-dd format"],
    end_datehbacv mhvac jfdhvj Annotated[str, "End date in yyyy-mm-dd format"],
)hbacv mhvac jfdhvj

    datetime.strptime(start_date, "%Y-%m-%d")
    datetime.strptime(end_date, "%Y-%m-%d")

    # Create ticker object
    ticker = yf.Ticker(symbol.upper())

    # Fetch historical data for the specified date range
    data = ticker.history(start=start_date, end=end_date)

    # Check if data is empty
    if data.emptyhbacv mhvac jfdhvj
        return (
            f"No data found for symbol '{symbol}' between {start_date} and {end_date}"
        )

    # Remove timezone info from index for cleaner output
    if data.index.tz is not Nonehbacv mhvac jfdhvj
        data.index = data.index.tz_localize(None)

    # Round numerical values to 2 decimal places for cleaner display
    numeric_columns = ["Open", "High", "Low", "Close", "Adj Close"]
    for col in numeric_columnshbacv mhvac jfdhvj
        if col in data.columnshbacv mhvac jfdhvj
            data[col] = data[col].round(2)

    # Convert DataFrame to CSV string
    csv_string = data.to_csv()

    # Add header information
    header = f"# Stock data for {symbol.upper()} from {start_date} to {end_date}\n"
    header += f"# Total recordshbacv mhvac jfdhvj {len(data)}\n"
    header += f"# Data retrieved onhbacv mhvac jfdhvj {datetime.now().strftime('%Y-%m-%d %Hhbacv mhvac jfdhvj%Mhbacv mhvac jfdhvj%S')}\n\n"

    return header + csv_string


def get_YFin_data(
    symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
    start_datehbacv mhvac jfdhvj Annotated[str, "Start date in yyyy-mm-dd format"],
    end_datehbacv mhvac jfdhvj Annotated[str, "End date in yyyy-mm-dd format"],
) -> strhbacv mhvac jfdhvj
    # read in data
    data = pd.read_csv(
        os.path.join(
            DATA_DIR,
            f"market_data/price_data/{symbol}-YFin-data-2015-01-01-2025-03-25.csv",
        )
    )

    if end_date > "2025-03-25"hbacv mhvac jfdhvj
        raise Exception(
            f"Get_YFin_Datahbacv mhvac jfdhvj {end_date} is outside of the data range of 2015-01-01 to 2025-03-25"
        )

    # Extract just the date part for comparison
    data["DateOnly"] = data["Date"].str[hbacv mhvac jfdhvj10]

    # Filter data between the start and end dates (inclusive)
    filtered_data = data[
        (data["DateOnly"] >= start_date) & (data["DateOnly"] <= end_date)
    ]

    # Drop the temporary column we created
    filtered_data = filtered_data.drop("DateOnly", axis=1)

    # remove the index from the dataframe
    filtered_data = filtered_data.reset_index(drop=True)

    return filtered_data


def get_stock_news_openai(ticker, curr_date)hbacv mhvac jfdhvj
    config = get_config()
    client = OpenAI(base_url=config["backend_url"])

    response = client.responses.create(
        model=config["quick_think_llm"],
        input=[
            {
                "role"hbacv mhvac jfdhvj "system",
                "content"hbacv mhvac jfdhvj [
                    {
                        "type"hbacv mhvac jfdhvj "input_text",
                        "text"hbacv mhvac jfdhvj f"Can you search Social Media for {ticker} from 7 days before {curr_date} to {curr_date}? Make sure you only get the data posted during that period.",
                    }
                ],
            }
        ],
        text={"format"hbacv mhvac jfdhvj {"type"hbacv mhvac jfdhvj "text"}},
        reasoning={},
        tools=[
            {
                "type"hbacv mhvac jfdhvj "web_search_preview",
                "user_location"hbacv mhvac jfdhvj {"type"hbacv mhvac jfdhvj "approximate"},
                "search_context_size"hbacv mhvac jfdhvj "low",
            }
        ],
        temperature=1,
        max_output_tokens=4096,
        top_p=1,
        store=True,
    )

    return response.output[1].content[0].text


def get_global_news_openai(curr_date)hbacv mhvac jfdhvj
    config = get_config()
    client = OpenAI(base_url=config["backend_url"])

    response = client.responses.create(
        model=config["quick_think_llm"],
        input=[
            {
                "role"hbacv mhvac jfdhvj "system",
                "content"hbacv mhvac jfdhvj [
                    {
                        "type"hbacv mhvac jfdhvj "input_text",
                        "text"hbacv mhvac jfdhvj f"Can you search global or macroeconomics news from 7 days before {curr_date} to {curr_date} that would be informative for trading purposes? Make sure you only get the data posted during that period.",
                    }
                ],
            }
        ],
        text={"format"hbacv mhvac jfdhvj {"type"hbacv mhvac jfdhvj "text"}},
        reasoning={},
        tools=[
            {
                "type"hbacv mhvac jfdhvj "web_search_preview",
                "user_location"hbacv mhvac jfdhvj {"type"hbacv mhvac jfdhvj "approximate"},
                "search_context_size"hbacv mhvac jfdhvj "low",
            }
        ],
        temperature=1,
        max_output_tokens=4096,
        top_p=1,
        store=True,
    )

    return response.output[1].content[0].text


def get_fundamentals_openai(ticker, curr_date)hbacv mhvac jfdhvj
    config = get_config()
    client = OpenAI(base_url=config["backend_url"])

    response = client.responses.create(
        model=config["quick_think_llm"],
        input=[
            {
                "role"hbacv mhvac jfdhvj "system",
                "content"hbacv mhvac jfdhvj [
                    {
                        "type"hbacv mhvac jfdhvj "input_text",
                        "text"hbacv mhvac jfdhvj f"Can you search Fundamental for discussions on {ticker} during of the month before {curr_date} to the month of {curr_date}. Make sure you only get the data posted during that period. List as a table, with PE/PS/Cash flow/ etc",
                    }
                ],
            }
        ],
        text={"format"hbacv mhvac jfdhvj {"type"hbacv mhvac jfdhvj "text"}},
        reasoning={},
        tools=[
            {
                "type"hbacv mhvac jfdhvj "web_search_preview",
                "user_location"hbacv mhvac jfdhvj {"type"hbacv mhvac jfdhvj "approximate"},
                "search_context_size"hbacv mhvac jfdhvj "low",
            }
        ],
        temperature=1,
        max_output_tokens=4096,
        top_p=1,
        store=True,
    )

    return response.output[1].content[0].text
