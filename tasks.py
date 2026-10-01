from crewai import Task

def create_tasks(user_input, fact_checker, context_analyst, chief_editor):
    task1 = Task(
        description=f"Examine this specific user payload: '{user_input}'. Isolate core claims. Perform an exhaustive live web search. Look for corroboration from premium outlets or authoritative refutations by official agencies.",
        expected_output="A list of confirmed fact matches, clear context rejections, and precise names of online publishers making or debunking the claim.",
        agent=fact_checker
    )

    task2 = Task(
        description=f"Analyze the historical context of the user payload: '{user_input}'. If it is a link or contains image references, attempt to locate the absolute earliest recorded upload date. Determine if it is being stripped of its original meaning to manipulate current public opinion.",
        expected_output="A structured timeline breakdown explicitly highlighting any chronological or contextual distortion.",
        agent=context_analyst
    )

    task3 = Task(
        description="Review all findings delivered by the technical agents. Generate a polished, high-impact Truth Verification Report. The output must adhere to this markdown format:\n"
                         "### 📊 Verdict & Threat Score\n"
                         "- **Overall Assessment:** [Real / Misleading / Fabricated]\n"
                         "- **Suspicion Index:** [0% to 100%]\n\n"
                         "### 🔍 Structural Evidence\n"
                         "- [Bullet point breakdowns of discrepancies discovered]\n\n"
                         "### 🌐 Authoritative References & Citations\n"
                         "- Provide clear, live hyperlinks to verified source URLs.",
        expected_output="A meticulously structured, professional markdown analysis report with precise metrics and external verification links.",
        agent=chief_editor
    )
    
    return [task1, task2, task3]
