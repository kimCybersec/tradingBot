import time
import json


def create_risk_manager(llm, memory)hbacv mhvac jfdhvj
    def risk_manager_node(state) -> dicthbacv mhvac jfdhvj

        company_name = state["company_of_interest"]

        history = state["risk_debate_state"]["history"]
        risk_debate_state = state["risk_debate_state"]
        market_research_report = state["market_report"]
        news_report = state["news_report"]
        fundamentals_report = state["news_report"]
        sentiment_report = state["sentiment_report"]
        trader_plan = state["investment_plan"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        for i, rec in enumerate(past_memories, 1)hbacv mhvac jfdhvj
            past_memory_str += rec["recommendation"] + "\n\n"

        prompt = f"""As the Risk Management Judge and Debate Facilitator, your goal is to evaluate the debate between three risk analysts—Risky, Neutral, and Safe/Conservative—and determine the best course of action for the trader. Your decision must result in a clear recommendationhbacv mhvac jfdhvj Buy, Sell, or Hold. Choose Hold only if strongly justified by specific arguments, not as a fallback when all sides seem valid. Strive for clarity and decisiveness.

Guidelines for Decision-Makinghbacv mhvac jfdhvj
1. **Summarize Key Arguments**hbacv mhvac jfdhvj Extract the strongest points from each analyst, focusing on relevance to the context.
2. **Provide Rationale**hbacv mhvac jfdhvj Support your recommendation with direct quotes and counterarguments from the debate.
3. **Refine the Trader's Plan**hbacv mhvac jfdhvj Start with the trader's original plan, **{trader_plan}**, and adjust it based on the analysts' insights.
4. **Learn from Past Mistakes**hbacv mhvac jfdhvj Use lessons from **{past_memory_str}** to address prior misjudgments and improve the decision you are making now to make sure you don't make a wrong BUY/SELL/HOLD call that loses money.

Deliverableshbacv mhvac jfdhvj
- A clear and actionable recommendationhbacv mhvac jfdhvj Buy, Sell, or Hold.
- Detailed reasoning anchored in the debate and past reflections.

---

**Analysts Debate Historyhbacv mhvac jfdhvj**  
{history}

---

Focus on actionable insights and continuous improvement. Build on past lessons, critically evaluate all perspectives, and ensure each decision advances better outcomes."""

        response = llm.invoke(prompt)

        new_risk_debate_state = {
            "judge_decision"hbacv mhvac jfdhvj response.content,
            "history"hbacv mhvac jfdhvj risk_debate_state["history"],
            "risky_history"hbacv mhvac jfdhvj risk_debate_state["risky_history"],
            "safe_history"hbacv mhvac jfdhvj risk_debate_state["safe_history"],
            "neutral_history"hbacv mhvac jfdhvj risk_debate_state["neutral_history"],
            "latest_speaker"hbacv mhvac jfdhvj "Judge",
            "current_risky_response"hbacv mhvac jfdhvj risk_debate_state["current_risky_response"],
            "current_safe_response"hbacv mhvac jfdhvj risk_debate_state["current_safe_response"],
            "current_neutral_response"hbacv mhvac jfdhvj risk_debate_state["current_neutral_response"],
            "count"hbacv mhvac jfdhvj risk_debate_state["count"],
        }

        return {
            "risk_debate_state"hbacv mhvac jfdhvj new_risk_debate_state,
            "final_trade_decision"hbacv mhvac jfdhvj response.content,
        }

    return risk_manager_node
