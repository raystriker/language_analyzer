import zipfile
import os
import tempfile
from collections import Counter
import argparse

def identify_language(file_name, other_types):
    ext = os.path.splitext(file_name)[1]
    language_map = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.html': 'HTML',
        '.css': 'CSS',
        '.java': 'Java',
        '.c': 'C',
        '.cpp': 'C++',
        '.txt': 'Text',
        '.md': 'Markdown',
        '.json': 'JSON',
        '.xml': 'XML',
        '.yaml': 'YAML',
        '.csv': 'CSV',
        '.ts': 'TypeScript',
        '.sh': 'Shell',
        '.bat': 'Batch',
        '.php': 'PHP',
        '.go': 'Go',
        '.rb': 'Ruby',
        '.txt': 'Text',
        '.log': 'Log',
        '.ini': 'INI',
        '.sql': 'SQL',
        '.zip': 'ZIP',
        '.rar': 'RAR',
        '.pdf': 'PDF',
        # Add more mappings here
    }
    return language_map.get(ext, other_types.setdefault(ext, f"Other ({ext})"))

def process_files(directory, other_types):
    languages = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            language = identify_language(file, other_types)
            languages.append(language)
    return languages

def process_zip(zip_path):
    other_types = {}
    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
            languages = process_files(temp_dir, other_types)
        display_results(languages, other_types)

def format_table(data):
    header = ['Language/File Type', 'Percentage', 'File Count']
    row_format = "{:<20} {:<15} {:<10}"
    table_lines = []

    # Header line
    table_lines.append(row_format.format(*header))
    table_lines.append("-" * 50)

    # Data lines
    for language, count in data.items():
        percentage = (count / sum(data.values())) * 100
        if count != 1:
            table_lines.append(row_format.format(language, f"{percentage:.2f}%", f"{count} files"))
        else:
            table_lines.append(row_format.format(language, f"{percentage:.2f}%", f"{count} file"))

    return "\n".join(table_lines)

def display_results(languages, other_types):
    total_files = len(languages)
    language_counts = Counter(languages)

    # Sort the results by file count in descending order
    sorted_results = {lang: count for lang, count in sorted(language_counts.items(), key=lambda item: item[1], reverse=True)}

    print(f"Total number of files: {total_files}")
    print("Programming languages and file types used, their percentages, and number of files:")
    print(format_table(sorted_results))


def main():
    parser = argparse.ArgumentParser(description="Analyze the programming languages in a ZIP file or a directory.")
    parser.add_argument('path', type=str, help='Path to the ZIP file or directory')
    parser.add_argument('--type', choices=['zip', 'folder'], default='zip', help='Type of the input path (zip or folder)')
    args = parser.parse_args()

    if args.type == 'zip':
        process_zip(args.path)
    else:
        other_types = {}
        languages = process_files(args.path, other_types)
        display_results(languages, other_types)

if __name__ == "__main__":
    main()
