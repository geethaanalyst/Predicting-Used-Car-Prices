# Predicting-Used-Car-Prices
Develop a robust machine learning model to accurately predict used car prices in the market. By utilizing this model, the company aims to improve pricing recommendations, optimize inventory management, and help both buyers and sellers make informed decisions.

## **Introduction** 
Empower a leading used car marketplace to optimize pricing, inventory, and decision-making through data analysis and machine learning on market data across major metro cities.
Develop a robust machine learning model to accurately predict used car prices in the market. 
By utilizing this model, the company aims to improve pricing recommendations, optimize inventory management, and help both buyers and sellers make informed decisions.
 
## **Deployment Flow** 
<img width="962" height="412" alt="image" src="https://github.com/user-attachments/assets/d52c446c-640f-4a8d-84ed-403f8a6a9b91" />

## **Dataset Overview** 
<img width="867" height="537" alt="image" src="https://github.com/user-attachments/assets/8d69c201-c27a-4c9d-9bff-0966e7c14c98" />


## **Data Preprocessing**
* **Checked for missing values:  No missing data was found.**
* **Detecting and removing Outlier (Price and Kilometer).**
* **Cleaned and imputed missing categorical and numerical features.**
* **Converted categorical features to numerical using encoding (one hot encoding).**
* **Split data into training (80%) and testing (20%) sets for model building.** 

## **Exploratory Data Analysis**
### **Top 5 Companies by Listings**
<img width="600" height="235" alt="image" src="https://github.com/user-attachments/assets/ba13d2e2-a4ac-44f7-93ab-75621ab92612" />

### **Distribution of body style**
* **Hatchback**
* **Sedan**
* **SUV**
* **MPV**
* **MUV/Van**

## **Visualization on Power BI**
<img width="1415" height="783" alt="image" src="https://github.com/user-attachments/assets/51af9d65-bf5d-47ee-8141-1bc8e9219bb0" />


## **Key Findings**
### **Most Influential Factors**
* **Model and brand**
* **Car age and kilometer driven**
* **Vehicle quality score**
* **City Location (Metro/Other Region)**
* **Number of Previous Owners: Fewer owners are generally associated with higher prices.**
### **Model Performance:**
* **MAE ~0.87 lakh INR: Typical prediction error per car** 
* **R² of 0.85: Strong prediction accuracy**

## **Machine Learning Models**
All models were evaluated using metrics MAE, MSE, RMSE and R² Score to ensure robust performance comparison.

### **Models Used**
* **Linear Regression**
* **Decision Tree Regressor**
* **Random Forest Regressor**
* **XGBoost Regressor**
### **Model Performance**
<img width="832" height="202" alt="image" src="https://github.com/user-attachments/assets/4967fcd7-7c6f-4567-9945-dc71097499ec" />

## **Recommendations**
To improve on-time delivery rates and customer satisfaction, the company should:

* **Optimize shipment mode selection based on delivery reliability.**
* **Proactively address shipments issues with multiple customer care calls.**
* **Use customer ratings to identify and fix recurring delivery issues.**
* **Prioritize high-importance and high-discount shipments for timely handling.**
* **Regularly analyse warehouse and route performance for targeted improvements.**
* **Implement predictive analytics to identify and intervene in at-risk shipments.**

## **Conclusion**
* **The project's objective was to forecast on-time delivery for an e-commerce company's products and to explore factors influencing delivery times and customer behaviour.**
* **The exploratory analysis highlighted that product weight and cost are crucial to delivery success, with products in the 4000-6000 gms range and priced approximately $300 being more likely to arrive on time. A significant volume of products was dispatched from warehouse F using shipping, suggesting its proximity to a seaport.**
* **Customer behaviour also sheds light on delivery outcomes. An increase in customer care calls often correlates with delivery delays.**
* **In contrast, customers with a history of multiple purchases tend to experience more punctual deliveries, which might explain their repeat business.**
* **Products with discounts ranging from 0-10% tend to arrive on time. Meanwhile, products with discounts above 10% are more likely to not arrive on time.**



