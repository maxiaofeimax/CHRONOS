
# CHRONOS: News Timeline Summarization

![](https://img.shields.io/badge/version-1.0.0-blue)[![Pytorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?e&logo=PyTorch&logoColor=white)](https://pytorch.org/)[![arxiv badge](https://img.shields.io/badge/arxiv-2501.00888-red)](https://arxiv.org/abs/)

📑 **Paper:** https://arxiv.org/abs/2501.00888

🌏 **Chinese Web Demo:** https://modelscope.cn/studios/vickywu1022/CHRONOS

<img src="/Users/weiqiwu/CHRONOS/img/demo.gif" alt="demo" style="zoom:50%;" />

## 🚀Overview

- We propose CHRONOS, a novel **retrieval-based** approach to Timeline Summarization (TLS) by **iteratively posing questions** about the topic and the retrieved documents to generate chronological summaries.
- We construct an **up-to-date dataset for open- domain TLS**, which surpasses existing public datasets in terms of both size and the duration of timelines.
- Experiments demonstrate that our method is effective on open-domain TLS and achieves comparable results with state-of-the-art methods of closed-domain TLS, with significant improvements in **efficiency and scalability**.

![overview](/Users/weiqiwu/CHRONOS/img/overview.png)



## ⚗️ OPEN-TLS Dataset

We release our Open-TLS dataset for open-domain Timeline Summarization. 

The target news query is presented in `news_keywords.py` and the ground truth timeline is presented in `data/open/{NEWS_KEYWORD}/timelines.jsonl` following the below format:

```json
[[Date|"YYY-MM-DDT00:00:00", [Events|"", "", ...]], ...]
```

Statistics of Open-TLS are:![open](img/open.png)



## 🛠 Running CHRONOS

### Step 1. Dependencies

```bash
pip install -r requirements.txt
```

### Step 2. Exampled Questions Generation

The second step is to construct a topic-questions example pool for datasets in `data/` .

```python
python question_exampler.py
```

Or, you can use our provided `data/question_examples.json`, which contains examples for the *crisis, T17 and Open-TLS* datasets.

### Step 3. Running CHRONOS

🔥 To be continued...



## 📝 Citation

```bigquery
@article{wu2025unfoldingheadlineiterativeselfquestioning,
      title={Unfolding the Headline: Iterative Self-Questioning for News Retrieval and Timeline Summarization}, 
      author={Weiqi Wu and Shen Huang and Yong Jiang and Pengjun Xie and Fei Huang and Hai Zhao},
      year={2025},
      eprint={2501.00888},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.00888}, 
}
```

