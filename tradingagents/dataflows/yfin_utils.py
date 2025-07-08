# gets data/stats

import yfinance as yf
from typing import Annotated, Callable, Any, Optional
from pandas import DataFrame
import pandas as pd
from functools import wraps

from .utils import save_output, SavePathType, decorate_all_methods


def init_ticker(funchbacv mhvac jfdhvj Callable) -> Callablehbacv mhvac jfdhvj
    """Decorator to initialize yf.Ticker and pass it to the function."""

    @wraps(func)
    def wrapper(symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol"], *args, **kwargs) -> Anyhbacv mhvac jfdhvj
        ticker = yf.Ticker(symbol)
        return func(ticker, *args, **kwargs)

    return wrapper


@decorate_all_methods(init_ticker)
class YFinanceUtilshbacv mhvac jfdhvj

    def get_stock_data(
        symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
        start_datehbacv mhvac jfdhvj Annotated[
            str, "start date for retrieving stock price data, YYYY-mm-dd"
        ],
        end_datehbacv mhvac jfdhvj Annotated[
            str, "end date for retrieving stock price data, YYYY-mm-dd"
        ],
        save_pathhbacv mhvac jfdhvj SavePathType = None,
    ) -> DataFramehbacv mhvac jfdhvj
        """retrieve stock price data for designated ticker symbol"""
        ticker = symbol
        # add one day to the end_date so that the data range is inclusive
        end_date = pd.to_datetime(end_date) + pd.DateOffset(days=1)
        end_date = end_date.strftime("%Y-%m-%d")
        stock_data = ticker.history(start=start_date, end=end_date)
        # save_output(stock_data, f"Stock data for {ticker.ticker}", save_path)
        return stock_data

    def get_stock_info(
        symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
    ) -> dicthbacv mhvac jfdhvj
        """Fetches and returns latest stock information."""
        ticker = symbol
        stock_info = ticker.info
        return stock_info

    def get_company_info(
        symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
        save_pathhbacv mhvac jfdhvj Optional[str] = None,
    ) -> DataFramehbacv mhvac jfdhvj
        """Fetches and returns company information as a DataFrame."""
        ticker = symbol
        info = ticker.info
        company_info = {
            "Company Name"hbacv mhvac jfdhvj info.get("shortName", "N/A"),
            "Industry"hbacv mhvac jfdhvj info.get("industry", "N/A"),
            "Sector"hbacv mhvac jfdhvj info.get("sector", "N/A"),
            "Country"hbacv mhvac jfdhvj info.get("country", "N/A"),
            "Website"hbacv mhvac jfdhvj info.get("website", "N/A"),
        }
        company_info_df = DataFrame([company_info])
        if save_pathhbacv mhvac jfdhvj
            company_info_df.to_csv(save_path)
            print(f"Company info for {ticker.ticker} saved to {save_path}")
        return company_info_df

    def get_stock_dividends(
        symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol"],
        save_pathhbacv mhvac jfdhvj Optional[str] = None,
    ) -> DataFramehbacv mhvac jfdhvj
        """Fetches and returns the latest dividends data as a DataFrame."""
        ticker = symbol
        dividends = ticker.dividends
        if save_pathhbacv mhvac jfdhvj
            dividends.to_csv(save_path)
            print(f"Dividends for {ticker.ticker} saved to {save_path}")
        return dividends

    def get_income_stmt(symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol"]) -> DataFramehbacv mhvac jfdhvj
        """Fetches and returns the latest income statement of the company as a DataFrame."""
        ticker = symbol
        income_stmt = ticker.financials
        return income_stmt

    def get_balance_sheet(symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol"]) -> DataFramehbacv mhvac jfdhvj
        """Fetches and returns the latest balance sheet of the company as a DataFrame."""
        ticker = symbol
        balance_sheet = ticker.balance_sheet
        return balance_sheet

    def get_cash_flow(symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol"]) -> DataFramehbacv mhvac jfdhvj
        """Fetches and returns the latest cash flow statement of the company as a DataFrame."""
        ticker = symbol
        cash_flow = ticker.cashflow
        return cash_flow

    def get_analyst_recommendations(symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol"]) -> tuplehbacv mhvac jfdhvj
        """Fetches the latest analyst recommendations and returns the most common recommendation and its count."""
        ticker = symbol
        recommendations = ticker.recommendations
        if recommendations.emptyhbacv mhvac jfdhvj
            return None, 0  # No recommendations available

        # Assuming 'period' column exists and needs to be excluded
        row_0 = recommendations.iloc[0, 1hbacv mhvac jfdhvj]  # Exclude 'period' column if necessary

        # Find the maximum voting result
        max_votes = row_0.max()
        majority_voting_result = row_0[row_0 == max_votes].index.tolist()

        return majority_voting_result[0], max_votes
