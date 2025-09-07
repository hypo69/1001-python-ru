import re
import sys

def convert_md_to_html_content(md_content: str) -> str:
    lines = md_content.splitlines()
    html_lines = []
    in_code_block = False
    code_fence = ""
    code_language = "python"

    for line in lines:
        if line.startswith("```"):
            if not in_code_block:
                match = re.match(r"```(\w+)", line)
                code_language = match.group(1).lower() if match else "python"
                code_fence = line[:3]
                html_lines.append(f'<pre class="line-numbers"><code class="language-{code_language}">')
                in_code_block = True
            else:
                html_lines.append('</code></pre>')
                in_code_block = False
                code_fence = ""
            continue

        if in_code_block:
            html_lines.append(line)
            continue

        stripped = line.strip()

        if stripped == "":
            continue

        if re.match(r"^(\*|\d+\.)\s", line):
            content = re.sub(r"^(\*|\d+\.)\s+", "", line, count=1).strip()
            processed = process_mixed_text(content)
            html_lines.append(f"<li>{processed}</li>")
            continue

        if re.match(r"^#{2,6}\s", line):
            level = len(re.match(r"^#+", line).group())
            content = line.strip("# ").strip()
            processed = process_mixed_text(content)
            html_lines.append(f"<h{level}>{processed}</h{level}>")
            continue

        processed = process_mixed_text(line.strip())
        html_lines.append(f"<p>{processed}</p>")

    return "\n".join(html_lines)

def process_mixed_text(text: str) -> str:
    patterns = [
        r'`[^`]+`',
        r'\b\w*__\w*\b',
        r'dir\(\)',
        r'dict\(\)',
        r'\b[A-Z][a-zA-Z0-9_]*\([^)]*\)',
        r'\b[a-zA-Z][\w.()]*\b',
    ]

    def wrap_match(match):
        matched = match.group(0)
        if any(c.isascii() and c.isalpha() for c in matched):
            return f'<span dir="ltr">{matched}</span>'
        return matched

    result = text

    def replace_inline_code(match):
        code = match.group(0)
        clean = code.strip("`")
        wrapped = f'<span dir="ltr"><code>{clean}</code></span>'
        return wrapped

    result = re.sub(r'`[^`]+`', replace_inline_code, result)

    for pattern in patterns:
        result = re.sub(pattern, wrap_match, result)

    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        md_file_path = sys.argv[1]
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        html_content = convert_md_to_html_content(md_content)
        print(html_content)
    else:
        print("Usage: python temp_convert_md_to_html.py <markdown_file_path>")
