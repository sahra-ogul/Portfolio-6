def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations of the fair sharing algorithm.

    In each iteration the highest value in `values` gives a fraction (share)
    to both the left and right neighbor.
    The leftmost field is considered the neighbor of the rightmost field.

    Examples:
    fair_sharer([0, 1000, 800, 0], 1) -> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) -> [100, 890, 720, 90]

    Args:
        values: list or numpy array of numeric values
        num_iterations: number of iterations
        share: fraction to distribute to each neighbor

    Returns:
        New list with updated values
    """
    values = list(values)  # defensive copy
    n = len(values)

    for _ in range(num_iterations):
        max_index = values.index(max(values))
        amount = values[max_index] * share

        left = (max_index - 1) % n
        right = (max_index + 1) % n

        values[max_index] -= 2 * amount
        values[left] += amount
        values[right] += amount

    return values