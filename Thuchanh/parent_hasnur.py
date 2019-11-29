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





