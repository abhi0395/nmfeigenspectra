DR14_QSO_NMF_zQSO_zmin_zmax_basis.fits
--------------------------------------

This FITS file contains eigenspectra basis vectors and rest-frame wavelengths for a subset of quasars from the SDSS DR14 catalog. The data are generated using a Non-negative Matrix Factorization (NMF) method applied to quasars in following redshift (zqso) ranges:

    1) 0 < z < 1
    2) 0.4 < z < 1.8
    3) 0.8 < z < 2.8
    4) 2 < z < 4.8

## File Structure

The file is composed of three HDUs:

### HDU 0 — Primary Header
Contains metadata about the file and the fitting process.

| Keyword | Value       | Description                               |
|---------|-------------|-------------------------------------------|
| AUTHOR  | A.Anand     | Data author                               |
| QSOVAC  | SDSS DR14   | Source QSO catalog                        |
| EIGFIT  | NMF         | Fitting method used (Zhu NMF)             |
| ZMIN    | zmin         | Minimum redshift of quasars in this file  |
| ZMAX    | zmax        | Maximum redshift of quasars in this file  |

### HDU 1 — EIGENVEC

- **Type**: 2D image array
- **EXTNAME**: `EIGENVEC`
- **Description**: The NMF eigenspectra coefficients for each quasar.

### HDU 2 — REST_WAVE

- **Type**: 1D image array
- **EXTNAME**: `REST_WAVE`
- **Description**: The corresponding rest-frame wavelengths for each entry in the EIGENVEC array.

## Description

This basis file provides a compact representation of quasar spectra using NMF. It is intended for spectral modeling, analysis of spectral diversity, or further dimensionality reduction tasks.

