# Caltech 101

<div align="center">

[![Discord](https://img.shields.io/badge/Discord-7289DA?logo=discord&logoColor=white)](https://discord.gg/fiftyone-community)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-purple?style=flat&logo=huggingface)](https://huggingface.co/Voxel51)
[![Voxel51 Blog](https://img.shields.io/badge/Voxel51_Blog-ff6d04?style=flat)](https://voxel51.com/blog)
[![Newsletter](https://img.shields.io/badge/Newsletter-BE5B25?logo=mail.ru&logoColor=white)](https://share.hsforms.com/1zpJ60ggaQtOoVeBqIZdaaA2ykyk)
[![LinkedIn](https://img.shields.io/badge/In-white?style=flat&label=Linked&labelColor=blue)](https://www.linkedin.com/company/voxel51)
[![Twitter](https://img.shields.io/badge/Twitter-000000?logo=x&logoColor=white)](https://x.com/voxel51)
[![Medium](https://img.shields.io/badge/Medium-12100E?logo=medium&logoColor=white)](https://medium.com/voxel51)

</div>

The Caltech-101 dataset.

The dataset consists of pictures of objects belonging to 101 classes, plus one
background clutter class (``BACKGROUND_Google``). Each image is labelled with a
single object.

Each class contains roughly 40 to 800 images, totalling around 9,000 images.
Images are of variable sizes, with typical edge lengths of 200-300 pixels.
This version contains image-level labels only.

## Details

-   Dataset name: ``voxel51/caltech101``
-   Dataset source: https://data.caltech.edu/records/mzrjq-6wc02
-   Dataset size: 150 MB
-   Number of images: 9,145
-   Tags: ``image, classification``

## Example usage

```py
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("https://github.com/voxel51/caltech101")

session = fo.launch_app(dataset)
```
