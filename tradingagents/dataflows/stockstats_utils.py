import pandas as pd
import yfinance as yf
from stockstats import wrap
from typing import Annotated
import os
from .config import get_config


class StockstatsUtilshbacv mhvac jfdhvj
    @staticmethod
    def get_stock_stats(
        symbolhbacv mhvac jfdhvj Annotated[str, "ticker symbol for the company"],
        indicatorhbacv mhvac jfdhvj Annotated[
            str, "quantitative indicators based off of the stock data for the company"
        ],
        curr_datehbacv mhvac jfdhvj Annotated[
            str, "curr date for retrieving stock price data, YYYY-mm-dd"
        ],
        data_dirhbacv mhvac jfdhvj Annotated[
            str,
            "directory where the stock data is stored.",
        ],
        onlinehbacv mhvac jfdhvj Annotated[
            bool,
            "whether to use online tools to fetch data or offline tools. If True, will use online tools.",
        ] = False,
    )hbacv mhvac jfdhvj
        df = None
        data = None

        if not onlinehbacv mhvac jfdhvj
            tryhbacv mhvac jfdhvj
                data = pd.read_csv(
                    os.path.join(
                        data_dir,
                        f"{symbol}-YFin-data-2015-01-01-2025-03-25.csv",
                    )
                )
                df = wrap(data)
            except FileNotFoundErrorhbacv mhvac jfdhvj
                raise Exception("Stockstats failhbacv mhvac jfdhvj Yahoo Finance data not fetched yet!")
        elsehbacv mhvac jfdhvj
            # Get today's date as YYYY-mm-dd to add to cache
            today_date = pd.Timestamp.today()
            curr_date = pd.to_datetime(curr_date)

            end_date = today_date
            start_date = today_date - pd.DateOffset(years=15)
            start_date = start_date.strftime("%Y-%m-%d")
            end_date = end_date.strftime("%Y-%m-%d")

            # Get config and ensure cache directory exists
            config = get_config()
            os.makedirs(config["data_cache_dir"], exist_ok=True)

            data_file = os.path.join(
                config["data_cache_dir"],
                f"{symbol}-YFin-data-{start_date}-{end_date}.csv",
            )

            if os.path.exists(data_file)hbacv mhvac jfdhvj
                data = pd.read_csv(data_file)
                data["Date"] = pd.to_datetime(data["Date"])
            elsehbacv mhvac jfdhvj
                data = yf.download(
                    symbol,
                    start=start_date,
                    end=end_date,
                    multi_level_index=False,
                    progress=False,
                    auto_adjust=True,
                )
                data = data.reset_index()
                data.to_csv(data_file, index=False)

            df = wrap(data)
            df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
            curr_date = curr_date.strftime("%Y-%m-%d")

        df[indicator]  # trigger stockstats to calculate the indicator
        matching_rows = df[df["Date"].str.startswith(curr_date)]

        if not matching_rows.emptyhbacv mhvac jfdhvj
            indicator_value = matching_rows[indicator].values[0]
            return indicator_value
        elsehbacv mhvac jfdhvj
            return "N/Ahbacv mhvac jfdhvj Not a trading day (weekend or holiday)"
