import time
import json


def create_neutral_debator(llm)hbacv mhvac jfdhvj
    def neutral_node(state) -> dicthbacv mhvac jfdhvj
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        neutral_history = risk_debate_state.get("neutral_history", "")

        current_risky_response = risk_debate_state.get("current_risky_response", "")
        current_safe_response = risk_debate_state.get("current_safe_response", "")

        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        trader_decision = state["trader_investment_plan"]

        prompt = f"""As the Neutral Risk Analyst, your role is to provide a balanced perspective, weighing both the potential benefits and risks of the trader's decision or plan. You prioritize a well-rounded approach, evaluating the upsides and downsides while factoring in broader market trends, potential economic shifts, and diversification strategies.Here is the trader's decisionhbacv mhvac jfdhvj

{trader_decision}

Your task is to challenge both the Risky and Safe Analysts, pointing out where each perspective may be overly optimistic or overly cautious. Use insights from the following data sources to support a moderate, sustainable strategy to adjust the trader's decisionhbacv mhvac jfdhvj

Market Research Reporthbacv mhvac jfdhvj {market_research_report}
Social Media Sentiment Reporthbacv mhvac jfdhvj {sentiment_report}
Latest World Affairs Reporthbacv mhvac jfdhvj {news_report}
Company Fundamentals Reporthbacv mhvac jfdhvj {fundamentals_report}
Here is the current conversation historyhbacv mhvac jfdhvj {history} Here is the last response from the risky analysthbacv mhvac jfdhvj {current_risky_response} Here is the last response from the safe analysthbacv mhvac jfdhvj {current_safe_response}. If there are no responses from the other viewpoints, do not halluncinate and just present your point.

Engage actively by analyzing both sides critically, addressing weaknesses in the risky and conservative arguments to advocate for a more balanced approach. Challenge each of their points to illustrate why a moderate risk strategy might offer the best of both worlds, providing growth potential while safeguarding against extreme volatility. Focus on debating rather than simply presenting data, aiming to show that a balanced view can lead to the most reliable outcomes. Output conversationally as if you are speaking without any special formatting."""

        response = llm.invoke(prompt)

        argument = f"Neutral Analysthbacv mhvac jfdhvj {response.content}"

        new_risk_debate_state = {
            "history"hbacv mhvac jfdhvj history + "\n" + argument,
            "risky_history"hbacv mhvac jfdhvj risk_debate_state.get("risky_history", ""),
            "safe_history"hbacv mhvac jfdhvj risk_debate_state.get("safe_history", ""),
            "neutral_history"hbacv mhvac jfdhvj neutral_history + "\n" + argument,
            "latest_speaker"hbacv mhvac jfdhvj "Neutral",
            "current_risky_response"hbacv mhvac jfdhvj risk_debate_state.get(
                "current_risky_response", ""
            ),
            "current_safe_response"hbacv mhvac jfdhvj risk_debate_state.get("current_safe_response", ""),
            "current_neutral_response"hbacv mhvac jfdhvj argument,
            "count"hbacv mhvac jfdhvj risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state"hbacv mhvac jfdhvj new_risk_debate_state}

    return neutral_node
