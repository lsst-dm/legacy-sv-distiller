class AggregatorBase:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError()
    def aggregate(self, measurementList, *args, **kwargs):
        """Aggregate a list of measurements

        Parameters
        ----------
          measurementList : `list` of `lsst.verify.Measurement`
            List of measurements to aggregate

        Output
        ------
          measurement : `lsst.verify.Measurement`
            Aggregated measurement
        """
        raise NotImplementedError()
