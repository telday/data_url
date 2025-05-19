# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.1] - 2025-05-19

### Fixed

- Allow for "." character to be used in [mime-types](https://github.com/telday/data_url/issues/8).

## [1.2.0] - 2024-11-20

### Fixed

- Fixed missing RFC specification allowing blank mime type

## [1.1.1] - 2024-11-20

### Fixed

- Fixed bug with using `construct_data_url` with string type parameters

## [1.1.0] - 2024-11-02

### Changed

- DataURL.from_data no longer accepts bytes type. Use DataURL.from_byte_data instead.
- Moves Regex to use raw string to avoid [warning](https://github.com/telday/data_url/issues/3)
- Adds "-" to list of acceptable characters for string data in a URL.
