"""
Test suite for validating NMF eigenspectra FITS files.
Run with: pytest test_validation.py -v
"""

import os
import re
import pytest
from astropy.io import fits
from pathlib import Path
import numpy as np


def get_data_root():
    """Get the root directory containing NMF eigenspectra folders for different surveys."""
    return Path(__file__).parent.parent


def get_all_fits_files():
    """Collect all .fits files from survey directories."""
    root = get_data_root()
    fits_files = []
    for survey_dir in root.glob("*/"):
        if survey_dir.is_dir() and survey_dir.name not in ["test", ".git"]:
            fits_files.extend(survey_dir.glob("*.fits"))
    return sorted(fits_files)


class TestFileNaming:
    """Tests for FITS file naming conventions."""

    def test_fits_files_exist(self):
        """Ensure FITS files are present in survey directories."""
        fits_files = get_all_fits_files()
        assert len(fits_files) > 0, "No FITS files found in survey directories"

    def test_naming_convention(self):
        """Check that FITS files follow expected naming pattern."""
        fits_files = get_all_fits_files()
        # Pattern: SURVEY_z_ZMIN_ZMAX_eigenspectra.fits where ZMIN/ZMAX are integers (scaled by 100)
        pattern = re.compile(r"^([A-Za-z0-9_]+)_z_(\d{3})_(\d{3})_(eigenspectra)\.fits$")

        for fits_file in fits_files:
            filename = fits_file.name
            assert pattern.match(filename), f"File '{filename}' does not match naming convention"

    def test_filename_parsing(self):
        """Verify redshift bounds can be extracted from filename."""
        fits_files = get_all_fits_files()
        pattern = re.compile(r"z_(\d+)_(\d+)")

        for fits_file in fits_files:
            match = pattern.search(fits_file.name)
            assert match is not None, f"Could not parse redshift bounds from '{fits_file.name}'"
            # Filename uses scaled integers: z_000_120 means 0.00 to 1.20
            zmin_scaled = int(match.group(1))
            zmax_scaled = int(match.group(2))
            zmin = zmin_scaled / 100.0
            zmax = zmax_scaled / 100.0
            assert zmin < zmax, f"Invalid redshift range in '{fits_file.name}': zmin={zmin} >= zmax={zmax}"


class TestFITSStructure:
    """Tests for FITS file internal structure."""

    def test_fits_readable(self):
        """Ensure all FITS files can be opened without errors."""
        fits_files = get_all_fits_files()
        for fits_file in fits_files:
            with fits.open(fits_file) as hdul:
                assert len(hdul) >= 3, f"'{fits_file.name}' has fewer than 3 HDUs"

    def test_required_extensions(self):
        """Check for required extension names."""
        fits_files = get_all_fits_files()
        for fits_file in fits_files:
            with fits.open(fits_file) as hdul:
                ext_names = [hdu.name.upper() for hdu in hdul]
                assert "EIGENVEC" in ext_names, f"'{fits_file.name}' missing EIGENVEC extension"
                assert "REST_WAVE" in ext_names, f"'{fits_file.name}' missing REST_WAVE extension"

    def test_required_headers(self):
        """Check for required header keywords in PRIMARY HDU."""
        fits_files = get_all_fits_files()
        required_keys = {"METHOD", "ZMIN", "ZMAX", "AUTHOR", "NORMSTAT", "LAMSTART", "LAMEND"}

        for fits_file in fits_files:
            with fits.open(fits_file) as hdul:
                header = hdul[0].header
                for key in required_keys:
                    assert key in header, f"'{fits_file.name}' PRIMARY header missing '{key}'"

    def test_data_shapes(self):
        """Verify EIGENVEC and REST_WAVE have compatible shapes."""
        fits_files = get_all_fits_files()
        for fits_file in fits_files:
            with fits.open(fits_file) as hdul:
                eigenvec = hdul["EIGENVEC"].data
                rest_wave = hdul["REST_WAVE"].data

                assert eigenvec.ndim == 2, f"'{fits_file.name}' EIGENVEC should be 2D"
                assert rest_wave.ndim == 1, f"'{fits_file.name}' REST_WAVE should be 1D"
                # EIGENVEC can be (wavelengths, components) or (components, wavelengths)
                # Just ensure one dimension matches wavelength array length
                assert len(rest_wave) in eigenvec.shape, \
                    f"'{fits_file.name}' shape mismatch: REST_WAVE length {len(rest_wave)} not in EIGENVEC shape {eigenvec.shape}"


class TestDataIntegrity:
    """Tests for data quality and consistency."""

    def test_no_invalid_values(self):
        """Check for NaN or inf values in eigenspectra."""
        fits_files = get_all_fits_files()
        for fits_file in fits_files:
            with fits.open(fits_file) as hdul:
                eigenvec = hdul["EIGENVEC"].data
                rest_wave = hdul["REST_WAVE"].data

                assert not np.any(np.isnan(eigenvec)), f"'{fits_file.name}' EIGENVEC contains NaN"
                assert not np.any(np.isinf(eigenvec)), f"'{fits_file.name}' EIGENVEC contains inf"
                assert not np.any(np.isnan(rest_wave)), f"'{fits_file.name}' REST_WAVE contains NaN"

    def test_redshift_consistency(self):
        """Verify redshift header values are within filename bounds."""
        fits_files = get_all_fits_files()
        pattern = re.compile(r"z_(\d+)_(\d+)")

        for fits_file in fits_files:
            match = pattern.search(fits_file.name)
            # Filename uses scaled integers: z_000_120 means 0.00 to 1.20
            zmin_scaled = int(match.group(1))
            zmax_scaled = int(match.group(2))
            name_zmin = zmin_scaled / 100.0
            name_zmax = zmax_scaled / 100.0

            with fits.open(fits_file) as hdul:
                header = hdul[0].header
                header_zmin = float(header["ZMIN"])
                header_zmax = float(header["ZMAX"])

                # Header values should be close to filename bounds (filename may be rounded)
                # Allow up to 10% tolerance for rounding
                z_range = name_zmax - name_zmin
                tolerance = max(0.1, 0.1 * z_range)
                assert abs(name_zmin - header_zmin) < tolerance, \
                    f"'{fits_file.name}' ZMIN too far from header: filename={name_zmin}, header={header_zmin}"
                assert abs(name_zmax - header_zmax) < tolerance, \
                    f"'{fits_file.name}' ZMAX too far from header: filename={name_zmax}, header={header_zmax}"


class TestSurveyREADMEs:
    """Tests for survey documentation."""

    def test_readme_in_surveys(self):
        """Check that each survey directory has a README."""
        root = get_data_root()
        for survey_dir in root.glob("*/"):
            if survey_dir.is_dir() and survey_dir.name not in ["test", ".git", ".github"]:
                readme = survey_dir / "README.md"
                assert readme.exists(), f"'{survey_dir.name}/' missing README.md"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
