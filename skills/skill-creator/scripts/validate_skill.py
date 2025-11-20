#!/usr/bin/env python3
"""
Validate Agent Skill YAML frontmatter and structure.

Usage:
    python validate_skill.py path/to/SKILL.md
"""

import sys
import re
from pathlib import Path

# Validation rules
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
RESERVED_WORDS = ["anthropic", "claude"]
NAME_PATTERN = re.compile(r'^[a-z0-9\-]+$')
XML_TAG_PATTERN = re.compile(r'<[^>]+>')

def extract_frontmatter(content):
    """Extract YAML frontmatter from SKILL.md content."""
    lines = content.split('\n')

    if not lines or lines[0].strip() != '---':
        return None, "Missing YAML frontmatter (must start with '---')"

    frontmatter_lines = []
    end_index = None

    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            end_index = i
            break
        frontmatter_lines.append(line)

    if end_index is None:
        return None, "YAML frontmatter not properly closed (missing closing '---')"

    return '\n'.join(frontmatter_lines), None

def parse_frontmatter(frontmatter):
    """Parse YAML frontmatter into dict."""
    data = {}
    for line in frontmatter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    return data

def validate_name(name):
    """Validate name field."""
    errors = []

    if not name:
        errors.append("name field is required and cannot be empty")
        return errors

    if len(name) > MAX_NAME_LENGTH:
        errors.append(f"name exceeds maximum length of {MAX_NAME_LENGTH} characters (found {len(name)})")

    if not NAME_PATTERN.match(name):
        errors.append("name must contain only lowercase letters, numbers, and hyphens")

    if XML_TAG_PATTERN.search(name):
        errors.append("name cannot contain XML tags")

    for word in RESERVED_WORDS:
        if word in name.lower():
            errors.append(f"name cannot contain reserved word '{word}'")

    return errors

def validate_description(description):
    """Validate description field."""
    errors = []

    if not description:
        errors.append("description field is required and cannot be empty")
        return errors

    if len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(f"description exceeds maximum length of {MAX_DESCRIPTION_LENGTH} characters (found {len(description)})")

    if XML_TAG_PATTERN.search(description):
        errors.append("description cannot contain XML tags")

    # Check for first/second person (heuristic)
    first_person_patterns = [r'\bI\b', r'\bmy\b', r'\bme\b', r"I'm", r"I'll"]
    second_person_patterns = [r'\byou\b', r'\byour\b', r'\byou\'re', r'\byou\'ll']

    for pattern in first_person_patterns:
        if re.search(pattern, description, re.IGNORECASE):
            errors.append("description should use third person, not first person (avoid 'I', 'my', 'me')")
            break

    for pattern in second_person_patterns:
        if re.search(pattern, description, re.IGNORECASE):
            errors.append("description should use third person, not second person (avoid 'you', 'your')")
            break

    # Check for "what + when" pattern (heuristic)
    has_when_indicator = any(phrase in description.lower() for phrase in [
        'use when', 'when the user', 'when working', 'when creating',
        'when implementing', 'when managing', 'when analyzing'
    ])

    if not has_when_indicator:
        errors.append("description should include 'when to use' guidance (e.g., 'Use when...')")

    return errors

def count_lines(content):
    """Count lines in SKILL.md body (excluding frontmatter)."""
    lines = content.split('\n')

    # Skip frontmatter
    start_index = 0
    frontmatter_count = 0

    for i, line in enumerate(lines):
        if line.strip() == '---':
            frontmatter_count += 1
            if frontmatter_count == 2:
                start_index = i + 1
                break

    body_lines = lines[start_index:]
    return len([line for line in body_lines if line.strip()])

def validate_skill(filepath):
    """Validate a Skill file."""
    errors = []
    warnings = []

    # Check file exists
    path = Path(filepath)
    if not path.exists():
        return [f"File not found: {filepath}"], []

    # Check filename
    if path.name != "SKILL.md":
        warnings.append(f"Skill file should be named 'SKILL.md', found '{path.name}'")

    # Read content
    try:
        content = path.read_text()
    except Exception as e:
        return [f"Error reading file: {e}"], []

    # Extract frontmatter
    frontmatter, error = extract_frontmatter(content)
    if error:
        return [error], []

    # Parse frontmatter
    data = parse_frontmatter(frontmatter)

    # Validate name
    name = data.get('name', '')
    name_errors = validate_name(name)
    errors.extend(name_errors)

    # Validate description
    description = data.get('description', '')
    desc_errors = validate_description(description)
    errors.extend(desc_errors)

    # Count body lines
    line_count = count_lines(content)
    if line_count > 500:
        warnings.append(f"SKILL.md body has {line_count} lines (recommended: under 500). Consider using progressive disclosure with separate reference files.")

    return errors, warnings

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_skill.py <SKILL.md>", file=sys.stderr)
        print("\nValidates Agent Skill YAML frontmatter and structure.")
        sys.exit(1)

    filepath = sys.argv[1]

    print(f"Validating: {filepath}")
    print()

    errors, warnings = validate_skill(filepath)

    if errors:
        print("❌ VALIDATION FAILED")
        print()
        print("Errors:")
        for error in errors:
            print(f"  - {error}")
        print()

        if warnings:
            print("Warnings:")
            for warning in warnings:
                print(f"  - {warning}")
            print()

        sys.exit(1)

    if warnings:
        print("⚠️  VALIDATION PASSED WITH WARNINGS")
        print()
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
        print()
        sys.exit(0)

    print("✓ VALIDATION PASSED")
    print()
    print("SKILL.md is valid and follows all best practices!")
    sys.exit(0)

if __name__ == "__main__":
    main()
