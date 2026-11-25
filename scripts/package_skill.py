"""Build a reproducible, installable skill ZIP using only the Python standard library."""

import argparse
import hashlib
from pathlib import Path
import re
import shutil
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="Release version, for example v0.1.0")
    parser.add_argument("--source-archive", type=Path, help="Also preserve an original supplied skill ZIP as a separate release asset")
    args = parser.parse_args()
    if not re.fullmatch(r"v\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?", args.version):
        parser.error("Use a version such as v0.1.0 or v0.2.0-beta.1")
    if args.source_archive:
        if not args.source_archive.is_file() or args.source_archive.suffix.lower() != ".zip":
            parser.error("--source-archive must name an existing ZIP file")
        if args.source_archive.name == f"design-academic-slides-{args.version}.zip":
            parser.error("The source archive must have a distinct name from the reviewed installation package")
        with ZipFile(args.source_archive) as supplied:
            if supplied.testzip() is not None:
                parser.error("The source archive failed its integrity check")

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

    assets = [archive]
    if args.source_archive:
        preserved = output / args.source_archive.name
        if args.source_archive.resolve() != preserved.resolve():
            shutil.copyfile(args.source_archive, preserved)
        assets.append(preserved)
    digests = [(hashlib.sha256(asset.read_bytes()).hexdigest(), asset.name) for asset in assets]
    checksum = output / "SHA256SUMS.txt"
    checksum.write_text("".join(f"{digest}  {name}\n" for digest, name in digests), encoding="utf-8")
    print(f"Built {archive.name} ({len(files)} files)")
    for digest, name in digests:
        print(f"SHA256: {digest}  {name}")
    print(f"Output: {output}")


if __name__ == "__main__":
    main()
