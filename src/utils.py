"""Module containing utilities."""

from __future__ import annotations

__all__: tuple[str, ...] = (
    "resolved_path_from_str",
    "source_to_ast",
    "ast_to_source",
    "exce_ast",
)

import ast
from pathlib import Path


def resolved_path_from_str(path_as_str: str) -> Path:
    """Return the absolute path given a string of a path."""
    return Path(path_as_str.strip()).resolve()


def source_to_ast(filepath: Path) -> ast.Module:
    """Return the AST of the given Python file."""
    contents: str = filepath.read_text(encoding="utf-8")
    return ast.parse(contents, filename=filepath.name)


def ast_to_source(tree: ast.AST, filepath: Path) -> None:
    """Convert the given AST back to source code and write it into the given file."""
    contents: str = ast.unparse(ast.fix_missing_locations(tree))
    filepath.write_text(contents, encoding="utf-8")


def exce_ast(tree: ast.AST) -> None:
    """Compile and excecute the given AST."""
    src: str = ast.unparse(ast.fix_missing_locations(tree))
    exec(src, {"__name__": "__main__"})  # noqa: S102 # pylint: disable=W0122 # nosec
