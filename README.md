# Telecom User Overview & Engagement Analysis

This project involves analyzing user behavior and engagement from a telecom dataset containing xDR (data session details). The goal is to explore user behavior and provide insights to improve user experience and marketing strategies.

## Objectives

1. **User Overview Analysis**
   - Identify top handsets and handset manufacturers.
   - Provide recommendations for marketing.
   - Analyze user behavior on various applications.
   
2. **User Engagement Analysis**
   - Track user engagement metrics like session frequency, duration, and data traffic.
   - Group users based on engagement metrics for QoS improvements.

---

## Task 1: User Overview Analysis

### 1.1 Top Handsets and Manufacturers

- **Top 10 Handsets**: Identify the top 10 most used handsets.
- **Top 3 Handset Manufacturers**: List the top 3 manufacturers based on handset usage.
- **Top 5 Handsets for Each Manufacturer**: Show the top 5 handsets for each of the top 3 manufacturers.

*Recommendation*: Use this information to tailor marketing campaigns for the most popular handset manufacturers.

---

### 1.2 User Behavior on Applications

Aggregate user behavior across applications (e.g., Social Media, YouTube, Google, etc.):
- Number of xDR sessions.
- Session duration.
- Total download (DL) and upload (UL) data.
- Total data volume (Bytes) per application.

#### Exploratory Data Analysis (EDA):

1. **Missing Values & Outliers**:
   - Handle missing values (mean imputation) and detect outliers.

2. **Variable Transformation**: 
   - Segment users into the top five deciles based on total session duration.
   - Compute total DL + UL per decile.

3. **Non-Graphical Univariate Analysis**:
   - Compute dispersion metrics (variance, standard deviation) for quantitative variables.
   - Interpretation of data spread, importance of each variable.

4. **Graphical Univariate Analysis**:
   - Use histograms, box plots, or bar charts for visual analysis.

5. **Bivariate Analysis**:
   - Analyze relationships between app usage (e.g., Social Media vs. total data volume).
   - Use scatter plots, correlation, or regression analysis to identify patterns.

6. **Correlation Analysis**:
   - Calculate a correlation matrix for app usage data (e.g., Social Media, Google, Netflix).
   - Interpret strong or weak relationships between apps.

7. **Dimensionality Reduction**:
   - Perform Principal Component Analysis (PCA).
   - Summarize results into 4 key points (e.g., variance explained by components).

---

## Task 2: User Engagement Analysis

### 2.1 Engagement Metrics

Aggregate metrics for each customer (MSISDN):
- Session frequency.
- Session duration.
- Total data traffic (DL + UL).

#### Steps:

1. **Top 10 Users by Engagement Metrics**:
   - Identify the top 10 users based on each engagement metric.

2. **Normalize Metrics**:
   - Normalize the engagement metrics to standardize values.
   - Use k-means clustering (k=3) to group users into 3 engagement categories (low, medium, high).

3. **Cluster Analysis**:
   - Calculate min, max, average, and total values for each cluster.
   - Visualize results using charts (e.g., bar plots, pie charts).

4. **Top Users per Application**:
   - Identify the top 10 users per application by total traffic.

5. **Most Used Applications**:
   - Plot the top 3 most used applications (e.g., bar chart).

6. **k-means Clustering Optimization**:
   - Use the elbow method to determine the optimal value of k for clustering.
   - Interpret the findings by analyzing the user engagement levels in each cluster.

---

## Technologies Used

- **Python Libraries**: pandas, matplotlib, seaborn, scikit-learn, numpy.
- **Data Analysis Tools**: Jupyter Notebook.

---

## Key Insights

- **Top Handsets & Manufacturers**: Marketing can focus on the top 3 manufacturers to optimize their strategies.
- **App Usage Insights**: High traffic on specific apps like YouTube and Social Media can help the telecom company allocate resources effectively.
- **User Engagement**: Grouping users based on engagement metrics can guide improvements in network infrastructure and resource allocation.
