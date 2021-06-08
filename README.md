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
shannon_entropy_rate_estimate = npd_entropy.grassberger_estimate(quantised_series, 100) # returns the shannon entropy rate estimate, with a history of 100 data points
npd_entropy.npd_entropy(shannon_entropy_rate_estimate, 1) #returns the differential entropy rate estimate
```

## Contributors
* Andrew Feutrill

## References

[Feutrill, A., & Roughan, M. (2021). NPD Entropy: A Non-Parametric Differential Entropy Rate Estimator. arXiv preprint arXiv:2105.11580.](https://arxiv.org/abs/2105.11580)

Please cite this paper if you use this estimator.

## License
[MIT](https://choosealicense.com/licenses/mit/)
