from datetime import date, timedelta

# Define your date range
start_date = date(2025, 4, 18)
end_date   = date(2025, 7, 11)
delta      = timedelta(days=1)

# Weekly chunks
weekly_content = {
    1: [
        "Intro to SQL + WideWorldImporters setup",
        "Basic SELECT queries and filtering",
        "JOINs and Aggregations",
        "Subqueries and Views",
        "CASE, IFs, and advanced filters",
        "Practice SQL problems (LeetCode)",
        "Project: Create 2 sales reports in SSMS",
    ],
    # … include weeks 2 through 12 exactly as we generated before …
}

# Build the full daily plan dict
prep_plan = {}
current = start_date
week   = 1
day_i  = 0

while current <= end_date and week <= len(weekly_content):
    if day_i >= len(weekly_content[week]):
        week += 1
        day_i = 0
        continue
    prep_plan[current.strftime("%Y-%m-%d")] = weekly_content[week][day_i]
    current += delta
    day_i  += 1

