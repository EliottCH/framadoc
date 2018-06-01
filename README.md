# Frama-c documentation tool

[Frama-c](https://frama-c.com/) is a Framework dedicated to formal methods applied to C code. Framadoc is a short python script that generates html documentation of a C project with ACSL specifications. There are several rules to be respected so that the tool can be used properly (see below).

## List of rules to be respected:

1. fonction contract must be put 5 lines before the function signature (with nothing between '*/' and the signature).
2. paths must be specified inside the two config files 'includes' and 'sources' using '/' and not '\'
