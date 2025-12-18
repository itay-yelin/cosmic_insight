# Design Rationale (1 page)

## Goals
- Keep algorithms simple, explainable, and efficient.
- Separate pure logic from IO/CLI for testability.
- Provide an easy path to scale up (vectorization, indexing, batching).

## Stage 1
- Smoothing: moving average (O(n)), stable, minimal parameters.
- Change detection: threshold on first difference after smoothing.

## Stage 2
- Match: per event, scan planets and compare user angle to target within tolerance.
- Score: linear mapping from delta to [0, 1].
- Scaling: index events by planet, or pre-filter relevant planets per user.

## Stage 3
- Pearson correlation across all column pairs.
- Select maximal absolute correlation; report p-value.
- Alternatives: Spearman, mutual information, robust correlation.

## Complexity
- Stage 1: O(n)
- Stage 2: O(E * P)
- Stage 3: O(Cm * Ca * N)

## Notes
- This skeleton focuses on clean structure; replace sample data with real datasets as needed.
