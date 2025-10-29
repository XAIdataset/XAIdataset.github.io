
# Saliency-Bench: A Comprehensive Benchmark for Evaluating Visual Explanations

[![Website](https://img.shields.io/badge/Website-XAIdataset.github.io-blue)](https://xaidataset.github.io/)  
[![Paper](https://img.shields.io/badge/Paper-arXiv%3A2310.08537-red)](https://arxiv.org/abs/2310.08537)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🔍 Overview

**Saliency-Bench** is a large-scale, standardized benchmark for evaluating **visual explanation** (saliency) methods. It provides carefully curated datasets across multiple domains and unified evaluation protocols, enabling systematic and fair comparisons between methods.

This benchmark addresses the lack of rigorous evaluation frameworks for assessing the **faithfulness** and **alignment** of saliency methods, supporting both academic research and real-world applications in explainable AI (XAI).

## ✨ Features

- 📊 **Unified Evaluation Framework**: Standardized metrics for faithfulness and alignment evaluation.  
- 🖼️ **8 Diverse Datasets**: Covering scene recognition, tumor detection, prohibited item detection, and object recognition.  
- 🛠️ **Easy-to-Use API**: Simple APIs for dataset loading and evaluation.  
- 📚 **Comprehensive Documentation**: Quick start guides, tutorials, and dataset details.

## 📂 Datasets

| Dataset            | Task Type                    | # Samples | Annotation Type        | Format        | Balanced | Counterfactuals |
|--------------------|------------------------------|-----------|------------------------|---------------|----------|-----------------|
| Gender-XAI         | Gender Classification        | 5,000     | Human-annotated        | Pixel-wise    | Yes      | Yes             |
| Scene-XAI          | Scene Recognition            | 5,000     | Human-annotated        | Pixel-wise    | Yes      | Yes             |
| Glasses-XAI        | Glasses Detection            | 2,614     | Human-annotated        | Pixel-wise    | Yes      | No              |
| Prohibited-XAI     | Prohibited Item Detection    | 17,654    | Human-annotated        | Bounding Box  | Yes      | No              |
| Nodule-XAI         | Nodule Detection (Medical)   | 5,250     | Human-annotated        | Pixel-wise    | Yes      | No              |
| Tumor-XAI          | Tumor Detection (Medical)    | 361       | Human-annotated        | Pixel-wise    | No       | No              |
| Cat&Dog-XAI        | Cat vs Dog Classification    | 7,390     | Foreground Extraction  | Pixel-wise    | No       | No              |
| Object-XAI         | Multi-class Object Recognition | 4,318   | Foreground Extraction  | Pixel-wise    | No       | No              |


More details are available on our [Dataset page](https://xaidataset.github.io/dataset/).

## 📢 Licensing and Attribution Notice

All datasets in **Saliency-Bench** are either:
- Derived from publicly available sources under academic/research licenses, or
- Built upon existing datasets by adding human-annotated explanations or saliency labels.

To comply with original dataset licenses:
- **We do not redistribute any raw image data**. Users must obtain raw data from the official sources.
- We only provide annotation files, split lists, and mapping scripts that support explanation benchmarking.
- Users must comply with both the original data licenses and the Saliency-Bench license for our annotations (MIT).

Please refer to each dataset's documentation for original sources and license details.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/XAIdataset/XAIdataset.github.io.git
cd XAIdataset.github.io
```

Install the dependencies:

```bash
Please refer to http://xaidataset.github.io/quick_start/
```

## 🛠️ Quick Start

```python
from xaibenchmark import load_dataset, evaluate_method

# Load a dataset
dataset = load_dataset('Gender-XAI')

# Evaluate a saliency method
results = evaluate_method(method='GradCAM', dataset=dataset)

# Print evaluation results
print(results)
```

For more examples, refer to the [Quickstart Notebook](https://github.com/XAIdataset/XAIdataset.github.io/blob/main/quickstart.ipynb).

## 🤝 Contributing

We welcome contributions!

To contribute:

1. Fork the repository.  
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -am "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request.

Please also feel free to open [Issues](https://github.com/XAIdataset/XAIdataset.github.io/issues) for discussions, suggestions, or bug reports.

## 📄 Citation

If you use Saliency-Bench in your research, please cite:

> Zhang, Yifei, et al. "Saliency-Bench: A Comprehensive Benchmark for Evaluating Visual Explanations." arXiv preprint arXiv:2310.08537.

BibTeX:

```bibtex
@misc{zhang2025saliencybenchcomprehensivebenchmarkevaluating,
  title        = {Saliency-Bench: A Comprehensive Benchmark for Evaluating Visual Explanations},
  author       = {Yifei Zhang and James Song and Siyi Gu and Tianxu Jiang and Bo Pan and Guangji Bai and Liang Zhao},
  year         = {2025},
  eprint       = {2310.08537},
  archivePrefix= {arXiv},
  primaryClass = {cs.CV},
  url          = {https://arxiv.org/abs/2310.08537},
}
```

## 📬 Contact

For any questions or feedback:

- Open an [Issue](https://github.com/XAIdataset/XAIdataset.github.io/issues)  
- Email: yzh3443@emory.edu

## 📝 License

This project is licensed under the [MIT License](LICENSE).
