import os

# for evaluation usage
# qid_year=dict(zip(list(range(1,301)), ['mb09'] * 50 + ['mb10'] * 50 + \
#                 ['mb11'] * 50 + ['mb12'] * 50 + ['mb13'] * 50 + ['mb14'] * 50))

year_qids={'mb11':list(range(1,50)),'mb12':list(range(51,111)), 'mb13':list(range(111,171)), 'mb14':list(range(171,226))}

def get_train_qids(year, years=['mb11', 'mb12', 'mb13']):
    if year.startswith('mb'):
        prefix = 'mb'
    a_qids = list()
    for y in year[len(prefix):].split('_'):
        a_qids.extend(year_qids['%s%s'%(prefix, y)])
    return a_qids

def get_qrelf(basepath, year):
    if year.startswith("mb"):
        qrelf = os.path.join(basepath, 'qrels.adhoc.6y')
    else:
        print("WARNING: no qrelf exists for get_train_qids on year: %s" % year)
        qrelf = None
        
    return qrelf

