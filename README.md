## Tutorial Implementasi Poetry

Poetry adalah tool untuk dependency management dan membuat package atau sebuah library dari project yang telah dibuat, termasuk untuk melakukan install atau update.
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

- Langkah selanjutnya adalah melakukan publish ke *pypi server*.
dengan melakukan publish ke *pypi server* maka module atau package dapat digunakan di project lain. Script dibawah ini untuk menambahkan source ke server pypi

```
poetry source add <name_source> http://<ip_server>:8080/simple/
```

Kemudian memasukan config pada poetry

```
poetry config repositories.<name_source> http://<ip_server>:6060
poetry config http-basic.<name_source> <username> <password>
```

Setelah itu, melakukan build script yang telah dibuat dengan script dibawah ini: 

```
poetry build
```

dan langkah terakhir, melakukan publish ke *pypi server* dengan script dibawah ini: 

```
poetry publish --build --repository <name_source>
```

kemudian check ke *http://<ip_server>:6060/simple/* apakah package telah terbuat.


### Reference: 
- https://github.com/oktapiancaw/module-typica
