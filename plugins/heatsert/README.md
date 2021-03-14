# Sample Plugin

Generates a hole that accepts a heatsert. Heatserts are often used in 3D printed parts. Standard M3, M4, M5 and M6 values included. TODO: list mfr part numbers of my heatserts

## Installation

```
pip install -e "git+https://github.com/CadQuery/cadquery-plugins.git#egg=heatsert&subdirectory=plugins/heatsert"
```

## Dependencies

This plugin has no dependencies other than the cadquery library.

## Usage

To use this plugin after it has been installed, import it and then call its `register` function to patch its function(s) into the `cadquery.Workplane` class.

```python
import cadquery as cq
from sampleplugin import sampleplugin

# Adds the make_cubes function to cadquery.Workplane
sampleplugin.register()

result = (cq.Workplane().rect(50, 50, forConstruction=True)
                        .vertices()
                        .make_cubes(10))
```
