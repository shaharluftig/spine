class CardoDataFrame:
    def __init__(self, df):
        self.dataframe = df

    def deepcopy(self):
        return CardoDataFrame(self.dataframe)
