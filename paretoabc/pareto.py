import pandas as pd


class ParetoABC:

    def __init__(self, df: pd.DataFrame, abc_column: str, label_a: float = 0.2,
                 label_b: float = 0.5):
        """

        Parameters
        ----------
        df: pandas.DataFrame
            data with numeric column to be used in abc analysis
        abc_column: str
            column with derired data for abc anls
         label_a: float, optional
            A Label - best 20% (default is 0.2)
         label_b: float, optional
            B Label - best category after A Label (default is 0.5).
            C Label - worst performing group, is defined by 1 - (a_label+b_label).
        """

        self.df = df.copy()
        self.abc_column = abc_column

        self._order_by_values()

        self.values = self.df[self.abc_column]

        self.total_items = 0
        self.total_values = 0
        self.items_rank = pd.Series([0])
        self.item_perc = pd.Series([0])
        self.values_perc = pd.Series([0])
        self.values_cum_perc = pd.Series([0])
        self.labels = pd.Series([0])

        self.label_a = label_a
        self.label_b = label_b
        self.label_c = 1 - (label_a + label_b)

        self.abc_columns_names = {"rank": "rank", "item_perc": "items representation",
                                  "values_perc": "values representation", "label": 'abc_labels'}

        self.abc_summary_table = pd.DataFrame({})

    def _order_by_values(self):
        """order dataframe by the values of abc_column"""
        self.df.sort_values(by=self.abc_column, inplace=True, ascending=False)
        self.df.index = range(self.df.shape[0])

    def _make_rank(self):
        """
        Returns
        -------
        Pandas.Series
            rank of values of abc_column
        """
        self.items_rank = self.values.rank(method="first", ascending=False)
        return self.items_rank

    def _make_item_perc(self):
        """
        Returns
        -------
        Pandas.Series
            values rank percentege of total
            exp: 20 rank = 0.45 -> 20 best itens correspond to 45% of total results
        """
        self.total_items = self.items_rank.count()
        self.item_perc = self.items_rank / self.total_items
        return self.item_perc

    def _make_values_perc(self):
        """

        Returns
        -------
        Pandas.Series
            abc_column value divided by total values
        """
        self.total_values = self.values.sum()
        self.values_perc = self.values / self.total_values
        self.values_cum_perc = self.values_perc.cumsum()
        return self.values_cum_perc

    def _classify_abc(self, value):
        """
        Classify labels by value
        Parameters
        ----------
        value: float

        Returns
        -------
        str
            the label ('A', 'B' or 'C')
        """
        if value <= self.label_a:
            return "A"
        elif value <= self.label_a + self.label_b:
            return "B"
        else:
            return "C"

    def _make_labels(self):
        """return series of labels"""
        self.labels = self.item_perc.apply(self._classify_abc)
        return self.labels

    def abc(self):
        """performs abc analysis"""
        self._make_rank()
        self._make_item_perc()
        self._make_values_perc()
        self._make_labels()

        cols = self.abc_columns_names
        self.df[cols["rank"]] = self.items_rank
        self.df[cols["item_perc"]] = self.item_perc
        self.df[cols["values_perc"]] = self.values_cum_perc
        self.df[cols["label"]] = self.labels

        # self.make_summary()

    def add_prefix(self, prefix: str, connector: str = "_"):
        change_cols = {}
        for colum, colum_name in self.abc_columns_names.items():
            new_col = prefix + connector + colum_name
            change_cols[colum_name] = new_col
            self.abc_columns_names[colum] = new_col

        self.df.rename(columns=change_cols, inplace=True)

    def add_sufix(self, sufix: str, connector: str = "_"):
        change_cols = {}
        for colum, colum_name in self.abc_columns_names.items():
            new_col = colum_name + connector + sufix
            change_cols[colum_name] = new_col
            self.abc_columns_names[colum] = new_col

        self.df.rename(columns=change_cols, inplace=True)

    def _get_last_label(self, label: str):
        return self.df[self.df[self.abc_columns_names["label"]] == label].last_valid_index()

    def _get_item_rep(self, pos: int):
        return self.df.loc[pos, self.abc_columns_names["item_perc"]]

    def _get_value_rep(self, pos: int):
        return self.df.loc[pos, self.abc_columns_names["values_perc"]]

    def make_summary(self):
        last_a = self._get_last_label("A")
        last_b = self._get_last_label("B")
        last_c = self._get_last_label("C")

        table = {"Labels": ["A", "B", "C"], self.abc_columns_names["item_perc"]: [self._get_item_rep(last_a),
                                                                                  self._get_item_rep(last_b),
                                                                                  self._get_item_rep(last_c)],
                 self.abc_columns_names["values_perc"]: [self._get_value_rep(last_a),
                                                         self._get_value_rep(last_b),
                                                         self._get_value_rep(last_c)]}

        self.abc_summary_table = pd.DataFrame(table)
        return self.abc_summary_table