# 📊 Students Social Media Addiction - Data Cleaning Report

**Total Rows Before Cleaning:** 705

### 🔍 Sample Data Before Cleaning:
|   Student_ID |   Age | Gender   | Academic_Level   | Country    |   Avg_Daily_Usage_Hours | Most_Used_Platform   | Affects_Academic_Performance   |   Sleep_Hours_Per_Night |   Mental_Health_Score | Relationship_Status   |   Conflicts_Over_Social_Media |   Addicted_Score |
|-------------:|------:|:---------|:-----------------|:-----------|------------------------:|:---------------------|:-------------------------------|------------------------:|----------------------:|:----------------------|------------------------------:|-----------------:|
|            1 |    19 | Female   | Undergraduate    | Bangladesh |                     5.2 | Instagram            | Yes                            |                     6.5 |                     6 | In Relationship       |                             3 |                8 |
|            2 |    22 | Male     | Graduate         | India      |                     2.1 | Twitter              | No                             |                     7.5 |                     8 | Single                |                           nan |                3 |
|            3 |    20 | Female   | Undergraduate    | USA        |                     6   | TikTok               | Yes                            |                     5   |                     5 | Complicated           |                             4 |                9 |
|            4 |    18 | Male     | High School      | UK         |                     3   | YouTube              | No                             |                     7   |                     7 | Single                |                             1 |                4 |
|            5 |    21 | Male     | Graduate         | Canada     |                     4.5 | Facebook             | Yes                            |                     6   |                     6 | In Relationship       |                             2 |                7 |

**Total Rows After Cleaning:** 701

### ✅ Sample Data After Cleaning:
|   Student_ID |   Age | Gender   | Academic_Level   | Country    |   Avg_Daily_Usage_Hours | Most_Used_Platform   | Affects_Academic_Performance   |   Sleep_Hours_Per_Night |   Mental_Health_Score | Relationship_Status   |   Conflicts_Over_Social_Media |   Addicted_Score | Addiction_Level   |
|-------------:|------:|:---------|:-----------------|:-----------|------------------------:|:---------------------|:-------------------------------|------------------------:|----------------------:|:----------------------|------------------------------:|-----------------:|:------------------|
|            1 |    19 | Female   | Undergraduate    | Bangladesh |                     5.2 | Instagram            | Yes                            |                     6.5 |                     6 | In Relationship       |                             3 |                8 | High              |
|            3 |    20 | Female   | Undergraduate    | USA        |                     6   | TikTok               | Yes                            |                     5   |                     5 | Complicated           |                             4 |                9 | High              |
|            4 |    18 | Male     | High School      | UK         |                     3   | YouTube              | No                             |                     7   |                     7 | Single                |                             1 |                4 | Moderate          |
|            5 |    21 | Male     | Graduate         | Canada     |                     4.5 | Facebook             | Yes                            |                     6   |                     6 | In Relationship       |                             2 |                7 | High              |
|            6 |    19 | Female   | Undergraduate    | Australia  |                     7.2 | Instagram            | Yes                            |                     4.5 |                     4 | Complicated           |                             5 |                9 | High              |

### 🔧 Transformations Applied:
- Replaced `0` in `Conflicts_Over_Social_Media` with null (NaN)
- Dropped rows with missing values in key columns
- Filtered rows with age between 15 and 30
- Removed entries with usage > 24 hours/day
- Added new column `Addiction_Level` based on `Addicted_Score`
