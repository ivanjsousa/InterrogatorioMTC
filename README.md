# InterrogatorioMTC

This project contains a graphical questionnaire built with [Flet](https://flet.dev/). The application allows recording Traditional Chinese Medicine (MTC) interrogation data and saving it to text files.

## Requirements

- Python 3.9 or newer
- [Flet](https://pypi.org/project/flet/) library

Install dependencies with:

```bash
pip install flet
```

## Running the application

Execute the main script using Python:

```bash
python Main_1.py
```

This launches a window with the MTC questionnaire. After filling in the form, use the **Salvar** button to store the answers.

## Where data is saved

Text files with the collected information are saved inside the `dados_interrogatorio/` directory. Each file name includes a timestamp, e.g. `interrogatorio_mtc_YYYYMMDD_HHMMSS.txt`.
