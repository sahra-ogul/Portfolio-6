# Portfolio-6
# Fairsharer


The goal of this project is to implement a simple redistribution algorithm,
write unit tests for it, and set up Continuous Integration using GitHub Actions.

## What does this project do?
The core of this project is the function `fair_sharer`.  
It simulates a redistribution process where, in each iteration, the highest
value shares a fixed fraction of itself with its direct neighbors.

The values are arranged in a **circular structure**, meaning the first and
last elements are considered neighbors as well.

---

## The `fair_sharer` function

```python
fair_sharer(values, num_iterations, share=0.1)
