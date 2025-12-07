#!/usr/bin/env python3
"""
Script to fix LaTeX backslash issues in markdown files.
"""

import re

def fix_latex_backslashes(file_path):
    """Fix double backslashes in LaTeX expressions in markdown files."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix double backslashes in math mode
    # This pattern looks for $...$ or $$...$$ and fixes double backslashes inside
    def fix_math_content(match):
        math_content = match.group(0)
        # Replace \\ with \ but be careful not to break valid LaTeX
        fixed = math_content.replace('\\\\', '\\')
        return fixed

    # Fix inline math: $...$
    content = re.sub(r'\$[^$]*\\[^$]*\$', fix_math_content, content)

    # Fix display math: $$...$$
    content = re.sub(r'\$\$[^$]*\\[^$]*\$\$', fix_math_content, content)

    # Also fix common LaTeX commands that might be double-escaped
    content = content.replace('$\\\\tau_i$', '$\\tau_i$')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed LaTeX backslashes in {file_path}")


if __name__ == "__main__":
    fix_latex_backslashes("website/docs/chapter-2-kinematics-dynamics.md")
    fix_latex_backslashes("website/docs/chapter-4-ai-robot-control-navigation.md")