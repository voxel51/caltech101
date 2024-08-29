# Caltech 101

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
