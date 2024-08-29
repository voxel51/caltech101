"""
Caltech 101 dataset.

| Copyright 2017-2024, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""
import logging
import os

import eta.core.utils as etau
import eta.core.web as etaw

import fiftyone as fo
import fiftyone.types as fot
import fiftyone.utils.data as foud


logger = logging.getLogger(__name__)


def download_and_prepare(dataset_dir):
    """Downloads the dataset prepares it for loading into FiftyOne.

    Args:
        dataset_dir: the directory in which to construct the dataset

    Returns:
        a tuple of

        -   ``dataset_type``: the ``fiftyone.types.Dataset`` type that the
            dataset is stored in locally
        -   ``num_samples``: the total number of downloaded samples
        -   ``classes``: the list of classes in the dataset
    """
    scratch_dir = os.path.join(dataset_dir, "tmp-download")

    # The source URL for the data is
    # https://data.caltech.edu/records/mzrjq-6wc02/files/caltech-101.zip?download=1
    # but this now redirects to the Google Drive file below
    _download_and_extract_archive(
        "137RyRjvTBkBiIfeYBNZBtViDHQ6_Ewsp",
        "101_ObjectCategories.tar.gz",
        "101_ObjectCategories",
        dataset_dir,
        scratch_dir,
    )

    etau.delete_dir(scratch_dir)

    # The data is stored on disk in
    dataset_type = fot.ImageClassificationDirectoryTree
    importer = foud.ImageClassificationDirectoryTreeImporter
    num_samples = importer._get_num_samples(dataset_dir)
    classes = importer._get_classes(dataset_dir)

    return dataset_type, num_samples, classes


def _download_and_extract_archive(
    fid, archive_name, dir_in_archive, dataset_dir, scratch_dir
):
    archive_path = os.path.join(scratch_dir, archive_name)

    logger.info("Downloading dataset...")
    etaw.download_google_drive_file(fid, path=archive_path)

    logger.info("Extracting archive...")
    etau.extract_archive(archive_path)
    _move_dir(os.path.join(scratch_dir, dir_in_archive), dataset_dir)