# Chunking experiment (pdf1.pdf, 8 pages)

| chunk_size / overlap | chunks | Q1 top score | Q1 top-3 pages |
|---|---|---|---|
| 200 / 40 | 113 | 0.672 | 1, 3, 5 |
| 800 / 150 | 29 | 0.643 | 1, 1, 3 |
| 1500 / 250 | 15 | 0.596 | 1, 2, 8 |

## Observations
- 1500-char chunks returned a References chunk (page 8) in the top 3.
- Scores are not comparable across configs as a quality measure.
- Q2 ("one line conclusion") is a summarization question, retrieval alone cannot answer it.

## Decision
Default: 800 / 150 for now. Revisit with Recall@k on Day 5.