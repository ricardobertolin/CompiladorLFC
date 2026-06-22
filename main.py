#!/usr/bin/env python3
"""
main.py  –  CompiladorLFC entry point
======================================
Compiles an LFC source file through four stages and prints ATmega2560 assembly.

Usage
-----
    python main.py <source.txt>            # compile and print assembly
    python main.py <source.txt> --ast      # print AST and stop
    python main.py <source.txt> --no-asm   # semantic check only
    python main.py <source.txt> -o out.asm # write assembly to file

Stages
------
1. Lexical + syntactic analysis  (ANTLR4: CompiladorLexer / CompiladorParser)
2. AST construction              (CompiladorVisitor)
3. Semantic analysis             (CompiladorSemantico)
4. Code generation               (AsmGenerator)
"""

import sys
import argparse

from antlr4 import FileStream, CommonTokenStream

from CompiladorLexer    import CompiladorLexer
from CompiladorParser   import CompiladorParser
from CompiladorVisitor  import CompiladorVisitor
from CompiladorSemantico import CompiladorSemantico
from AsmGenerator       import AsmGenerator


def main():
    ap = argparse.ArgumentParser(
        description='CompiladorLFC – Arduino/ATmega2560 language compiler')
    ap.add_argument('source',   help='Source file (.txt)')
    ap.add_argument('--ast',    action='store_true',
                    help='Print the AST (as JSON) and stop')
    ap.add_argument('--no-asm', action='store_true',
                    help='Run semantic analysis only (no code generation)')
    ap.add_argument('-o', '--output', metavar='FILE',
                    help='Write assembly to FILE instead of stdout')
    args = ap.parse_args()

    # ── Stage 1: Lex + Parse ─────────────────────────────────────────────────
    try:
        stream = FileStream(args.source, encoding='utf-8')
    except OSError as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)

    lexer  = CompiladorLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = CompiladorParser(tokens)
    tree   = parser.prog()

    n_syntax = parser.getNumberOfSyntaxErrors()
    if n_syntax:
        print(f'{n_syntax} syntax error(s) found. Aborting.', file=sys.stderr)
        sys.exit(1)

    # ── Stage 2: Build AST ───────────────────────────────────────────────────
    visitor = CompiladorVisitor()
    ast = visitor.visit(tree)

    if args.ast:
        import json
        print(json.dumps(ast, indent=2, default=str))
        return

    # ── Stage 3: Semantic analysis ───────────────────────────────────────────
    analyzer = CompiladorSemantico()
    errors   = analyzer.analyze(ast)

    if errors:
        for err in errors:
            print(f'Semantic error: {err}', file=sys.stderr)
        print(f'{len(errors)} semantic error(s). Aborting.', file=sys.stderr)
        sys.exit(1)

    if args.no_asm:
        print('Semantic analysis passed. No errors.')
        return

    # ── Stage 4: Code generation ─────────────────────────────────────────────
    gen = AsmGenerator()
    asm = gen.generate(ast)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(asm)
            print(f'Assembly written to {args.output}')
        except OSError as e:
            print(f'Error writing output: {e}', file=sys.stderr)
            sys.exit(1)
    else:
        print(asm)


if __name__ == '__main__':
    main()
