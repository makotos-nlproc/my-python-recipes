# Embeddings

- one-hot encoding
  - 単語を次元数＝ボキャブラリ数の01のベクトルで表現
  - ベクトル間の演算に意味を持たせられない
  - 次元数大きくなる、ボキャブラリの追加コスト大きい
- Word Embeddings / Distributed Representation
  - 単語を（ボキャブラリ数に関係ない）低次元の実数値ベクトルで表現
  - ベクトル間の演算に意味を込められる（類似度・和と差）
  - 