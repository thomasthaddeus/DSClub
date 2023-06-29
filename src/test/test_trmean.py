load_file_in_context("script.py")

try:
  # Attempt to access a variable identifier:
  trmean_budget

except NameError:
  fail_tests("Did you define a variable called `trmean_budget`?")

try:
  trmean_budget_sol = trim_mean(movies.production_budget, proportiontocut=0.2)

except NameError:
  fail_tests("Did you import `trim_mean()` from the `scipy.stats` module to calculate the trimmed mean?")

if trmean_budget != trmean_budget_sol:
  fail_tests("Did you use `trim_mean()` to find the mean for `production_budget` after trimming the most extreme 20% of data points?")

pass_tests()
