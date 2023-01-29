# paretoabc


## SUMMARY

## EXAMPLES

### ABC ANLS
```python
import pandas as pd  
from paretoabc import ParetoABC  
  
products = pd.read_csv("../data/office_co.csv", sep=';')  
  
pareto_anls = ParetoABC(products, abc_column="Revenue")  
  
pareto_anls.abc()  
pareto_anls.df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Prodct</th>
      <th>Revenue</th>
      <th>rank</th>
      <th>items representation</th>
      <th>values representation</th>
      <th>abc_labels</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Backup batteries</td>
      <td>50.0</td>
      <td>1.0</td>
      <td>0.025</td>
      <td>0.073314</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Webcams</td>
      <td>50.0</td>
      <td>2.0</td>
      <td>0.050</td>
      <td>0.146628</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Staplers</td>
      <td>50.0</td>
      <td>3.0</td>
      <td>0.075</td>
      <td>0.219941</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Business cards</td>
      <td>50.0</td>
      <td>4.0</td>
      <td>0.100</td>
      <td>0.293255</td>
      <td>A</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Shredders</td>
      <td>50.0</td>
      <td>5.0</td>
      <td>0.125</td>
      <td>0.366569</td>
      <td>A</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Scissors</td>
      <td>50.0</td>
      <td>6.0</td>
      <td>0.150</td>
      <td>0.439883</td>
      <td>A</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Post it notes</td>
      <td>50.0</td>
      <td>7.0</td>
      <td>0.175</td>
      <td>0.513196</td>
      <td>A</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Desk lamps</td>
      <td>50.0</td>
      <td>8.0</td>
      <td>0.200</td>
      <td>0.586510</td>
      <td>A</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Smartphones</td>
      <td>30.0</td>
      <td>9.0</td>
      <td>0.225</td>
      <td>0.630499</td>
      <td>B</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Laptops</td>
      <td>30.0</td>
      <td>10.0</td>
      <td>0.250</td>
      <td>0.674487</td>
      <td>B</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Paper</td>
      <td>20.0</td>
      <td>11.0</td>
      <td>0.275</td>
      <td>0.703812</td>
      <td>B</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Printer</td>
      <td>20.0</td>
      <td>12.0</td>
      <td>0.300</td>
      <td>0.733138</td>
      <td>B</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Glue</td>
      <td>20.0</td>
      <td>13.0</td>
      <td>0.325</td>
      <td>0.762463</td>
      <td>B</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ink and toner cartridges</td>
      <td>20.0</td>
      <td>14.0</td>
      <td>0.350</td>
      <td>0.791789</td>
      <td>B</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Correction fluid</td>
      <td>20.0</td>
      <td>15.0</td>
      <td>0.375</td>
      <td>0.821114</td>
      <td>B</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Highlighters</td>
      <td>20.0</td>
      <td>16.0</td>
      <td>0.400</td>
      <td>0.850440</td>
      <td>B</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Rulers</td>
      <td>20.0</td>
      <td>17.0</td>
      <td>0.425</td>
      <td>0.879765</td>
      <td>B</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Tablets</td>
      <td>15.0</td>
      <td>18.0</td>
      <td>0.450</td>
      <td>0.901760</td>
      <td>B</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Paper clips</td>
      <td>10.0</td>
      <td>19.0</td>
      <td>0.475</td>
      <td>0.916422</td>
      <td>B</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Computer chairs</td>
      <td>10.0</td>
      <td>20.0</td>
      <td>0.500</td>
      <td>0.931085</td>
      <td>B</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Notebooks</td>
      <td>7.0</td>
      <td>21.0</td>
      <td>0.525</td>
      <td>0.941349</td>
      <td>B</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Pens</td>
      <td>5.0</td>
      <td>22.0</td>
      <td>0.550</td>
      <td>0.948680</td>
      <td>B</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Surge protectors</td>
      <td>5.0</td>
      <td>23.0</td>
      <td>0.575</td>
      <td>0.956012</td>
      <td>B</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Keyboard</td>
      <td>5.0</td>
      <td>24.0</td>
      <td>0.600</td>
      <td>0.963343</td>
      <td>B</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Networking equipment</td>
      <td>5.0</td>
      <td>25.0</td>
      <td>0.625</td>
      <td>0.970674</td>
      <td>B</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Copy machines</td>
      <td>3.0</td>
      <td>26.0</td>
      <td>0.650</td>
      <td>0.975073</td>
      <td>B</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Folders</td>
      <td>3.0</td>
      <td>27.0</td>
      <td>0.675</td>
      <td>0.979472</td>
      <td>B</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Binders</td>
      <td>2.0</td>
      <td>28.0</td>
      <td>0.700</td>
      <td>0.982405</td>
      <td>B</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Desk organizers</td>
      <td>1.0</td>
      <td>29.0</td>
      <td>0.725</td>
      <td>0.983871</td>
      <td>C</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Envelopes</td>
      <td>1.0</td>
      <td>30.0</td>
      <td>0.750</td>
      <td>0.985337</td>
      <td>C</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Labels</td>
      <td>1.0</td>
      <td>31.0</td>
      <td>0.775</td>
      <td>0.986804</td>
      <td>C</td>
    </tr>
    <tr>
      <th>31</th>
      <td>File cabinets</td>
      <td>1.0</td>
      <td>32.0</td>
      <td>0.800</td>
      <td>0.988270</td>
      <td>C</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Mouse</td>
      <td>1.0</td>
      <td>33.0</td>
      <td>0.825</td>
      <td>0.989736</td>
      <td>C</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Headphones</td>
      <td>1.0</td>
      <td>34.0</td>
      <td>0.850</td>
      <td>0.991202</td>
      <td>C</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Speakers</td>
      <td>1.0</td>
      <td>35.0</td>
      <td>0.875</td>
      <td>0.992669</td>
      <td>C</td>
    </tr>
    <tr>
      <th>35</th>
      <td>USB drives</td>
      <td>1.0</td>
      <td>36.0</td>
      <td>0.900</td>
      <td>0.994135</td>
      <td>C</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Whiteboards</td>
      <td>1.0</td>
      <td>37.0</td>
      <td>0.925</td>
      <td>0.995601</td>
      <td>C</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Tapes</td>
      <td>1.0</td>
      <td>38.0</td>
      <td>0.950</td>
      <td>0.997067</td>
      <td>C</td>
    </tr>
    <tr>
      <th>38</th>
      <td>External hard drives</td>
      <td>1.0</td>
      <td>39.0</td>
      <td>0.975</td>
      <td>0.998534</td>
      <td>C</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Calculators</td>
      <td>1.0</td>
      <td>40.0</td>
      <td>1.000</td>
      <td>1.000000</td>
      <td>C</td>
    </tr>
  </tbody>
</table>


```python
summary = pareto_anls.make_summary()  
summary
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Labels</th>
      <th>items representation</th>
      <th>values representation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0.2</td>
      <td>0.586510</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>0.7</td>
      <td>0.982405</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>1.0</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>


### ABC CURVE PLOT