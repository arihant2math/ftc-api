# 0.0.0
* Initial Release
### 0.0.1
* Changed default prefix of Authorization header to "Basic", which should be the default for the API
* Fixed bug that caused double //s when requesting an api endpoint.
### 0.0.2
* Fixed numbering in pyproject.toml
## 0.1.0
* Merged `Client` with `AuthenticatedClient` using `AuthenticatedClient` is now deprecated
* Added support for creating a Client with a username and access key
* Removed `attrs` as a dependency
* Added support for [ftcstats](https://ftcstats.org)
