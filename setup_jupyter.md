# Jupyter Notebook & WebPDF Setup Guide (Windows / PowerShell)

Run the following commands in PowerShell to set up Python 3.12, Jupyter Notebook, and Playwright for WebPDF export:

```powershell
winget install --exact --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install -U notebook "nbconvert[webpdf]"
python -m playwright install chromium
python -m notebook
```

## Step-by-Step Command Breakdown

1. **Install Python 3.12**:
   ```powershell
   winget install --exact --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements
   ```
   Installs official Python 3.12 via Windows Package Manager (`winget`) with source and package license agreements auto-accepted.

2. **Refresh Environment PATH in Current Shell**:
   ```powershell
   $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
   ```
   Reloads system and user `PATH` environment variables so PowerShell immediately recognizes `python` and `pip` without needing a terminal restart.

3. **Bootstrap and Upgrade PIP**:
   ```powershell
   python -m ensurepip --upgrade
   python -m pip install --upgrade pip
   ```
   Ensures `pip` is installed and upgrades it to the latest release.

4. **Install Jupyter Notebook & WebPDF Dependencies**:
   ```powershell
   python -m pip install -U notebook "nbconvert[webpdf]"
   ```
   Installs the Jupyter Notebook interface and `nbconvert` with the `webpdf` extra for exporting `.ipynb` notebooks directly to PDF.

5. **Install Chromium Browser for PDF Rendering**:
   ```powershell
   python -m playwright install chromium
   ```
   Downloads the headless Chromium binary required by Playwright to render notebooks and print high-fidelity PDFs.

6. **Launch Jupyter Notebook**:
   ```powershell
   python -m notebook
   ```
   Starts the local Jupyter Notebook server and opens the interface in your default browser.
