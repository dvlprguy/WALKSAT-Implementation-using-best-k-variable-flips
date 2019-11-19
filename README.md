#   Modified WALKSAT Algorithm

This code implements WALKSAT algorithm for solving SAT problems.
Instead of just using random assignments, it uses uniform probabilty to flip least false-clause-creating "v" variables in the model.
I have uploaded both jupyter notebook and my python script separately.
The code was run on 117 different inputs taken from sources like: https://satcompetition.org, https://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html
The hyperparameters maxv, maxit, pflip can be easily changed by the user.
pflip has been set to 0.5 to maintain uniform probability.

##  Library Requirements

Only matplotlib is required as a dependency.

```python
pip install matplotlib
```

##  Dataset

The dataset is in the 'Benchmarks/findata' folder.
It contains 117 files containing SAT problems in DIMAC format.

## Results

The final plots for meantime(number of iterations per input) and mnratio( number of clauses/ number of variables) are uploaded.
These plots are in accordance with the plots given in the textbook showing that large number of iterations are required for cnfs having mnratio around 4.


