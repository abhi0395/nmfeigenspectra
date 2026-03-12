DESI DR1 based NMF Eigenspectra for Quasar Continuum Modeling
--------------------------------------

This directory contains eigenspectra basis vectors and rest-frame wavelengths that can be used to build continuum of DESI quasars. The data are generated using a Non-negative Matrix Factorization (NMF) method applied to DESI DR1 spectra in the following redshift ranges:

    1) 0 < z < 1.20
    2) 0.60 < z < 2.10
    3) 1.60 < z < 3.30
    4) 2.60 < z < 5.00

Each file is named by their redshift range: `DESI_DR1_z_zmin_zmax_eigenspectra.fits`

## File Structure

The file is composed of three HDUs:

### HDU 0 — Primary Header
Contains metadata about the file and the fitting process.

| Keyword   | Description                               |
|-----------|-------------------------------------------|
| METHOD    | Eigenspectra construction method used (NMF)             |
| ZMIN      | Minimum redshift of QSOs used for NMF construction |
| ZMAX      | Maximum redshift of QSOs used for NMF construction  |
| LAMSTART  | Starting wavelength (Ang) for normalization    |
| LAMEND    | Ending wavelength (Ang) for normalization      |
| NCOMP     | Number of NMF basis components                  |
| MAXIT     | Maximum number of iterations during fit   |
| SIGCLIP   | Sigma-clipping threshold (to remove outliers)                  |
| SCLNIT    | Number of iterations to remove outliers       |
| NORMSTAT  | Statistic used for normalization |
| CHI2RED   | Reduced chi-squared of the fit            |
| AUTHOR    | Data author                               |
| SURVEY    | Survey name and Data Release                             |

### HDU 1 — REST_WAVE

- **Type**: 1D image array
- **EXTNAME**: `REST_WAVE`
- **Description**: The corresponding rest-frame wavelengths for each entry in the EIGENVEC array.

### HDU 2 — EIGENVEC

- **Type**: 2D image array
- **EXTNAME**: `EIGENVEC`
- **Description**: The NMF eigenspectra coefficients for each spectrum.

## Description

This basis file provides a compact representation of DESI quasar spectra using NMF. It is intended for continuum modeling, analysis of spectral diversity, or further dimensionality reduction tasks.