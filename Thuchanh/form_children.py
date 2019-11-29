import pandas as pd
import numpy as np

data = pd.read_csv("nursery.data")


print ("=================FORM===============")
print("")
data.form = data.iloc[:8640,2]

#------------------FORM---------------

#not_recom 

dt0 = data.form[data.application=="not_recom"]
P_form_not_recom = dt0.value_counts()
P_form_not_recom = P_form_not_recom / dt0.count()
print("-------------not_recom-------------")
print(P_form_not_recom)
#priority

dt0 = data.form[data.application=="priority"]
P_form_priority = dt0.value_counts()
P_form_priority = P_form_priority / dt0.count()
print("------------priority----------")
print(P_form_priority)
#spec_prior 

dt0 = data.form[data.application=="spec_prior"]
P_form_spec_prior = dt0.value_counts()
P_form_spec_prior = P_form_spec_prior / dt0.count()
print("------------spec_prior----------")
print(P_form_spec_prior)
#very_recom 

dt0 = data.form[data.application=="very_recom"]
P_form_very_recom = dt0.value_counts()
P_form_very_recom = P_form_very_recom / dt0.count()
print("------------very_recom----------")
print(P_form_very_recom)
#recommend 

dt0 = data.form[data.application=="recommend"]
P_form_recommend = dt0.value_counts()
P_form_recommend = P_form_recommend / dt0.count()
print("------------recommend----------")
print(P_form_recommend)

#--------------------------------------
print("")
print("")
print("================================================")
print("")
print("")
#----------------CHILDREN---------------
print("=================CHILDREN===============")
print()
data.form = data.iloc[:8640,3]
#not_recom 

dt0 = data.children[data.application=="not_recom"]
P_children_not_recom = dt0.value_counts()
P_children_not_recom = P_children_not_recom / dt0.count()
print("-------------not_recom-------------")
print(P_children_not_recom)
#priority

dt0 = data.children[data.application=="priority"]
P_children_priority = dt0.value_counts()
P_children_priority = P_children_priority / dt0.count()
print("------------priority----------")
print(P_children_priority)
#spec_prior 

dt0 = data.children[data.application=="spec_prior"]
P_children_spec_prior = dt0.value_counts()
P_childrenm_spec_prior = P_children_spec_prior / dt0.count()
print("------------spec_prior----------")
print(P_children_spec_prior)
#very_recom 

dt0 = data.children[data.application=="very_recom"]
P_children_very_recom = dt0.value_counts()
P_children_very_recom = P_children_very_recom / dt0.count()
print("------------very_recom----------")
print(P_children_very_recom)
#recommend 

dt0 = data.children[data.application=="recommend"]
P_children_recommend = dt0.value_counts()
P_children_recommend = P_children_recommend / dt0.count()
print("------------recommend----------")
print(P_children_recommend)
#--------------------------------
print("")
print("================================================")