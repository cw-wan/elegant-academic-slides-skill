"""Build a reproducible, installable skill ZIP using only the Python standard library."""

import argparse
import hashlib
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="Release version, for example v0.1.0")
    args = parser.parse_args()
    if not re.fullmatch(r"v\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?", args.version):
        parser.error("Use a version such as v0.1.0 or v0.2.0-beta.1")

    root = Path(__file__).resolve().parents[1]
    source = root / "skills" / "design-academic-slides"
    if not (source / "SKILL.md").is_file():
        parser.error("The skill source is missing SKILL.md")
    files = sorted(
        path for path in source.rglob("*")
        if path.is_file()
        and not any(part.startswith(".") or part == "__pycache__" for part in path.relative_to(source).parts)
        and path.suffix not in {".pyc", ".pyo"}
    )
    if any(path.is_symlink() or not path.resolve().is_relative_to(source.resolve()) for path in files):
        parser.error("Skill package files must be regular files inside the source directory")

    output = root / "dist"
    output.mkdir(exist_ok=True)
    archive = output / f"design-academic-slides-{args.version}.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in files:
            name = f"{source.name}/{path.relative_to(source).as_posix()}"
            entry = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            entry.compress_type = ZIP_DEFLATED
            bundle.writestr(entry, path.read_bytes(), compresslevel=9)

    with ZipFile(archive) as bundle:
        if bundle.testzip() is not None:
            raise RuntimeError("Archive integrity check failed")
        for path in files:
            name = f"{source.name}/{path.relative_to(source).as_posix()}"
            if bundle.read(name) != path.read_bytes():
                raise RuntimeError(f"Archive content differs from source: {name}")

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = output / "SHA256SUMS.txt"
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(f"Built {archive.name} ({len(files)} files)")
    print(f"SHA256: {digest}")
    print(f"Output: {output}")


if __name__ == "__main__":
    main()
