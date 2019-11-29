import pandas as pd
import numpy as np

data = pd.read_csv("nursery.data")
#Thong ke tan so xuat hien cua cac gia tri cua cac truong parents
data_parent = data.iloc[:8640,0]
  #application = "not_recom"
data_parent = data.parents[data.application=="not_recom"]
P_parents_not_recom = data_parent.value_counts()
P_parents_not_recom = P_parents_not_recom/data_parent.count()
print(P_parents_not_recom)
    #application = "recommend"
data_parent = data.parents[data.application=="recommend"]
P_parents_recommend = data_parent.value_counts()
P_parents_recommend = P_parents_recommend/data_parent.count()
print(P_parents_recommend)
    #application = "very_recom"
data_parent = data.parents[data.application=="very_recom"]
P_parents_very_recom = data_parent.value_counts()
P_parents_very_recom = P_parents_very_recom/data_parent.count()
print(P_parents_very_recom)
    #application = "priority"
data_parent = data.parents[data.application=="priority"]
P_parents_priority = data_parent.value_counts()
P_parents_priority = P_parents_priority/data_parent.count()
print(P_parents_priority)
    #application = "spec_prior"
data_parent = data.parents[data.application=="spec_prior"]
P_parents_spec_prior = data_parent.value_counts()
P_parents_spec_prior = P_parents_spec_prior/data_parent.count()
print(P_parents_priority)



#########################################################
#Thong ke tan so xuat hien cua cac gia tri cua cac truong has_nurs
data_has_nurs = data.iloc[:8640,1]
   #application = "not_recom"
data_has_nurs = data.has_nurs[data.application=="not_recom"]
P_has_nurs_not_recom = data_has_nurs.value_counts()
P_has_nurs_not_recom = P_has_nurs_not_recom/data_has_nurs.count()
print(P_has_nurs_not_recom)
    #application = "recommend"
data_has_nurs = data.has_nurs[data.application=="recommend"]
P_has_nurs_recommend = data_has_nurs.value_counts()
P_has_nurs_recommend = P_has_nurs_recommend/data_has_nurs.count()
print(P_has_nurs_recommend)
    #application = "very_recom"
data_has_nurs = data.has_nurs[data.application=="very_recom"]
P_has_nurs_very_recom = data_has_nurs.value_counts()
P_has_nurs_very_recom = P_has_nurs_very_recom/data_has_nurs.count()
print(P_has_nurs_very_recom)
    #application = "priority"
data_has_nurs = data.has_nurs[data.application=="priority"]
P_has_nurs_priority = data_has_nurs.value_counts()
P_has_nurs_priority = P_has_nurs_priority/data_has_nurs.count()
print(P_has_nurs_priority)
    #application = "spec_prior"
data_has_nurs = data.has_nurs[data.application=="spec_prior"]
P_has_nurs_spec_prior = data_has_nurs.value_counts()
P_has_nurs_spec_prior = P_has_nurs_spec_prior/data_has_nurs.count()
print(P_has_nurs_spec_prior)

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


#############################  social ##################################
dt_social= data.iloc[:8640,6]
#social - recommend
dt0 = dt_social[data.application=="recommend"]

P_social_recommend = dt0.value_counts()
P_social_recommend = P_social_recommend / dt0.count()
print(P_social_recommend)

#social - not_recom
dt0 = dt_social[data.application=="not_recom"]
P_social_not_recom = dt0.value_counts()
P_social_not_recom = P_social_not_recom / dt0.count()
print(P_social_not_recom)

#social - very_recom
dt0 = dt_social[data.application=="very_recom"]
P_social_very_recom = dt0.value_counts()
P_social_very_recom = P_social_very_recom / dt0.count()
print(P_social_very_recom)

#social - priority
dt0 = dt_social[data.application=="priority"]
P_social_priority = dt0.value_counts()
P_social_priority = P_social_priority / dt0.count()
print(P_social_priority)

#social - spec_prior
dt0 = dt_social[data.application=="spec_prior"]
P_social_spec_prior = dt0.value_counts()
P_social_spec_prior = P_social_spec_prior / dt0.count()
print(P_social_spec_prior)

#############################  health ##################################
print("==============================================================")
dt_health= data.iloc[:8640,7]

#heath - recommend
dt0 = dt_health[data.application=="recommend"]
P_health_recommend = dt0.value_counts()
P_health_recommend = P_health_recommend / dt0.count()
print(P_health_recommend)

#health - not_recom
dt0 = dt_health[data.application=="not_recom"]
P_health_not_recom = dt0.value_counts()
P_health_not_recom = P_health_not_recom / dt0.count()
print(P_health_not_recom)
#health - not_very_recom
dt0 = dt_health[data.application=="very_recom"]
P_health_very_recom = dt0.value_counts()
P_health_very_recom = P_health_very_recom / dt0.count()
print(P_health_very_recom)

#health - priority
dt0 = dt_health[data.application=="priority"]
P_health_priority = dt0.value_counts()
P_health_priority = P_health_priority / dt0.count()
print(P_health_priority)

#health - spec_prior
dt0 = dt_health[data.application=="spec_prior"]
P_health_spec_prior = dt0.value_counts()
P_health_spec_prior = P_health_spec_prior / dt0.count()
print(P_health_spec_prior)



### application
print("============ Application ============")
data_app= data.iloc[:8640,8]
app  = data_app.value_counts() / data_app.count()
print(app)


P_not_ret_com =  P_parents_not_recom.great_pret * P_has_nurs_not_recom.very_crit * P_form_not_recom.foster * P_children_not_recom.more * P_housing_not_recom.critical * P_finance_not_recom.convenient * P_social_not_recom.problematic * P_health_not_recom.not_recom *  app.not_recom
#P_priority =  P_parents_priority.great_pret * P_has_nurs_priority.very_crit * P_form_priority.foster * P_children_priority.more * P_housing_priority.critical * P_finance_priority.convenient * P_social_priority.problematic * P_health_priority.not_recom *  app.priority
# P_spec_prior = P_parents_not_recom.great_pret * P_has_nurs_not_recom.very_crit * P_form_not_recom.foster * P_children_not_recom.more * P_housing_not_recom.critical * P_finance_not_recom.convenient * P_social_not_recom.problematic * P_health_not_recom.not_recom *  app.not_recom
# P_very_recom = P_parents_not_recom.great_pret * P_has_nurs_not_recom.very_crit * P_form_not_recom.foster * P_children_not_recom.more * P_housing_not_recom.critical * P_finance_not_recom.convenient * P_social_not_recom.problematic * P_health_not_recom.not_recom *  app.not_recom
# P_recommend = P_parents_not_recom.great_pret * P_has_nurs_not_recom.very_crit * P_form_not_recom.foster * P_children_not_recom.more * P_housing_not_recom.critical * P_finance_not_recom.convenient * P_social_not_recom.problematic * P_health_not_recom.not_recom *  app.not_recom



print(P_health_priority)

