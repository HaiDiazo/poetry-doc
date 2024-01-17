## Tutorial Using Poetry

Berikut adalah langkah untuk melakukan konfigurasi poetry

- Langkah pertama, lakukan instalasi Poetry terlebih dahulu,
source: [Poetry Instalation](https://python-poetry.org/docs/#installing-with-the-official-installer)

- Selanjutnya, script dibawah ini untuk melakukan buat create project dengan poetry

```
poetry new poetry-demo
```

- Selanjutnya, script dibawah ini untuk melakukan konfigurasi package

```
poetry lock
```

- langkah selanjutnya, untuk menambahkan package dapat melalui script dibawah ini, sebagai contoh script dibawah ini akan melakukan install package *loguru*

```
poetry add loguru
```
atau dapat melakukan edit pada file *pyproject.toml*

```
[tool.poetry.dependencies]
python = "^3.9"
loguru = "0.6.0"
```

- Jika, menggunakan edit file *pyproject.toml*, maka harus melakukan script dibawah ini

```
poetry lock
poetry install
```

Sehingga, package akan terinstall

Selain itu, untuk melakukan inisialisasi env seperti conda activate <nama_env> (jika menggunakan conda) atau source venv/bin/activate (jika menggunakan venv), maka di poetry dapat menggunakan script dibawah ini:

```
poetry shell
```

### Reference: 
- https://github.com/oktapiancaw/module-typica