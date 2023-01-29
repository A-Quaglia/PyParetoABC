import pandas as pd
from paretoabc import ParetoABC

products = pd.read_csv("../data/office_co.csv", sep=';')

pareto_anls = ParetoABC(products, abc_column="Revenue")

pareto_anls.abc()
print(pareto_anls.df)

summary = pareto_anls.make_summary()
print(summary)




