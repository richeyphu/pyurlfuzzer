# pyurlfuzzer
**pyurlfuzzer** is a simple website directory scanner written in Python.

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
Fuzzing : █ (2.96%)	path=/2004	status=200
Fuzzing : █ (2.98%)	path=/2005	status=200
Fuzzing : █ (3.00%)	path=/2006	status=200
Fuzzing : ██ (3.02%)	path=/2007	status=200
Fuzzing : ██ (3.04%)	path=/2008	status=200
Fuzzing : ██ (3.06%)	path=/2009	status=200
Fuzzing : ██ (3.08%)	path=/2010	status=200
Fuzzing : ██ (3.11%)	path=/2011	status=200
Fuzzing : ██ (3.13%)	path=/2012	status=200
Fuzzing : ██ (3.15%)	path=/2013	status=200
Fuzzing : ███ (6.51%)	path=/Recycled	status=200
...
```
### Required Package
- [`requests`](https://pypi.org/project/requests/)

## Notes
- "common.txt" file courtesy of [SecLists](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt)
- For much w0w edition, please check out here : [LucusExpress](https://github.com/karinzaa/LucusExpress)
