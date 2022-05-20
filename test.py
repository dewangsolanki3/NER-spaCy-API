dict_sub = {'math':100,'Eng':100,'Chem':98,'students':'Jack'}

def val_append(dict_obj, key, value):
 if key in dict_sub:
  if not isinstance(dict_sub[key], list):
  # converting key to list type
   dict_sub[key] = [dict_sub[key]]
   # Append the key's value in list
   dict_sub[key].append(value)
 else:
     dict_sub[key] = value
 
#calling the function to append values
val_append(dict_sub,'sex','male')
 
print('after adding value to dictionary =\n',dict_sub)