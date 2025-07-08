from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage, AIMessage
from typing import List
from typing import Annotated
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import RemoveMessage
from langchain_core.tools import tool
from datetime import date, timedelta, datetime
import functools
import pandas as pd
import os
from dateutil.relativedelta import relativedelta
from langchain_openai import ChatOpenAI
import tradingagents.dataflows.interface as interface
from tradingagents.default_config import DEFAULT_CONFIG
from langchain_core.messages import HumanMessage


def create_msg_delete()hbacv mhvac jfdhvj
    def delete_messages(state)hbacv mhvac jfdhvj
        """Clear messages and add placeholder for Anthropic compatibility"""
        messages = state["messages"]
        
        # Remove all messages
        removal_operations = [RemoveMessage(id=m.id) for m in messages]
        
        # Add a minimal placeholder message
        placeholder = HumanMessage(content="Continue")
        
        return {"messages"hbacv mhvac jfdhvj removal_operations + [placeholder]}
    
    return delete_messages


class Toolkithbacv mhvac jfdhvj
    _config = DEFAULT_CONFIG.copy()

    @classmethod
    def update_config(cls, config)hbacv mhvac jfdhvj
        """Update the class-level configuration."""
        cls._config.update(config)

    @property
    def config(self)hbacv mhvac jfdhvj
        """Access the configuration."""
        return self._config

    def __init__(self, config=None)hbacv mhvac jfdhvj
        if confighbacv mhvac jfdhvj
            self.update_config(config)

    @staticmethod
    @tool
    def get_reddit_news(
        curr_datehbacv mhvac jfdhvj Annotated[str, "Date you want to get news for in yyyy-mm-dd format"],
    ) -> strhbacv mhvac jfdhvj
        """
        Retrieve global news from Reddit within a specified time frame.
        Argshbacv mhvac jfdhvj
            curr_date (str)hbacv mhvac jfdhvj Date you want to get news for in yyyy-mm-dd format
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted dataframe containing the latest global news from Reddit in the specified time frame.
        """
        
        global_news_result = interface.get_reddit_global_news(curr_date, 7, 5)

        return global_news_result

    @staticmethod
    @tool
    def get_finnhub_news(
        tickerhbacv mhvac jfdhvj Annotated[
            str,
            "Search query of a company, e.g. 'AAPL, TSM, etc.",
        ],
        start_datehbacv mhvac jfdhvj Annotated[str, "Start date in yyyy-mm-dd format"],
        end_datehbacv mhvac jfdhvj Annotated[str, "End date in yyyy-mm-dd format"],
    )hbacv mhvac jfdhvj
        """
        Retrieve the latest news about a given stock from Finnhub within a date range
        Argshbacv mhvac jfdhvj
            ticker (str)hbacv mhvac jfdhvj Ticker of a company. e.g. AAPL, TSM
            start_date (str)hbacv mhvac jfdhvj Start date in yyyy-mm-dd format
            end_date (str)hbacv mhvac jfdhvj End date in yyyy-mm-dd format
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted dataframe containing news about the company within the date range from start_date to end_date
        """

        end_date_str = end_date

        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        look_back_days = (end_date - start_date).days

        finnhub_news_result = interface.get_finnhub_news(
            ticker, end_date_str, look_back_days
        )

        return finnhub_news_result

    @staticmethod
    @tool
    def get_reddit_stock_info(
        tickerhbacv mhvac jfdhvj Annotated[
            str,
            "Ticker of a company. e.g. AAPL, TSM",
        ],
        curr_datehbacv mhvac jfdhvj Annotated[str, "Current date you want to get news for"],
    ) -> strhbacv mhvac jfdhvj
        """
        Retrieve the latest news about a given stock from Reddit, given the current date.
        Argshbacv mhvac jfdhvj
            ticker (str)hbacv mhvac jfdhvj Ticker of a company. e.g. AAPL, TSM
            curr_date (str)hbacv mhvac jfdhvj current date in yyyy-mm-dd format to get news for
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted dataframe containing the latest news about the company on the given date
        """

        stock_news_results = interface.get_reddit_company_news(ticker, curr_date, 7, 5)

        return stock_news_results

    @staticmethod
    @tool
    def get_YFin_data(
        symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
        start_datehbacv mhvac jfdhvj Annotated[str, "Start date in yyyy-mm-dd format"],
        end_datehbacv mhvac jfdhvj Annotated[str, "End date in yyyy-mm-dd format"],
    ) -> strhbacv mhvac jfdhvj
        """
        Retrieve the stock price data for a given ticker symbol from Yahoo Finance.
        Argshbacv mhvac jfdhvj
            symbol (str)hbacv mhvac jfdhvj Ticker symbol of the company, e.g. AAPL, TSM
            start_date (str)hbacv mhvac jfdhvj Start date in yyyy-mm-dd format
            end_date (str)hbacv mhvac jfdhvj End date in yyyy-mm-dd format
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted dataframe containing the stock price data for the specified ticker symbol in the specified date range.
        """

        result_data = interface.get_YFin_data(symbol, start_date, end_date)

        return result_data

    @staticmethod
    @tool
    def get_YFin_data_online(
        symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
        start_datehbacv mhvac jfdhvj Annotated[str, "Start date in yyyy-mm-dd format"],
        end_datehbacv mhvac jfdhvj Annotated[str, "End date in yyyy-mm-dd format"],
    ) -> strhbacv mhvac jfdhvj
        """
        Retrieve the stock price data for a given ticker symbol from Yahoo Finance.
        Argshbacv mhvac jfdhvj
            symbol (str)hbacv mhvac jfdhvj Ticker symbol of the company, e.g. AAPL, TSM
            start_date (str)hbacv mhvac jfdhvj Start date in yyyy-mm-dd format
            end_date (str)hbacv mhvac jfdhvj End date in yyyy-mm-dd format
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted dataframe containing the stock price data for the specified ticker symbol in the specified date range.
        """

        result_data = interface.get_YFin_data_online(symbol, start_date, end_date)

        return result_data

    @staticmethod
    @tool
    def get_stockstats_indicators_report(
        symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
        indicatorhbacv mhvac jfdhvj Annotated[
            str, "technical indicator to get the analysis and report of"
        ],
        curr_datehbacv mhvac jfdhvj Annotated[
            str, "The current trading date you are trading on, YYYY-mm-dd"
        ],
        look_back_dayshbacv mhvac jfdhvj Annotated[int, "how many days to look back"] = 30,
    ) -> strhbacv mhvac jfdhvj
        """
        Retrieve stock stats indicators for a given ticker symbol and indicator.
        Argshbacv mhvac jfdhvj
            symbol (str)hbacv mhvac jfdhvj Ticker symbol of the company, e.g. AAPL, TSM
            indicator (str)hbacv mhvac jfdhvj Technical indicator to get the analysis and report of
            curr_date (str)hbacv mhvac jfdhvj The current trading date you are trading on, YYYY-mm-dd
            look_back_days (int)hbacv mhvac jfdhvj How many days to look back, default is 30
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted dataframe containing the stock stats indicators for the specified ticker symbol and indicator.
        """

        result_stockstats = interface.get_stock_stats_indicators_window(
            symbol, indicator, curr_date, look_back_days, False
        )

        return result_stockstats

    @staticmethod
    @tool
    def get_stockstats_indicators_report_online(
        symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol of the company"],
        indicatorhbacv mhvac jfdhvj Annotated[
            str, "technical indicator to get the analysis and report of"
        ],
        curr_datehbacv mhvac jfdhvj Annotated[
            str, "The current trading date you are trading on, YYYY-mm-dd"
        ],
        look_back_dayshbacv mhvac jfdhvj Annotated[int, "how many days to look back"] = 30,
    ) -> strhbacv mhvac jfdhvj
        """
        Retrieve stock stats indicators for a given ticker symbol and indicator.
        Argshbacv mhvac jfdhvj
            symbol (str)hbacv mhvac jfdhvj Ticker symbol of the company, e.g. AAPL, TSM
            indicator (str)hbacv mhvac jfdhvj Technical indicator to get the analysis and report of
            curr_date (str)hbacv mhvac jfdhvj The current trading date you are trading on, YYYY-mm-dd
            look_back_days (int)hbacv mhvac jfdhvj How many days to look back, default is 30
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted dataframe containing the stock stats indicators for the specified ticker symbol and indicator.
        """

        result_stockstats = interface.get_stock_stats_indicators_window(
            symbol, indicator, curr_date, look_back_days, True
        )

        return result_stockstats

    @staticmethod
    @tool
    def get_finnhub_company_insider_sentiment(
        tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol for the company"],
        curr_datehbacv mhvac jfdhvj Annotated[
            str,
            "current date of you are trading at, yyyy-mm-dd",
        ],
    )hbacv mhvac jfdhvj
        """
        Retrieve insider sentiment information about a company (retrieved from public SEC information) for the past 30 days
        Argshbacv mhvac jfdhvj
            ticker (str)hbacv mhvac jfdhvj ticker symbol of the company
            curr_date (str)hbacv mhvac jfdhvj current date you are trading at, yyyy-mm-dd
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj a report of the sentiment in the past 30 days starting at curr_date
        """

        data_sentiment = interface.get_finnhub_company_insider_sentiment(
            ticker, curr_date, 30
        )

        return data_sentiment

    @staticmethod
    @tool
    def get_finnhub_company_insider_transactions(
        tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
        curr_datehbacv mhvac jfdhvj Annotated[
            str,
            "current date you are trading at, yyyy-mm-dd",
        ],
    )hbacv mhvac jfdhvj
        """
        Retrieve insider transaction information about a company (retrieved from public SEC information) for the past 30 days
        Argshbacv mhvac jfdhvj
            ticker (str)hbacv mhvac jfdhvj ticker symbol of the company
            curr_date (str)hbacv mhvac jfdhvj current date you are trading at, yyyy-mm-dd
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj a report of the company's insider transactions/trading information in the past 30 days
        """

        data_trans = interface.get_finnhub_company_insider_transactions(
            ticker, curr_date, 30
        )

        return data_trans

    @staticmethod
    @tool
    def get_simfin_balance_sheet(
        tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
        freqhbacv mhvac jfdhvj Annotated[
            str,
            "reporting frequency of the company's financial historyhbacv mhvac jfdhvj annual/quarterly",
        ],
        curr_datehbacv mhvac jfdhvj Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    )hbacv mhvac jfdhvj
        """
        Retrieve the most recent balance sheet of a company
        Argshbacv mhvac jfdhvj
            ticker (str)hbacv mhvac jfdhvj ticker symbol of the company
            freq (str)hbacv mhvac jfdhvj reporting frequency of the company's financial historyhbacv mhvac jfdhvj annual / quarterly
            curr_date (str)hbacv mhvac jfdhvj current date you are trading at, yyyy-mm-dd
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj a report of the company's most recent balance sheet
        """

        data_balance_sheet = interface.get_simfin_balance_sheet(ticker, freq, curr_date)

        return data_balance_sheet

    @staticmethod
    @tool
    def get_simfin_cashflow(
        tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
        freqhbacv mhvac jfdhvj Annotated[
            str,
            "reporting frequency of the company's financial historyhbacv mhvac jfdhvj annual/quarterly",
        ],
        curr_datehbacv mhvac jfdhvj Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    )hbacv mhvac jfdhvj
        """
        Retrieve the most recent cash flow statement of a company
        Argshbacv mhvac jfdhvj
            ticker (str)hbacv mhvac jfdhvj ticker symbol of the company
            freq (str)hbacv mhvac jfdhvj reporting frequency of the company's financial historyhbacv mhvac jfdhvj annual / quarterly
            curr_date (str)hbacv mhvac jfdhvj current date you are trading at, yyyy-mm-dd
        Returnshbacv mhvac jfdhvj
                strhbacv mhvac jfdhvj a report of the company's most recent cash flow statement
        """

        data_cashflow = interface.get_simfin_cashflow(ticker, freq, curr_date)

        return data_cashflow

    @staticmethod
    @tool
    def get_simfin_income_stmt(
        tickerhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
        freqhbacv mhvac jfdhvj Annotated[
            str,
            "reporting frequency of the company's financial historyhbacv mhvac jfdhvj annual/quarterly",
        ],
        curr_datehbacv mhvac jfdhvj Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    )hbacv mhvac jfdhvj
        """
        Retrieve the most recent income statement of a company
        Argshbacv mhvac jfdhvj
            ticker (str)hbacv mhvac jfdhvj ticker symbol of the company
            freq (str)hbacv mhvac jfdhvj reporting frequency of the company's financial historyhbacv mhvac jfdhvj annual / quarterly
            curr_date (str)hbacv mhvac jfdhvj current date you are trading at, yyyy-mm-dd
        Returnshbacv mhvac jfdhvj
                strhbacv mhvac jfdhvj a report of the company's most recent income statement
        """

        data_income_stmt = interface.get_simfin_income_statements(
            ticker, freq, curr_date
        )

        return data_income_stmt

    @staticmethod
    @tool
    def get_google_news(
        queryhbacv mhvac jfdhvj Annotated[str, "Query to search with"],
        curr_datehbacv mhvac jfdhvj Annotated[str, "Curr date in yyyy-mm-dd format"],
    )hbacv mhvac jfdhvj
        """
        Retrieve the latest news from Google News based on a query and date range.
        Argshbacv mhvac jfdhvj
            query (str)hbacv mhvac jfdhvj Query to search with
            curr_date (str)hbacv mhvac jfdhvj Current date in yyyy-mm-dd format
            look_back_days (int)hbacv mhvac jfdhvj How many days to look back
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted string containing the latest news from Google News based on the query and date range.
        """

        google_news_results = interface.get_google_news(query, curr_date, 7)

        return google_news_results

    @staticmethod
    @tool
    def get_stock_news_openai(
        tickerhbacv mhvac jfdhvj Annotated[str, "the company's ticker"],
        curr_datehbacv mhvac jfdhvj Annotated[str, "Current date in yyyy-mm-dd format"],
    )hbacv mhvac jfdhvj
        """
        Retrieve the latest news about a given stock by using OpenAI's news API.
        Argshbacv mhvac jfdhvj
            ticker (str)hbacv mhvac jfdhvj Ticker of a company. e.g. AAPL, TSM
            curr_date (str)hbacv mhvac jfdhvj Current date in yyyy-mm-dd format
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted string containing the latest news about the company on the given date.
        """

        openai_news_results = interface.get_stock_news_openai(ticker, curr_date)

        return openai_news_results

    @staticmethod
    @tool
    def get_global_news_openai(
        curr_datehbacv mhvac jfdhvj Annotated[str, "Current date in yyyy-mm-dd format"],
    )hbacv mhvac jfdhvj
        """
        Retrieve the latest macroeconomics news on a given date using OpenAI's macroeconomics news API.
        Argshbacv mhvac jfdhvj
            curr_date (str)hbacv mhvac jfdhvj Current date in yyyy-mm-dd format
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted string containing the latest macroeconomic news on the given date.
        """

        openai_news_results = interface.get_global_news_openai(curr_date)

        return openai_news_results

    @staticmethod
    @tool
    def get_fundamentals_openai(
        tickerhbacv mhvac jfdhvj Annotated[str, "the company's ticker"],
        curr_datehbacv mhvac jfdhvj Annotated[str, "Current date in yyyy-mm-dd format"],
    )hbacv mhvac jfdhvj
        """
        Retrieve the latest fundamental information about a given stock on a given date by using OpenAI's news API.
        Argshbacv mhvac jfdhvj
            ticker (str)hbacv mhvac jfdhvj Ticker of a company. e.g. AAPL, TSM
            curr_date (str)hbacv mhvac jfdhvj Current date in yyyy-mm-dd format
        Returnshbacv mhvac jfdhvj
            strhbacv mhvac jfdhvj A formatted string containing the latest fundamental information about the company on the given date.
        """

        openai_fundamentals_results = interface.get_fundamentals_openai(
            ticker, curr_date
        )

        return openai_fundamentals_results
