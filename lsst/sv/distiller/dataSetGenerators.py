class DataSetGeneratorBase:
    """Class to generate tabular datasets for use by measurers

    Parameters:
      butler : `lsst.daf.persistence.Butler`
        Butler for retrieving data
    """
    def __init__(self, butler, *args, **kwargs):
        raise NotImplementedError()

    def generate(self, dataIdList, *args, **kwargs):
        """Function to generate tabular datasets for use by measurers
          dataIdList : `list`
            List of dataIds to use to generate output

        Output:
          result : Table-like thingy
            Table of data
        """
        raise NotImplementedError()
