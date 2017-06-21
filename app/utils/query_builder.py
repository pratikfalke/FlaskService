from __future__ import print_function
from __future__ import unicode_literals


exclude_params = set([
    '_page', 
    '_page_size'
])

# queryable: Collection or Query
def build_mongo_query_cond(args, init_cond={}):
    condition = init_cond.copy()
    p_keys = filter(lambda k: k not in exclude_params, 
                    args.keys())
    
    for k in p_keys:
        values = args[k].split(',')
        if len(values) == 1:
            condition[k] = values[0]
        else:
            condition[k] = {'$in': values}

    return condition
        