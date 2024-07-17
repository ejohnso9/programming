
2024May18 ----------

There are severals ways to try to do substring matching.
For the Pattern: 'CTTGATCAT', the problem at:
    https://cogniterra.org/lesson/30257/step/10?thread=solutions&unit=22334
states that the pattern is found in the genome at the following indices:

hits = [60039, 98409, 129189, 152283, 152354, 152411, 163207, 197028, 200160,
    357976, 376771, 392723, 532935, 600085, 622755, 1065555]

[v] First of all, is that true?
    Check: [s[i:i+len(pattern)] for i in hits]
    [v] Yes, it's true. See: check_vib_chol_genome.py

I guess if you really want to look at all the possible substrings that
come up in a sliding window (like, you want to aggregate data), you can
proceed as the tutorial has shown.

But, if you are looking for a particular known pattern, I suspect that
str.index() may be substantially faster. Is it? How much faster?

The Vibrio_cholerae.txt file is a single string of {AGCT}*, length
1108250, no line feeds (i.e., wc -l returns 0).

You can read it like this (Python):

# you should be able to paste this block into interactive Py shell:
fname = 'Vibrio_cholera.txt'
with open(fname) as fd:
    s = fd.read()

print(f"read {len(s)} bytes from {fname}")
vibrio_cholera = s

    
