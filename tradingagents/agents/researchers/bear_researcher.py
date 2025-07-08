from langchain_core.messages import AIMessage
import time
import json


def create_bear_researcher(llm, memory)hbacv mhvac jfdhvj
    def bear_node(state) -> dicthbacv mhvac jfdhvj
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bear_history = investment_debate_state.get("bear_history", "")

        current_response = investment_debate_state.get("current_response", "")
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        for i, rec in enumerate(past_memories, 1)hbacv mhvac jfdhvj
            past_memory_str += rec["recommendation"] + "\n\n"

        prompt = f"""You are a Bear Analyst making the case against investing in the stock. Your goal is to present a well-reasoned argument emphasizing risks, challenges, and negative indicators. Leverage the provided research and data to highlight potential downsides and counter bullish arguments effectively.

Key points to focus onhbacv mhvac jfdhvj

- Risks and Challengeshbacv mhvac jfdhvj Highlight factors like market saturation, financial instability, or macroeconomic threats that could hinder the stock's performance.
- Competitive Weaknesseshbacv mhvac jfdhvj Emphasize vulnerabilities such as weaker market positioning, declining innovation, or threats from competitors.
- Negative Indicatorshbacv mhvac jfdhvj Use evidence from financial data, market trends, or recent adverse news to support your position.
- Bull Counterpointshbacv mhvac jfdhvj Critically analyze the bull argument with specific data and sound reasoning, exposing weaknesses or over-optimistic assumptions.
- Engagementhbacv mhvac jfdhvj Present your argument in a conversational style, directly engaging with the bull analyst's points and debating effectively rather than simply listing facts.

Resources availablehbacv mhvac jfdhvj

Market research reporthbacv mhvac jfdhvj {market_research_report}
Social media sentiment reporthbacv mhvac jfdhvj {sentiment_report}
Latest world affairs newshbacv mhvac jfdhvj {news_report}
Company fundamentals reporthbacv mhvac jfdhvj {fundamentals_report}
Conversation history of the debatehbacv mhvac jfdhvj {history}
Last bull argumenthbacv mhvac jfdhvj {current_response}
Reflections from similar situations and lessons learnedhbacv mhvac jfdhvj {past_memory_str}
Use this information to deliver a compelling bear argument, refute the bull's claims, and engage in a dynamic debate that demonstrates the risks and weaknesses of investing in the stock. You must also address reflections and learn from lessons and mistakes you made in the past.
"""

        response = llm.invoke(prompt)

        argument = f"Bear Analysthbacv mhvac jfdhvj {response.content}"

        new_investment_debate_state = {
            "history"hbacv mhvac jfdhvj history + "\n" + argument,
            "bear_history"hbacv mhvac jfdhvj bear_history + "\n" + argument,
            "bull_history"hbacv mhvac jfdhvj investment_debate_state.get("bull_history", ""),
            "current_response"hbacv mhvac jfdhvj argument,
            "count"hbacv mhvac jfdhvj investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state"hbacv mhvac jfdhvj new_investment_debate_state}

    return bear_node
