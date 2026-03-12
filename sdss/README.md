
SDSS DR14 based NMF Eigenspectra for Quasar Continuum Modeling
--------------------------------------

This directory contains eigenspectra basis vectors and rest-frame wavelengths that can be used to build continuum of SDSS quasars. The data are generated using a Non-negative Matrix Factorization (NMF) method applied to SDSS DR14 spectra in the following redshift ranges:

    1) 0 < z < 1.0
    2) 0.40 < z < 1.80
    3) 0.80 < z < 2.80
    4) 2.0 < z < 4.80

Each file is named by their redshift range: `SDSS_DR14_z_zmin_zmax_eigenspectra.fits`

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
| NORMSTAT  | Statistic used for normalization |
| AUTHOR    | Data author                               |
| QSOVAC    | Survey name and Data Release  |
| EIGFIT    | Eigenspectra fit method: NMF    

### HDU 1 — EIGENVEC

- **Type**: 2D image array
- **EXTNAME**: `EIGENVEC`
- **Description**: The NMF eigenspectra coefficients for each quasar.

### HDU 2 — REST_WAVE

- **Type**: 1D image array
- **EXTNAME**: `REST_WAVE`
- **Description**: The corresponding rest-frame wavelengths for each entry in the EIGENVEC array.

## Description

This basis file provides a compact representation of SDSS quasar spectra using NMF. It is intended for continuum modeling, analysis of spectral diversity, or further dimensionality reduction tasks.