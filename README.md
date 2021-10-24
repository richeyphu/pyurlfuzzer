# pyurlfuzzer
**pyurlfuzzer** is a simple website directory scanner, written in Python.

## Usage
### Example
```ps1
Input target : google.com
--------------------------------------------------
Fuzzing : █ (1.85%)	path=/.well-known/resourcesync	status=200
Fuzzing : █ (2.87%)	path=/2000	status=200
Fuzzing : █ (2.89%)	path=/2001	status=200
Fuzzing : █ (2.91%)	path=/2002	status=200
Fuzzing : █ (2.93%)	path=/2003	status=200
.
.
.
Fuzzing : ████████████████████████████████████████████████ (96.62%)	path=/wordpress	status=200
Fuzzing : █████████████████████████████████████████████████ (98.38%)	path=/xfer	status=405
Fuzzing : ██████████████████████████████████████████████████ (100.00%)	path=/~www
```
### Required Package
- [`requests`](https://pypi.org/project/requests/)

## Notes
- [`common.txt`](https://github.com/richeyphu/pyurlfuzzer/blob/main/src/common.txt) file courtesy of [SecLists](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt)
- For much w0w edition, please check out here : [LucusExpress](https://github.com/karinzaa/LucusExpress)
