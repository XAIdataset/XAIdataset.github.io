---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: "XAI Benchmarking"
excerpt: "This is the description of the project"
layout: default
description: "XAI benchmarking is a collection of 8 image datasets that covers a variety of fields and aims to provide standardized benchmarks for visual explanation of Explainable AI (XAI). 
You can download these datasets from this website, and we also provide a user-friendly API with a quick start guide. 
If you want to learn more, please consider read our paper on Arxiv. "
---

## Introduction
The rise of deep learning algorithms has led to significant advancements in computer vision tasks, 
but their "black box" nature has raised concerns regarding interpretability. 
Explainable AI (XAI) has emerged as a critical area of research aiming to open this "black box", 
and shed light on the decision-making process of AI models. 
Visual explanations, as a subset of Explainable Artificial Intelligence (XAI), 
provide intuitive insights into the decision-making processes of AI models handling visual data by highlighting influential areas in an input image. 
Despite extensive research conducted on visual explanations, 
the availability of corresponding real-world datasets with ground truth explanations is scarce in the context of image data. 
To bridge this gap, we introduce an XAI Benchmark comprising a datasets collection from diverse topics 
that provide both class labels and corresponding explanation annotations for images. 
We have processed data from diverse domains to align with our unified visual explanation framework. 
We introduce a comprehensive Visual Explanation pipeline, 
which integrates data loading, preprocessing, experimental setup, and model evaluation processes. 
This structure enables researchers to conduct fair comparisons of various visual explanation techniques. 
In addition, we provide a comprehensive review of over 10 evaluation methods for visual explanation to assist researchers in effectively utilizing our dataset collection. 
To further assess the performance of existing visual explanation methods, we conduct experiments on selected datasets using various evaluation metrics. 
We envision this benchmark could facilitate the advancement of visual explanation models.

![Examples]("/xaibenchmarking/images/example.png")
Examples of objective classification dataset showing the original images (row (a)), the visual explanation outputs obtained from GradCAM based on trained RESNET-18 classifier (row (b)), and the corresponding ground truth explanation annotations (row (c)).


## Citation
Please consider cite us: 

> Zhang, Yifei, et al. "XAI Benchmark for Visual Explanation." arXiv preprint arXiv:2310.08537 (2023).

**BibTex**: 
```
@misc{zhang2023xai,
      title={XAI Benchmark for Visual Explanation}, 
      author={Yifei Zhang and Siyi Gu and James Song and Bo Pan and Liang Zhao},
      year={2023},
      eprint={2310.08537},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```