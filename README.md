# npd_entropy

An implementation of a non-parametric differential entropy rate estimator, developed by Andrew Feutrill and Matthew Roughan. This technique quantises data from a continuous-valued process, then utilises Shannon entropy rate estimators for a differential entropy rate estimate.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install npd_entropy.

```bash
pip install npd_entropy
```

## Usage

```python
import npd_entropy

quantised_series = npd_entropy.quantise_series(series, 1) # returns a quantised version of the series, with bin size of 1
npd_entropy.grassberger_estimate(quantised_series, 100) # returns the differential entropy rte estimate, with a history of 100 data points
```

## Contributors
* Andrew Feutrill

## License
[MIT](https://choosealicense.com/licenses/mit/)
