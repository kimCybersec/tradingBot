from langchain_core.messages import AIMessage
import time
import json


def create_bull_researcher(llm, memory)hbacv mhvac jfdhvj
    def bull_node(state) -> dicthbacv mhvac jfdhvj
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bull_history = investment_debate_state.get("bull_history", "")

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

        prompt = f"""You are a Bull Analyst advocating for investing in the stock. Your task is to build a strong, evidence-based case emphasizing growth potential, competitive advantages, and positive market indicators. Leverage the provided research and data to address concerns and counter bearish arguments effectively.

Key points to focus onhbacv mhvac jfdhvj
- Growth Potentialhbacv mhvac jfdhvj Highlight the company's market opportunities, revenue projections, and scalability.
- Competitive Advantageshbacv mhvac jfdhvj Emphasize factors like unique products, strong branding, or dominant market positioning.
- Positive Indicatorshbacv mhvac jfdhvj Use financial health, industry trends, and recent positive news as evidence.
- Bear Counterpointshbacv mhvac jfdhvj Critically analyze the bear argument with specific data and sound reasoning, addressing concerns thoroughly and showing why the bull perspective holds stronger merit.
- Engagementhbacv mhvac jfdhvj Present your argument in a conversational style, engaging directly with the bear analyst's points and debating effectively rather than just listing data.

Resources availablehbacv mhvac jfdhvj
Market research reporthbacv mhvac jfdhvj {market_research_report}
Social media sentiment reporthbacv mhvac jfdhvj {sentiment_report}
Latest world affairs newshbacv mhvac jfdhvj {news_report}
Company fundamentals reporthbacv mhvac jfdhvj {fundamentals_report}
Conversation history of the debatehbacv mhvac jfdhvj {history}
Last bear argumenthbacv mhvac jfdhvj {current_response}
Reflections from similar situations and lessons learnedhbacv mhvac jfdhvj {past_memory_str}
Use this information to deliver a compelling bull argument, refute the bear's concerns, and engage in a dynamic debate that demonstrates the strengths of the bull position. You must also address reflections and learn from lessons and mistakes you made in the past.
"""

        response = llm.invoke(prompt)

        argument = f"Bull Analysthbacv mhvac jfdhvj {response.content}"

        new_investment_debate_state = {
            "history"hbacv mhvac jfdhvj history + "\n" + argument,
            "bull_history"hbacv mhvac jfdhvj bull_history + "\n" + argument,
            "bear_history"hbacv mhvac jfdhvj investment_debate_state.get("bear_history", ""),
            "current_response"hbacv mhvac jfdhvj argument,
            "count"hbacv mhvac jfdhvj investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state"hbacv mhvac jfdhvj new_investment_debate_state}

    return bull_node
