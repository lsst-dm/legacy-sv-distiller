class MeasurerBase:
    def __init__(self, butler, *args, **kwargs):
        raise NotImplementedError()
    def measure(self, tabularDataset, columnList=None, dataIdList=None, *args, **kwargs):
        """Measure a quantity on the input tabular dataset

        Parameters
        ----------
        tabularDataset : Table-like thingy
          A tabular data structure on which to make a measurement
        columnList : `list`, optional
          An optional list of column names to use in the computation
        dataIdList : `list`, optional
          A list of data ids to use to look up metadata in the input repository

        Output
        ------
        measurement : `lsst.verify.Measurement`
          Measurement of the thing we are measuring
        """
        raise NotImplementedError()
