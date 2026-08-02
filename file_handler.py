# json.dump : eh use hoyega json file de andar data store krn de lai(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, 
#           allow_nan=True, cls=None, indent=None, separators=None, 
#           default=None, sort_keys=False, **kw)

# indent = 4  iss nll ohne indenet a jan ge jine chahide 
# ensure_ascii=False   es nall apa eoji ya kki hor chahrachter use kr skde aa 
# sort_keys=True  ehnde nll data sort hoke mile ga keys da 
# separators=(',', ':'   eh spaces remove kr de ga 


# json.load   eh use hunda json file de andar da data load krn de lai  read mode che (fp, *, cls=None, object_hook=None, parse_float=None, 
        #   parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

# | Parameter         | Type        | Default  | Description                                                                 |
# | ----------------- | ----------- | -------- | --------------------------------------------------------------------------- |
# | fp                | File object | Required | File jahan se JSON read karna hai (.read() support karna chahiye) youtube+1 |
# | object_hook       | function    | None     | Custom dict conversion function                                             |
# | parse_float       | function    | None     | Custom float parsing                                                        |
# | parse_int         | function    | None     | Custom int parsing                                                          |
# | object_pairs_hook | function    | None     | Custom key-value pairs processing      

import json

 

FILE_PATH = "data/expenses.json"

def load_data():

 try:
  
   with open(FILE_PATH, "r") as f :
       data = json.load(f)
       return data
       
       
 except FileNotFoundError:  
   return []  
 
 except json.JSONDecodeError:
     return []
   
      
      
def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)