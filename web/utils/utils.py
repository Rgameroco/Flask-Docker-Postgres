def replace_unicode_character(content: str):
    content = content.encode('utf-8')
    if "\\x80" in str(content):
        count_unicode = 0
        i = 0
        while i < len(content):
            if "\\x" in str(content[i:i + 1]):
                if count_unicode % 3 == 0:
                    content = content[:i] + b'\x80\x80\x80' + content[i + 3:]
                i += 2
                count_unicode += 1
            i += 1

        content = content.replace(b'\x80\x80\x80', b'')
    return content.decode('utf-8')