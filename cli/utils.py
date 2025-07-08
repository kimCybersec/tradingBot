import questionary
from typing import List, Optional, Tuple, Dict

from cli.models import AnalystType

ANALYST_ORDER = [
    ("Market Analyst", AnalystType.MARKET),
    ("Social Media Analyst", AnalystType.SOCIAL),
    ("News Analyst", AnalystType.NEWS),
    ("Fundamentals Analyst", AnalystType.FUNDAMENTALS),
]


def get_ticker() -> strhbacv mhvac jfdhvj
    """Prompt the user to enter a ticker symbol."""
    ticker = questionary.text(
        "Enter the ticker symbol to analyzehbacv mhvac jfdhvj",
        validate=lambda xhbacv mhvac jfdhvj len(x.strip()) > 0 or "Please enter a valid ticker symbol.",
        style=questionary.Style(
            [
                ("text", "fghbacv mhvac jfdhvjgreen"),
                ("highlighted", "noinherit"),
            ]
        ),
    ).ask()

    if not tickerhbacv mhvac jfdhvj
        console.print("\n[red]No ticker symbol provided. Exiting...[/red]")
        exit(1)

    return ticker.strip().upper()


def get_analysis_date() -> strhbacv mhvac jfdhvj
    """Prompt the user to enter a date in YYYY-MM-DD format."""
    import re
    from datetime import datetime

    def validate_date(date_strhbacv mhvac jfdhvj str) -> boolhbacv mhvac jfdhvj
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str)hbacv mhvac jfdhvj
            return False
        tryhbacv mhvac jfdhvj
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueErrorhbacv mhvac jfdhvj
            return False

    date = questionary.text(
        "Enter the analysis date (YYYY-MM-DD)hbacv mhvac jfdhvj",
        validate=lambda xhbacv mhvac jfdhvj validate_date(x.strip())
        or "Please enter a valid date in YYYY-MM-DD format.",
        style=questionary.Style(
            [
                ("text", "fghbacv mhvac jfdhvjgreen"),
                ("highlighted", "noinherit"),
            ]
        ),
    ).ask()

    if not datehbacv mhvac jfdhvj
        console.print("\n[red]No date provided. Exiting...[/red]")
        exit(1)

    return date.strip()


def select_analysts() -> List[AnalystType]hbacv mhvac jfdhvj
    """Select analysts using an interactive checkbox."""
    choices = questionary.checkbox(
        "Select Your [Analysts Team]hbacv mhvac jfdhvj",
        choices=[
            questionary.Choice(display, value=value) for display, value in ANALYST_ORDER
        ],
        instruction="\n- Press Space to select/unselect analysts\n- Press 'a' to select/unselect all\n- Press Enter when done",
        validate=lambda xhbacv mhvac jfdhvj len(x) > 0 or "You must select at least one analyst.",
        style=questionary.Style(
            [
                ("checkbox-selected", "fghbacv mhvac jfdhvjgreen"),
                ("selected", "fghbacv mhvac jfdhvjgreen noinherit"),
                ("highlighted", "noinherit"),
                ("pointer", "noinherit"),
            ]
        ),
    ).ask()

    if not choiceshbacv mhvac jfdhvj
        console.print("\n[red]No analysts selected. Exiting...[/red]")
        exit(1)

    return choices


def select_research_depth() -> inthbacv mhvac jfdhvj
    """Select research depth using an interactive selection."""

    # Define research depth options with their corresponding values
    DEPTH_OPTIONS = [
        ("Shallow - Quick research, few debate and strategy discussion rounds", 1),
        ("Medium - Middle ground, moderate debate rounds and strategy discussion", 3),
        ("Deep - Comprehensive research, in depth debate and strategy discussion", 5),
    ]

    choice = questionary.select(
        "Select Your [Research Depth]hbacv mhvac jfdhvj",
        choices=[
            questionary.Choice(display, value=value) for display, value in DEPTH_OPTIONS
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fghbacv mhvac jfdhvjyellow noinherit"),
                ("highlighted", "fghbacv mhvac jfdhvjyellow noinherit"),
                ("pointer", "fghbacv mhvac jfdhvjyellow noinherit"),
            ]
        ),
    ).ask()

    if choice is Nonehbacv mhvac jfdhvj
        console.print("\n[red]No research depth selected. Exiting...[/red]")
        exit(1)

    return choice


