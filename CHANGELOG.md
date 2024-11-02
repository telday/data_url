# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2024-11-02

### Changed

- DataURL.from_data no longer accepts bytes type. Use DataURL.from_byte_data instead.
- Moves Regex to use raw string to avoid [warning](https://github.com/telday/data_url/issues/3)
- Adds "-" to list of acceptable characters for string data in a URL.