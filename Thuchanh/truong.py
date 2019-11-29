
import pandas as pd
import numpy as np

data = pd.read_csv("nursery.data")
#housing

dt_housing = data.iloc[:8640,4]
dt_housing = data.housing[data.application=="recommend"]
P_housing_recommend = dt_housing.value_counts()
P_housing_recommend = P_housing_recommend / dt_housing.count()
print(P_housing_recommend)


dt_housing = data.housing[data.application=="priority"]
P_housing_priority = dt_housing.value_counts()
P_housing_priority = P_housing_priority / dt_housing.count()
print(P_housing_priority)


dt_housing = data.housing[data.application=="not_recom"]
P_housing_not_recom = dt_housing.value_counts()
P_housing_not_recom = P_housing_not_recom / dt_housing.count()
print(P_housing_not_recom)


dt_housing = data.housing[data.application=="spec_prior"]
P_housing_spec_prior = dt_housing.value_counts()
P_housing_spec_prior = P_housing_spec_prior / dt_housing.count()
print(P_housing_spec_prior)


dt_housing = data.housing[data.application=="very_recom"]
P_housing_very_recom = dt_housing.value_counts()
P_housing_very_recom = P_housing_very_recom / dt_housing.count()
print(P_housing_very_recom)

#finance

dt_finance = data.iloc[:8640,5]
dt_finance = data.finance[data.application=="recommend"]
P_finance_recommend = dt_finance.value_counts()
P_finance_recommend = P_finance_recommend / dt_finance.count()
print(P_finance_recommend)

dt_finance = data.finance[data.application=="priority"]
P_finance_priority = dt_finance.value_counts()
P_finance_priority = P_finance_priority / dt_finance.count()
print(P_finance_priority)

dt_finance = data.finance[data.application=="not_recom"]
P_finance_not_recom = dt_finance.value_counts()
P_finance_not_recom = P_finance_not_recom / dt_finance.count()
print(P_finance_not_recom)

dt_finance = data.finance[data.application=="spec_prior"]
P_finance_spec_prior = dt_finance.value_counts()
P_finance_spec_prior = P_finance_spec_prior / dt_finance.count()
print(P_finance_spec_prior)

dt_finance = data.finance[data.application=="very_recom"]
P_finance_very_recom = dt_finance.value_counts()
P_finance_very_recom = P_finance_very_recom / dt_finance.count()
print(P_finance_very_recom)
