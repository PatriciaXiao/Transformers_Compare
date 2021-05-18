# Transformers

## Related Papers

### Basic Transformer Models
* [Transformer](https://arxiv.org/abs/1706.03762)
* [Transformer-XL](https://arxiv.org/abs/1901.02860)

### Encoder-Only
* [BERT](https://arxiv.org/abs/1810.04805)
* [XLNet](https://arxiv.org/abs/1906.08237)

### Decoder-Only
GPT / GPT-1 is using the same objective as [ELMo](https://arxiv.org/abs/1802.05365) in pre-training phase. (language model, LM; single directed)
* [GPT-1](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)
* [GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
* [GPT-3](https://arxiv.org/abs/2005.14165)

### Encoder-Decoder Models
* [BART](https://arxiv.org/abs/1910.13461)
* [T5](https://arxiv.org/pdf/1910.10683.pdf)

### Paper for Further Discussions
* [It's Not Just Size That Matters](https://arxiv.org/abs/2009.07118)
* [Pre-trained methods could be applied to other structures](https://arxiv.org/abs/2105.03322)
* [BERT as Markov Random Field](https://arxiv.org/abs/1902.04094):  it learns a distribution over sentences; we can use BERT not only as parameter initialization for finetuning, but as a generative model of sentences to either score a sentence or sample a sentence.

## Compare

### A brief history

* Simple RNN
  * simply Seq2Seq, the downside is forgetting as the sequence grows long
* Contextualize RNN
  * introducing context, or encoded source sentence --- usually the average hidden state or the final hidden state of the encoder; avoid forgetting, but lack dynamic
* Contextualized RNN with attention / soft align
  * [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473.pdf)
* Transformer(2017)

### Compare their costs

I found the following figure from [here](https://samcash.substack.com/p/-laymans-guide-to-language-models).
![Compare Cost](./compare_cost.png)

| Model Name | # Parameters | Memory Cost (≥) | Training Set  | Pre-training ($) |
|------------|--------------|-----------------|---------------|------------------|
| GPT        | 117 million  |                 | 5.75 gigabyte |                  |
| GPT-2      | 1.54 billion | 24 gigabyte     | 40 gigabyte   | 50 thousand      |
| GPT-3      | 175 billion  | 350 gigabyte    | 700 gigabyte  | 12 million       |
| BERT-large | 340 million  | 16 gigabyte     |               | 7 thousand       |
| BART-large | 406 million  | 12 gigabyte     |               |                  |

References:
* [A list of pretrained models in library](https://huggingface.co/transformers/pretrained_models.html)
* [BookCorpus](https://huggingface.co/datasets/bookcorpus)
* [An intro blog to GPT-3](https://samcash.substack.com/p/-laymans-guide-to-language-models)
* [BERT memory analysis](https://krishansubudhi.github.io/deeplearning/2019/09/20/BertMemoryAnalysis.html)
* [GPT-3 training cost](https://towardsdatascience.com/the-future-of-ai-is-decentralized-848d4931a29a#:~:text=Training%20GPT%2D3%20reportedly%20cost,way%20to%20train%20a%20model%3F&text=Artificial%20intelligence%20is%20a%20commodity,Google%2C%20Baidu%2C%20and%20Facebook%C2%B2.)
* [BERT training cost](https://dl.acm.org/doi/fullHtml/10.1145/3381831#:~:text=BERT%2Dlarge%20was%20trained%20on,an%20estimated%20cost%20of%20%2425%2C000.)
* [BART training discussion](https://github.com/pytorch/fairseq/issues/2731)
* [BERT pretraining dataset](https://d2l.ai/chapter_natural-language-processing-pretraining/bert-dataset.html)
* [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models (a paper on optimizing the memory)](https://arxiv.org/pdf/1910.02054.pdf)
* [GPT summary blog](https://medium.com/walmartglobaltech/the-journey-of-open-ai-gpt-models-32d95b7b7fb2)
* [A transformers summary blog](https://www.topbots.com/generalized-language-models-bert-openai-gpt2/)
* [Discussion of encoder-only v.s. decoder-only](https://datascience.stackexchange.com/questions/87637/what-is-the-difference-between-gpt-blocks-and-bert-blocks), [another discussion on similar topic](https://stats.stackexchange.com/questions/515152/deciding-between-decoder-only-or-encoder-only-transformers-bert-gpt)
* [XLNet the permutation trick](https://medium.com/saarthi-ai/xlnet-the-permutation-language-model-b30f5b4e3c1e)
* Some Chinese blogs (high-quality, but not in English): 
  * [BERT could also be used for few-shot learning](https://kexue.fm/archives/7764/comment-page-1)
  * [A faster and better MLM](https://kexue.fm/archives/7661) ([paper on ArXiV](https://arxiv.org/abs/2004.08097))
  * [Transformers benefit from Masks, plus the idea of using BERT as Seq2Seq model, etc.](https://kexue.fm/archives/6933)
  * [History of Transformer: emerged from Machine Translation](https://zhuanlan.zhihu.com/p/104393915)

### Other important differences

#### Encoder v.s. Decoder

Encoder-only v.s. Decoder-only
* An encoder-only Transformer, such as **BERT**, each position in the input corresponds to the output at the same position (or [MASK] if masked).
* A decoder-only Transformer, such as **GPT** models, is meant for autoregressive inference. In other words, the tokens in the input are shifted one position to the right with respect to the output. If the output is ```[hello, world, are, you, okay </end>]```, the input is ```[<start>, hello, world, are, you, okay </end>]```.
* At inference time, BERT generates all output at once; GPT iteratively generate one token at a time.

#### Pre-Training Masking Methodologies

* Traditional, Single-directed (unaware of the "future", aware of the "past"): LSTM, ELMo, GPT, GPT-2, GPT-3.
* Masked Language Model (hide some tokens in the middle, using information fromtwo directions at the same time): BERT
* Permutation Language Model (avoiding the [MASK] token, not predicting the tokens in sequential order, predicts in some random order): XLNet
* etc.

