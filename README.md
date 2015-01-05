langcmp
=======

Langcmp is a language comparison tool. It computes the Levenshtein distances
between the words contained in an input file and outputs, for each considered
input word, a list of words containing its "closest" words. If the contents
of the input file represent the most commonly used words of a language, the
results will indicate how similar the words of this language are (only written
form is taken into consideration; langcmp does not deal with word pronunciation).


Required Libraries
==================

The following python libraries are used:

    - numpy
    - matplotlib

On Ubuntu/Debian, you can install these libraries with:

	sudo apt-get install python3-numpy python3-matplotlib


Subprocesses
============

Langcmp can break the computing work into subprocesses to reduce the overall
computation time. I recommend you try using different numbers of subprocesses
to find out an optimal value for your device (suggestion: try first using the
number of CPU cores available).


Histogram
=========

After computing all necessary Levenshtein distances, langcmp generates a
histogram showing the fraction of the total number of words versus the number
of detected words within distance d.


Usage
=====

The example command below shows most options from langcmp. It instructs langcmp
to run 3 subprocesses, to consider only words in the input file (words.txt)
which are at least 5 characters long and to only consider pairs of words which
are no farther (in distance) than 2 edits from each other:

	./langcmp -v -n 3 -l 5 -d 2 -i words.txt -o results.txt -s stats.txt -g histogram.txt

Above -n (--num-subproc) specifies the number of subprocesses, -l (--min-length)
specifies the minimum length a word must have to be analyzed and -d (--max-distance)
specifies the maximum Levenshtein distance which will be accepted in the analysis
(pairs of words whose Levenshtein distances are larger than this specified value
will not be considered). The results will be written on results.txt, the
computed statistics on stats.txt and the histogram data on histogram.txt.

If you need help, run './langcmp -h'.


Included word lists
===================

Langcmp already comes with the following word lists (in the wordlists directory):

- 100 most commonly used English/German/French/Dutch words
- 1000 most commonly used English/German/French/Dutch words
- 10000 most commonly used English/German/French/Dutch words

These lists were obtaind from the website of the University of Leipzig, Germany
(http://www.wortschatz.uni-leipzig.de/html/wliste.html).

Contributors & Contact Information
==================================

Diego Assencio / diego@assencio.com

