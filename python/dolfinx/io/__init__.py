# Copyright (C) 2022 Jørgen S. Dokken
#
# This file is part of DOLFINx (https://www.fenicsproject.org)
#
# SPDX-License-Identifier:    LGPL-3.0-or-later
"""Tools for file input/output (IO)."""

from dolfinx import cpp as _cpp
from dolfinx.io import gmshio  # noqa: F401
from dolfinx.io.utils import (VTKFile, XDMFFile,  # noqa: F401
                              distribute_entity_data)

__all__ = ["gmshio", "distribute_entity_data", "VTKFile", "XDMFFile"]

if _cpp.common.has_adios2:
    # FidesWriter and VTXWriter require ADIOS2
    from dolfinx.io.utils import (FidesMeshPolicy, FidesWriter,  # noqa: F401
                                  VTXWriter)
    __all__ = __all__ + ["FidesWriter", "VTXWriter", "FidesMeshPolicy"]
