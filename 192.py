underweight_count = underweight_dataframe['index'].count()
value = [underweight_count, healty_weight_count]
label = ["underweight", "hea;thy_weight"]
under_dataframe.groupby('geneder')['gender'].count().reset_index(name='number')	