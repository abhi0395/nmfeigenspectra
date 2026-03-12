# Nonnegative Matrix Factorization (NMF) based Eigenspectra for Quasar Continuum Modeling

This repository collects non-negative matrix factorization (NMF) eigenspectra that
are designed to model and reconstruct quasar continua in large  spectroscopic surveys.  Each set of eigenspectra covers a range of redshifts and wavelengths appropriate for a particular survey; by linearly combining a small number of components one can generate realistic continua for use in fitting,
mock-generation, or dimensionality‑reduction studies.

### Scientific background
The basic technique follows Zhu (2016) and the more recent applications in
Anand et al. (2021, 2025).  The reader is referred to those papers for
details on the NMF algorithm, preprocessing steps, and quality checks.

- **[Zhu (2016)](https://arxiv.org/abs/1612.06037)** — original vectorized NMF implementation for astronomical spectra
- **[Anand et al. (2021)](https://arxiv.org/abs/2103.15842)** — application to SDSS DR14 quasars
- **[Anand et al. (2025)](https://arxiv.org/abs/2504.20299)** — extended analysis and DESI compatibility

> Please cite these papers when using these data if you make use of these eigenspectra basis vectors in your research.

---

## Getting started

Clone the repository to obtain all available eigenspectra files:

```bash
git clone https://github.com/abhi0395/nmfeigenspectra.git
```

Files are stored in survey‑specific subdirectories (e.g. `sdss/`, `desi/`).
See the README in each directory for detailed information on file naming,
redshift bins, and the internal FITS structure.

---

## Running the basic tests

After cloning, please run the following test to confirm the fits file structure and contents.

```bash
cd $REPO
pytest test/test_validation.py -v
```

---

## Datasets included

At the moment the repository contains:

| Survey         | Description                                      | Path   |
|----------------|--------------------------------------------------|--------|
| SDSS DR14      | NMF igenspectra generated from SDSS DR14 QSOs        | `sdss/`|
| DESI DR1       | NMF igenspectra generated from DESI DR1 QSOs    | `desi/`|

The SDSS products were released in 2021; the DESI files were added more
recently and use similar redshift ranges to the DESI data files already
hosted in the `desi/` folder.

Additional surveys (HST, 4MOST, WAVES, PFS, WEAVE, later DESI releases) are planned but not yet
available.

---

## Repository layout

Each survey folder contains one or more FITS files named according to the
pattern:

```
<SURVEY>_z_<zmin>_<zmax>_eigenspectra.fits
```

and a `README.md` describing the contents.  The FITS files typically include
three HDUs:

1. **PRIMARY** – header keywords describing the NMF run (e.g. METHOD, ZMIN,
   ZMAX, AUTHOR)  
2. **EIGENVEC** – 2‑D array of eigenspectra coefficients  
3. **REST_WAVE** – 1‑D array of rest‑frame wavelengths  

Users should inspect the header of each file to confirm the redshift range and
other metadata.

---

## Future directions

Planned enhancements include:

1. Generating NMF bases for HST, DESI DR2, PFS, 4MOST, WAVES, and WEAVE spectra.  

---

## Contributions

Contributions are always welcome; feel free to open an issue or submit a pull
request.

---

## Acknowledgments

If you use these eigenspectra, please cite the appropriate papers listed above.

Abhijeet Anand  
IUCAA Pune
