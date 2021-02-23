# KDB to Vault Tools

Package that allow migrate from kdb to vault and vise versa

### Example
- Start vault in development mode
```bash
docker-compose up
```

- Prepare simple script or use `kdb_2_vault.py`

```python
from kdb_vault_tools import Processor

def create_kdb():
    vault_conf = {"url": "http://localhost:1234", "token": "myroot"}
    kdb_conf = {
        "filename": "kdb_tmp/secrets-20190422.kdbx",
        "password": "superSecret123",
    }

    processor = Processor(vault_settings=vault_conf, kdb_settings=kdb_conf)
    processor.sync_from_kdb()
    processor.write_vault(base_path="/sandbox/org/team/foo/")


def fill_vault():
    vault_conf = {"url": "http://localhost:1234", "token": "myroot"}
    kdb_conf = {
        "filename": "kdb_tmp/secrets-20190422.kdbx",
        "password": "superSecret123",
    }

    processor = Processor(vault_settings=vault_conf, kdb_settings=kdb_conf)
    processor.sync_from_kdb()
    processor.write_vault(base_path="/sandbox/org/team/foo/") 
```

### History
Version 0.1.0 (2021-02-23) - Base Concept

### Credits
Lead Developer - Max Nikitenko (moaddib666@gmail.com)

### License
The MIT License (MIT)

Copyright (c) 2021 Max Nikitenko

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.