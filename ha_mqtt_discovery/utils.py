def sanitize_name(name: str):
    return name.lower().replace('-', '_').replace(' ', '_').replace('.', '_')
