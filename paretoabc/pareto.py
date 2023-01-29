import pandas as pd


class CurveABC:

      def __init__(self, df: pd.DataFrame, abc_column: str, label_a: float = 0.2,
                 label_b: float = 0.5, label_c: float = 0.3):

        self.df = df.copy()
        self.abc_column = abc_column

        self._order_by_values()

        self.values = self.df[self.abc_column]

        self.total_items = 0
        self.total_values = 0
        self.items_rank = pd.Series([0])
        self.item_porc = pd.Series([0])
        self.values_porc = pd.Series([0])
        self.values_cum_porc = pd.Series([0])
        self.labels = pd.Series([0])

        self.label_a = label_a
        self.label_b = label_b
        self.label_c = label_c

        self.abc_columns_names = {"rank": "rank", "item_porc": "items representation",
                                  "values_porc": "values representation", "label": 'abc_labels'}

        self.abc_summary_table = pd.DataFrame({})

    def _order_by_values(self):
        self.df.sort_values(by=self.abc_column, inplace=True, ascending=False)
        self.df.index = range(self.df.shape[0])

    def _make_rank(self, method="first", ascending=False):
        self.items_rank = self.values.rank(method=method, ascending=ascending)
        return self.items_rank

    def _make_item_porc(self):
        self.total_items = self.items_rank.count()
        self.item_porc = self.items_rank / self.total_items
        return self.item_porc

    def _make_values_porc(self):
        self.total_values = self.values.sum()
        self.values_porc = self.values / self.total_values
        self.values_cum_porc = self.values_porc.cumsum()
        return self.values_cum_porc

    def _classify_abc(self, value):
        if value <= self.label_a:
            return "A"
        elif value <= self.label_a + self.label_b:
            return "B"
        else:
            return "C"

    def _make_labels(self):
        self.labels = self.item_porc.apply(self._classify_abc)
        return self.labels

    def abc(self, automatic=True):
        if automatic:
            self._make_rank()
            self._make_item_porc()
            self._make_values_porc()
            self._make_labels()

        cols = self.abc_columns_names
        self.df[cols["rank"]] = self.items_rank
        self.df[cols["item_porc"]] = self.item_porc
        self.df[cols["values_porc"]] = self.values_cum_porc
        self.df[cols["label"]] = self.labels

        self.make_summary()

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
        return self.df.loc[pos, self.abc_columns_names["item_porc"]]

    def _get_value_rep(self, pos: int):
        return self.df.loc[pos, self.abc_columns_names["values_porc"]]

    def make_summary(self):
        last_a = self._get_last_label("A")
        last_b = self._get_last_label("B")
        last_c = self._get_last_label("C")

        table = {"Labels": ["A", "B", "C"], self.abc_columns_names["item_porc"]: [],
                 self.abc_columns_names["values_porc"]: []}

        table[self.abc_columns_names["item_porc"]] = [self._get_item_rep(last_a),
                                                      self._get_item_rep(last_b),
                                                      self._get_item_rep(last_c)]

        table[self.abc_columns_names["values_porc"]] = [self._get_value_rep(last_a),
                                                        self._get_value_rep(last_b),
                                                        self._get_value_rep(last_c)]

        self.abc_summary_table = pd.DataFrame(table)
        return self.abc_summary_table