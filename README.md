# echoserver

Echo back HTTP request data as text or json. **Server runs on port 5000.**

### endpoints

- `/`: echo request as text representation
- `/json`: echo request back in JSON format

---

```bash
usage: echoserver.py [-h] [--stdout]

light server for echoing back HTTP requests

options:
  -h, --help  show this help message and exit
  --stdout    print HTTP request data to stdout
```
