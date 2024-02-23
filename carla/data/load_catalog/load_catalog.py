# Software Name : carla_croco_vcnet
# Version: 1.0
# SPDX-FileCopyrightText: Copyright (c) 2024 Orange
# SPDX-License-Identifier: MIT
#
# This software is distributed under the MIT License,
# the text of which is available at https://spdx.org/licenses/MIT.html
# or see the "license.txt" file for more details.


import os
from typing import List

import yaml

from carla import lib_path


def load(filename: str, dataset: str, keys: List[str]):
    with open(os.path.join(lib_path, filename), "r") as f:
        catalog = yaml.safe_load(f)

    if dataset not in catalog:
        raise KeyError("Dataset not in catalog.")

    for key in keys:
        if key not in catalog[dataset].keys():
            raise KeyError("Important key {} is not in Catalog".format(key))
        if catalog[dataset][key] is None:
            catalog[dataset][key] = []

    return catalog[dataset]
