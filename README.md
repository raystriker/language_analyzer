
# Language Analyzer CLI

## Overview
Language Analyzer CLI is a Python-based command-line tool designed to analyze and report the programming languages used in the files within a given directory or ZIP archive. It provides an easy-to-use interface to quickly identify the distribution and percentage of various programming languages in a project.

## Features
- Support for multiple programming languages.
- Ability to process files from both directories and ZIP archives.
- Detailed report of language usage including file count and percentage.

## Installation
This tool requires Python 3.6 or later. You can clone this repository or download the source code directly.

```bash
git clone https://github.com/[your-username]/language-analyzer-cli.git
cd language-analyzer-cli
```

## Usage
To use the Language Analyzer CLI, you can specify either a directory or a ZIP file path along with the type of the input. 

Analyzing a ZIP file:
```bash
python language_analyzer.py path/to/yourfile.zip --type zip
```

Analyzing a directory:
```bash
python language_analyzer.py path/to/yourdirectory --type folder
```

## Supported Languages
- Python
- JavaScript
- HTML
- CSS
- Java
- C
- C++
- and more

## Extending Language Support
To add support for more languages, edit the `language_map` dictionary in `identify_language` function within the script.

## License
This project is licensed under the [MIT License](LICENSE).