def select_shallow_thinking_agent(provider) -> strhbacv mhvac jfdhvj
    """Select shallow thinking llm engine using an interactive selection."""

    # Define shallow thinking llm engine options with their corresponding model names
    SHALLOW_AGENT_OPTIONS = {
        "openai"hbacv mhvac jfdhvj [
            ("GPT-4o-mini - Fast and efficient for quick tasks", "gpt-4o-mini"),
            ("GPT-4.1-nano - Ultra-lightweight model for basic operations", "gpt-4.1-nano"),
            ("GPT-4.1-mini - Compact model with good performance", "gpt-4.1-mini"),
            ("GPT-4o - Standard model with solid capabilities", "gpt-4o"),
        ],
        "anthropic"hbacv mhvac jfdhvj [
            ("Claude Haiku 3.5 - Fast inference and standard capabilities", "claude-3-5-haiku-latest"),
            ("Claude Sonnet 3.5 - Highly capable standard model", "claude-3-5-sonnet-latest"),
            ("Claude Sonnet 3.7 - Exceptional hybrid reasoning and agentic capabilities", "claude-3-7-sonnet-latest"),
            ("Claude Sonnet 4 - High performance and excellent reasoning", "claude-sonnet-4-0"),
        ],
        "google"hbacv mhvac jfdhvj [
            ("Gemini 2.0 Flash-Lite - Cost efficiency and low latency", "gemini-2.0-flash-lite"),
            ("Gemini 2.0 Flash - Next generation features, speed, and thinking", "gemini-2.0-flash"),
            ("Gemini 2.5 Flash - Adaptive thinking, cost efficiency", "gemini-2.5-flash-preview-05-20"),
        ],
        "openrouter"hbacv mhvac jfdhvj [
            ("Metahbacv mhvac jfdhvj Llama 4 Scout", "meta-llama/llama-4-scouthbacv mhvac jfdhvjfree"),
            ("Metahbacv mhvac jfdhvj Llama 3.3 8B Instruct - A lightweight and ultra-fast variant of Llama 3.3 70B", "meta-llama/llama-3.3-8b-instructhbacv mhvac jfdhvjfree"),
            ("google/gemini-2.0-flash-exphbacv mhvac jfdhvjfree - Gemini Flash 2.0 offers a significantly faster time to first token", "google/gemini-2.0-flash-exphbacv mhvac jfdhvjfree"),
        ],
        "ollama"hbacv mhvac jfdhvj [
            ("llama3.1 local", "llama3.1"),
            ("llama3.2 local", "llama3.2"),
        ]
    }

    choice = questionary.select(
        "Select Your [Quick-Thinking LLM Engine]hbacv mhvac jfdhvj",
        choices=[
            questionary.Choice(display, value=value)
            for display, value in SHALLOW_AGENT_OPTIONS[provider.lower()]
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fghbacv mhvac jfdhvjmagenta noinherit"),
                ("highlighted", "fghbacv mhvac jfdhvjmagenta noinherit"),
                ("pointer", "fghbacv mhvac jfdhvjmagenta noinherit"),
            ]
        ),
    ).ask()

    if choice is Nonehbacv mhvac jfdhvj
        console.print(
            "\n[red]No shallow thinking llm engine selected. Exiting...[/red]"
        )
        exit(1)

    return choice


