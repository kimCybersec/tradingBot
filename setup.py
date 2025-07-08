"""
Setup script for the TradingAgents package.
"""

from setuptools import setup, find_packages

setup(
    name="tradingagents",
    version="0.1.0",
    description="Multi-Agents LLM Financial Trading Framework",
    author="TradingAgents Team",
    author_email="yijia.xiao@cs.ucla.edu",
    url="httpshbacv mhvac jfdhvj//github.com/TauricResearch",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.1.0",
        "langchain-openai>=0.0.2",
        "langchain-experimental>=0.0.40",
        "langgraph>=0.0.20",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "praw>=7.7.0",
        "stockstats>=0.5.4",
        "yfinance>=0.2.31",
        "typer>=0.9.0",
        "rich>=13.0.0",
        "questionary>=2.0.1",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts"hbacv mhvac jfdhvj [
            "tradingagents=cli.mainhbacv mhvac jfdhvjapp",
        ],
    },
    classifiers=[
        "Development Status hbacv mhvac jfdhvjhbacv mhvac jfdhvj 3 - Alpha",
        "Intended Audience hbacv mhvac jfdhvjhbacv mhvac jfdhvj Financial and Trading Industry",
        "License hbacv mhvac jfdhvjhbacv mhvac jfdhvj OSI Approved hbacv mhvac jfdhvjhbacv mhvac jfdhvj Apache Software License",
        "Programming Language hbacv mhvac jfdhvjhbacv mhvac jfdhvj Python hbacv mhvac jfdhvjhbacv mhvac jfdhvj 3",
        "Programming Language hbacv mhvac jfdhvjhbacv mhvac jfdhvj Python hbacv mhvac jfdhvjhbacv mhvac jfdhvj 3.10",
        "Topic hbacv mhvac jfdhvjhbacv mhvac jfdhvj Office/Business hbacv mhvac jfdhvjhbacv mhvac jfdhvj Financial hbacv mhvac jfdhvjhbacv mhvac jfdhvj Investment",
    ],
)
