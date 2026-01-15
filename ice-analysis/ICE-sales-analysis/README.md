# Video Game Sales Analysis - Ice Online Store: #
## Project Overview: ##
This project analyzes historical video game sales and reviews to identify patterns that determine a game's commercial success. The goal is to provide actionable insights for the online store Ice to plan marketing campaigns and focus on potentially profitable games and platforms for the upcoming year (2017).

The analysis covers:
- Platform trends over time
- Genre performance
- Regional sales (North America, Europe, Japan)
- Critic and user ratings effects on sales
- ESRB rating effects
- Hypothesis testing on user ratings

## Dataset: ##
**name**	Game title
**platform**	Gaming platform (e.g., PS4, Xbox One)
**year_of_release**	Year of game release
**genre**	Game genre
**na_sales**	North American sales (millions USD)
**eu_sales**	European sales (millions USD)
**jp_sales**	Japanese sales (millions USD)
**other_sales**	Sales in other regions (millions USD)
**critic_score**	Critic rating (max 100)
**user_score**	User rating (max 10)
**rating**	ESRB content rating (e.g., Teen, Mature)

**Notes on Dataset:**
- Some values are missing or marked as 'TBD' (To Be Determined) and were handled during preprocessing.
- Total global sales were calculated as the sum of regional sales.

## Project Workflow: ##
**1. Data Preparation**
  - Standardized column names to lowercase.
  - Converted data types for consistency (e.g., numeric for scores and sales).
  - Handled missing values and TBD entries thoughtfully, explaining the rationale.
**2. Exploratory Data Analysis (EDA)**
  - Analyzed the number of games released per year to determine data relevance.
  - Investigated sales distribution across platforms and identified leading and declining platforms.
  - Selected a relevant period of data to forecast 2017 trends.
  - Explored relationships between critic/user scores and sales with scatter plots and correlations.
  - Analyzed genre performance and profitability trends.
**3. Regional Analysis / User Profiles**
  - For North America (NA), Europe (EU), and Japan (JP):
    - Identified the top 5 platforms and top 5 genres.
    - Examined differences in regional sales patterns.
    - Analyzed the effect of ESRB ratings on regional sales.
**4. Hypothesis Testing**
- Tested whether average user ratings for Xbox One and PC are the same.
- Tested whether average user ratings for Action and Sports genres differ.
  - Explained null/alternative hypotheses, significance level, and choice of statistical tests.
**5. Insights and Conclusions**
- Summarized findings on which platforms, genres, and ratings are most likely to succeed.
- Provided recommendations for marketing campaigns and potential profitable games.

## Tools and Libraries: ##
- Python 3
- Pandas, NumPy for data manipulation
- Matplotlib, Seaborn for visualization
- SciPy for hypothesis testing
- Jupyter Notebook for analysis

***Included the .venv (virtual environment) used for all libraries and tools***

**Key Takeaways:**
- Certain platforms dominate global sales, while others decline over time.
- Critic and user scores moderately correlate with sales; highly rated games tend to sell more.
- Regional differences exist: genres and ratings impact NA, EU, and JP differently.
- Hypothesis testing validates significant differences between user ratings for selected platforms/genres.
