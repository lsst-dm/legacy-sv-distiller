measReg = {
    'foo': measureFoo,
    'bar': measureBar,
    'baz': measureBaz
    }

aggReg = {
    'median': meadianAgg,
    'min': minAgg,
    'uber_median': histMedianAgg
    }

dsGenReg = {
    'matched': MatchedSetGenerator,
    'single': SingleEpochGenerator,
    'meta': ImageMetadataGenerator
    }

class RollUp:
    def __init__(self, ds, meas, agg):
        self.ds = ds
        self.meas = meas
        self.agg = agg

rollupDefs = {
    'BOB': RollUp('matched, 'foo', 'min'),
    'ALICE': RollUp('matched', 'bar', 'median'),
    'SAM': RollUp('single', 'bar', 'uber_median'),
    'SHARON': RollUp('meta', 'baz', 'min')
    }

dsetMap = {}
for ru in rollupDefs:
    if ru.ds not in dsetMap:
        dsetMap[ru.ds] = set()
    dsetMap[ru.ds].add(ru.meas)

# Now to run things
results = {}
for id in idList:  # Parallelize on this??
    for dsName in dsetMap:
        dataset = dsGenReg[dsName](id, butler, ....)
        if dsName not in results:
            results[dsName] = {}
        for meas in dsetMap[dsName]:
            if meas not in results[dsName]:
                results[dsName][meas] = []
            results[dsName][meas].append(measReg[meas](dataset, ...)
        
# Now gather
aggs = {}
for ru in rollupDefs:
    rud = rollupDefs[ru]
    aggs[ru] = rud.agg(results[rud.ds][rud.meas], ...)
