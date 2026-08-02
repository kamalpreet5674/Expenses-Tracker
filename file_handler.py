# json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, 
#           allow_nan=True, cls=None, indent=None, separators=None, 
#           default=None, sort_keys=False, **kw)

# indent = 4  iss nll ohne indenet a jan ge jine chahide 
# ensure_ascii=False   es nall apa eoji ya kki hor chahrachter use kr skde aa 
# sort_keys=True  ehnde nll data sort hoke mile ga keys da 
# separators=(',', ':'   eh spaces remove kr de ga 


# json.load(fp, *, cls=None, object_hook=None, parse_float=None, 
        #   parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

# | Parameter         | Type        | Default  | Description                                                                 |
# | ----------------- | ----------- | -------- | --------------------------------------------------------------------------- |
# | fp                | File object | Required | File jahan se JSON read karna hai (.read() support karna chahiye) youtube+1 |
# | object_hook       | function    | None     | Custom dict conversion function                                             |
# | parse_float       | function    | None     | Custom float parsing                                                        |
# | parse_int         | function    | None     | Custom int parsing                                                          |
# | object_pairs_hook | function    | None     | Custom key-value pairs processing                                           |