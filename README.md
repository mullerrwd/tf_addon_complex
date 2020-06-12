# tf_addon_complex
A tf addon that aims to provide the necessary components for implementing complex-valued deep neural networks.


# Development
Create a `conda` environment:
```bash
conda create -n tf_addon_complex python=3.7
```

Activate the environment:
```bash
conda activate tf_addon_complex
```

Install `tf_addon_complex` in editable mode:
```bash
pip install -e .
```
This will setup `tf_addon_complex` and the required packages.


Errors when installing the package in editable mode may be due to versioning of pip. First try:
```bash
pip install pip --upgrade
```
