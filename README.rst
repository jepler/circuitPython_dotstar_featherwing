
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-dotstar_featherwing/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/dotstar_featherwing/en/latest/
    :alt: Documentation Status

.. image :: https://badges.gitter.im/adafruit/circuitpython.svg
    :target: https://gitter.im/adafruit/circuitpython?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
    :alt: Gitter

A higher level library for working with the DotStar FeatherWing, build on top of the CircuitPython DotStar driver.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit CircuitPython DotStar <https://github.com/adafruit/Adafruit_CircuitPython_DotStar>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block:: python
				
   import board
   import dotstar_featherwing
   wing = dotstar_featherwing.DotstarFeatherwing(board.D13, board.D11)
   
   xmas = ["..y.w......w",
           "..G.....w...",
           "..G..w....w.",
           ".GGG...w....",
           "GGGGG.......",
           "wwwwwwwwwwww"]
   
   xmas_colours = {'w': (0x20, 0x20, 0x20),
                   'W': (0xFF, 0xFF, 0xFF),
                   'G': (0x00, 0x20, 0x00),
                   'y': (0x20, 0x20, 0x00),
                   'Y': (0xFF, 0xFF, 0x00)}

   wing.display_coloured_image(xmas, xmas_colours)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_dotstar_featherwing/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

API Reference
=============

.. toctree::
   :maxdepth: 2

   api
