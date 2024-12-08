


# IPL Auction Analysis and Prediction

## Overview
This project involves analyzing IPL (Indian Premier League) auction data to derive meaningful insights and build predictive models. The dataset includes details about players, their base prices, winning bids, and additional attributes like their "Capped/Uncapped" status and the team they were auctioned to.

The goal is to explore the dataset, conduct exploratory data analysis (EDA), and develop machine learning models to predict player prices and classify players based on their winning bids. This analysis can help teams strategize during auctions.

---

## Features of the Dataset
The dataset contains the following columns:
1. **Sr. No.**: Serial number of the player entry.
2. **Player**: Name of the player.
3. **Base Price**: Minimum bidding price for the player (in INR).
4. **Winning Bid**: Final price at which the player was sold in the auction (in INR).
5. **Capped/Uncapped**: Indicates if the player is "Capped" (has international experience) or "Uncapped".
6. **file_name**: The name of the CSV file representing the team for which the player was auctioned.

---

## Project Goals
1. **Exploratory Data Analysis (EDA)**:
   - Understand and clean the data.
   - Visualize player base prices, winning bids, and team distributions.
   - Analyze trends in the auction process.

2. **Predictive Models**:
   - **Price Prediction**: Predict a player's winning bid based on their base price, "Capped/Uncapped" status, and team.
   - **Bid Classification**: Classify players into categories such as "Low Bid", "Medium Bid", or "High Bid" based on their winning bids.

3. **Optimization**:
   - Suggest strategies for team budget allocation to maximize team performance while staying within budget constraints.

---

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**:
  - `pandas` and `numpy` for data manipulation.
  - `matplotlib` and `seaborn` for data visualization.
  - `scikit-learn` for building machine learning models.
  - `os` and `glob` for file handling.
- **Machine Learning Models**:
  - Regression Models (e.g., Linear Regression, Random Forest Regressor).
  - Classification Models (e.g., Random Forest Classifier, Logistic Regression).