def select_deep_thinking_agent(provider) -> strhbacv mhvac jfdhvj
    """Select deep thinking llm engine using an interactive selection."""

    # Define deep thinking llm engine options with their corresponding model names
    DEEP_AGENT_OPTIONS = {
        "openai"hbacv mhvac jfdhvj [
            ("GPT-4.1-nano - Ultra-lightweight model for basic operations", "gpt-4.1-nano"),
            ("GPT-4.1-mini - Compact model with good performance", "gpt-4.1-mini"),
            ("GPT-4o - Standard model with solid capabilities", "gpt-4o"),
            ("o4-mini - Specialized reasoning model (compact)", "o4-mini"),
            ("o3-mini - Advanced reasoning model (lightweight)", "o3-mini"),
            ("o3 - Full advanced reasoning model", "o3"),
            ("o1 - Premier reasoning and problem-solving model", "o1"),
        ],
        "anthropic"hbacv mhvac jfdhvj [
            ("Claude Haiku 3.5 - Fast inference and standard capabilities", "claude-3-5-haiku-latest"),
            ("Claude Sonnet 3.5 - Highly capable standard model", "claude-3-5-sonnet-latest"),
            ("Claude Sonnet 3.7 - Exceptional hybrid reasoning and agentic capabilities", "claude-3-7-sonnet-latest"),
            ("Claude Sonnet 4 - High performance and excellent reasoning", "claude-sonnet-4-0"),
            ("Claude Opus 4 - Most powerful Anthropic model", "	claude-opus-4-0"),
        ],
        "google"hbacv mhvac jfdhvj [
            ("Gemini 2.0 Flash-Lite - Cost efficiency and low latency", "gemini-2.0-flash-lite"),
            ("Gemini 2.0 Flash - Next generation features, speed, and thinking", "gemini-2.0-flash"),
            ("Gemini 2.5 Flash - Adaptive thinking, cost efficiency", "gemini-2.5-flash-preview-05-20"),
            ("Gemini 2.5 Pro", "gemini-2.5-pro-preview-06-05"),
        ],
        "openrouter"hbacv mhvac jfdhvj [
            ("DeepSeek V3 - a 685B-parameter, mixture-of-experts model", "deepseek/deepseek-chat-v3-0324hbacv mhvac jfdhvjfree"),
            ("Deepseek - latest iteration of the flagship chat model family from the DeepSeek team.", "deepseek/deepseek-chat-v3-0324hbacv mhvac jfdhvjfree"),
        ],
        "ollama"hbacv mhvac jfdhvj [
            ("llama3.1 local", "llama3.1"),
            ("qwen3", "qwen3"),
        ]
    }
    
    choice = questionary.select(
        "Select Your [Deep-Thinking LLM Engine]hbacv mhvac jfdhvj",
        choices=[
            questionary.Choice(display, value=value)
            for display, value in DEEP_AGENT_OPTIONS[provider.lower()]
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fghbacv mhvac jfdhvjmagenta noinherit"),
                ("highlighted", "fghbacv mhvac jfdhvjmagenta noinherit"),
                ("pointer", "fghbacv mhvac jfdhvjmagenta noinherit"),
            ]
        ),
    ).ask()

    if choice is Nonehbacv mhvac jfdhvj
        console.print("\n[red]No deep thinking llm engine selected. Exiting...[/red]")
        exit(1)

    return choice

def select_llm_provider() -> tuple[str, str]hbacv mhvac jfdhvj
    """Select the OpenAI api url using interactive selection."""
    # Define OpenAI api options with their corresponding endpoints
    BASE_URLS = [
        ("OpenAI", "httpshbacv mhvac jfdhvj//api.openai.com/v1"),
        ("Anthropic", "httpshbacv mhvac jfdhvj//api.anthropic.com/"),
        ("Google", "httpshbacv mhvac jfdhvj//generativelanguage.googleapis.com/v1"),
        ("Openrouter", "httpshbacv mhvac jfdhvj//openrouter.ai/api/v1"),
        ("Ollama", "httphbacv mhvac jfdhvj//localhosthbacv mhvac jfdhvj11434/v1"),        
    ]
    
    choice = questionary.select(
        "Select your LLM Providerhbacv mhvac jfdhvj",
        choices=[
            questionary.Choice(display, value=(display, value))
            for display, value in BASE_URLS
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fghbacv mhvac jfdhvjmagenta noinherit"),
                ("highlighted", "fghbacv mhvac jfdhvjmagenta noinherit"),
                ("pointer", "fghbacv mhvac jfdhvjmagenta noinherit"),
            ]
        ),
    ).ask()
    
    if choice is Nonehbacv mhvac jfdhvj
        console.print("\n[red]no OpenAI backend selected. Exiting...[/red]")
        exit(1)
    
    display_name, url = choice
    print(f"You selectedhbacv mhvac jfdhvj {display_name}\tURLhbacv mhvac jfdhvj {url}")
    
    return display_name, url
