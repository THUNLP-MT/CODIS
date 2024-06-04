# <img src="./static/images/logo.png" alt="logo" width="3%">CODIS: Benchmarking Context-Dependent Visual Comprehension for Multimodal Large Language Models

[**🌐 Homepage**](https://thunlp-mt.github.io/CODIS) | [**📖 arXiv**](https://arxiv.org/abs/2402.13607) | [**🤗 Dataset**](https://huggingface.co/datasets/CODIS/CODIS)

This repo contains the dataset and evaluation code for paper [CODIS: Benchmarking Context-Dependent Visual Comprehension for Multimodal Large Language Models](https://arxiv.org/abs/2402.13607).

## Introduction

In certain situations, images need to be interpreted within a broader context. We introduce a new benchmark, named as **CODIS** (**CO**ntext-**D**ependent **I**mage di**S**ambiguation), designed to assess the ability of models to use context provided in free-form text to enhance visual comprehension.

- Each image in CODIS contains inherent ambiguity that can only be resolved with additional context.
- The questions are deliberately designed to highlight these ambiguities, requiring external context for accurate interpretation.
- For every image-question pair, we provide two contexts in a free-form text format.

![taxonomy](./static/images/taxonomy.jpg)

## Evaluation

Please organize outputs of your models as follows.

```
[
    {
        "id": "000",
        "output": {
            "output_1": "[YOUR OUTPUT TO CASE 000 GIVEN CONTEXT_1 HERE]",
            "output_2": "[YOUR OUTPUT TO CASE 000 GIVEN CONTEXT_2 HERE]"
        }
    },
    {
        "id": "001",
        "output": {
            "output_1": "[YOUR OUTPUT TO CASE 001 GIVEN CONTEXT_1 HERE]",
            "output_2": "[YOUR OUTPUT TO CASE 001 GIVEN CONTEXT_2 HERE]"
        }
    },
    ...
]
```

A complete example of output file can be found at `data/output_example.json`.

For evaluation, please run the following command to calculate Acc_p and Acc_q.

```bash
cd data

# your OpenAI API key
export OPENAI_API_KEY=[YOUR OPENAI API KEY HERE]
# path to "data.json"
export ANSWER_PATH=./data.json
# path to your output file
export OUTPUT_PATH=./output_example.json

python eval.py
```

## Leaderboard

We report Acc_p scores based on human and GPT-4 evaluation. Models score only if their answers to a pair of queries are both correct. 

### Human Evaluation

| Model          | Loc & Ori     | Temporal      | Cultural      | Attributes    | Relationships | Average       |
|----------------|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
Human            | 85.2          | 90.9          | 72.8          | 87.2          | 89.6          | 86.2          |
GPT-4V           | 33.3          | 28.4          | 25.5          | 26.7          | 51.9          | 32.3          |
Gemini           | 21.4          | 29.5          | 21.3          | 24.0          | 34.6          | 26.1          |
LLaVA-1.5-13B    | 6.0           | 4.2           | 10.6          | 14.7          | 13.5          | 9.1           |
BLIP-2-11B       | 6.0           | 8.4           | 4.3           | 6.7           | 11.5          | 7.4           |
InstructBLIP-13B | 6.0           | 2.1           | 4.3           | 4.0           | 7.7           | 4.5           |
mPLUG-Owl-2-7B   | 13.1          | 9.5           | 6.4           | 12.0          | 19.2          | 11.9          |
MiniGPT4-7B      | 10.7          | 3.2           | 0.0           | 12.0          | 13.5          | 7.9           |
LLaVA-1.5-7B     | 11.9          | 5.3           | 4.3           | 9.3           | 7.7           | 7.9           |
InstructBLIP-7B  | 1.2           | 7.4           | 0.0           | 4.0           | 11.5          | 4.8           |
Otter-7B         | 2.4           | 5.3           | 4.3           | 0.0           | 5.8           | 3.4           |
LLaVA-7B         | 2.4           | 6.3           | 0.0           | 1.3           | 5.8           | 3.4           |
Qwen-VL-Chat     | 3.6           | 3.2           | 0.0           | 1.3           | 9.6           | 3.4           |
OpenFlamingo-7B  | 2.4           | 2.1           | 0.0           | 5.3           | 5.8           | 3.1           |
BLIP-2-6.7B      | 0.0           | 1.1           | 2.1           | 2.7           | 7.7           | 2.3           |

### GPT-4 Evaluation

| Model          | Loc & Ori     | Temporal      | Cultural      | Attributes    | Relationships | Average       |
|----------------|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
GPT-4V           | 33.3          | 28.4          | 21.3          | 25.3          | 50.0          | 31.2          |
Gemini           | 20.2          | 27.4          | 21.3          | 22.7          | 30.8          | 24.4          |
LLaVA-1.5-13B    | 6.0           | 3.2           | 12.8          | 13.3          | 11.5          | 8.5           |
BLIP-2-11B       | 6.0           | 10.5          | 4.3           | 6.7           | 11.5          | 8.0           |
InstructBLIP-13B | 6.0           | 2.1           | 6.4           | 4.0           | 5.8           | 4.5           |
mPLUG-Owl-2-7B   | 13.1          | 9.5           | 4.3           | 9.3           | 11.5          | 9.9           |
MiniGPT4-7B      | 10.7          | 4.2           | 0.0           | 8.0           | 9.6           | 6.8           |
LLaVA-1.5-7B     | 8.3           | 1.1           | 2.1           | 9.3           | 7.7           | 5.7           |
InstructBLIP-7B  | 1.2           | 5.3           | 0.0           | 4.0           | 11.5          | 4.2           |
Otter-7B         | 2.4           | 3.2           | 0.0           | 1.3           | 5.8           | 2.5           |
LLaVA-7B         | 2.4           | 4.2           | 0.0           | 2.7           | 1.9           | 2.5           |
Qwen-VL-Chat     | 4.8           | 3.2           | 0.0           | 1.3           | 7.7           | 3.4           |
OpenFlamingo-7B  | 2.4           | 2.1           | 0.0           | 5.3           | 5.8           | 3.1           |
BLIP-2-6.7B      | 0.0           | 1.1           | 4.3           | 4.0           | 5.8           | 2.5           |

## Citation

```bibtex
@article{luo2024codis,
  title={CODIS: Benchmarking Context-Dependent Visual Comprehension for Multimodal Large Language Models},
  author={Fuwen Luo and Chi Chen and Zihao Wan and Zhaolu Kang and Qidong Yan and Yingjie Li and Xiaolong Wang and Siyu Wang and Ziyue Wang and Xiaoyue Mi and Peng Li and Ning Ma and Maosong Sun and Yang Liu},
  journal={arXiv preprint arXiv:2402.13607},
  year={2024}
}
```
