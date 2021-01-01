![Functional tests](https://github.com/dassencio/langcmp/workflows/Functional%20tests/badge.svg)

# Description

`langcmp` is a language comparison tool (written in Python 3) which computes the
Levenshtein distances between the words contained in an input file and outputs,
for each considered input word, a list of words containing its "closest" words.
If the contents of the input file represent the most commonly used words of a
language, the results will indicate how similar the words of this language are
(only written form is taken into consideration; `langcmp` does not deal with word
pronunciation). As an example of what it can be used for, see
[this article](http://diego.assencio.com/?index=9636c4a74afcc3924fdd2f03f83492c6).

# License

All code from this project is licensed under the GPLv3. See the
[`LICENSE`](https://github.com/dassencio/langcmp/tree/master/LICENSE)
file for more information.

# Required modules

The following modules are used:

- `numpy`
- `matplotlib`

You can install them with the following command:

    pip3 install numpy matplotlib

# Subprocesses

`langcmp` can break the computing work into subprocesses to reduce the overall
computation time. I recommend you try using different numbers of subprocesses
to find out the optimal value for your machine (suggestion: try first using the
number of CPU cores available).

# Histogram

After computing all necessary Levenshtein distances, `langcmp` generates a
histogram showing the fraction of the total number of words versus the number
of detected words within distance `d`, i.e., each column in the histogram
represents how many words in the input dictionary have `d` "closest" neighbors
in this dictionary. The more "to the left" the histogram is, the bigger
is the difference in spelling between the words in the dictionary.

# Usage instructions

The example command below shows most options from `langcmp`. It instructs `langcmp`
to run 3 subprocesses, to consider only words in the input file `words.txt`
which are at least 5 characters long and to only consider pairs of words which
are no farther (in distance) than 2 edits from each other:

    ./langcmp -v -n 3 -l 5 -d 2 -i words.txt -o results.txt -s stats.txt -g histogram.txt

Above `-n` (`--num-subproc`) specifies the number of subprocesses, `-l` (`--min-length`)
specifies the minimum length a word must have to be analyzed and `-d` (`--max-distance`)
specifies the maximum Levenshtein distance which will be accepted in the analysis
(pairs of words whose Levenshtein distances are greater than this specified value
will not be considered). The results will be written on `results.txt`, the
computed statistics on `stats.txt` and the histogram data on `histogram.txt`.

For more details on the parameters which `langcmp` can take, run `./langcmp -h`.

# Included word lists

This project already comes with the following word lists (in the `wordlists`
subdirectory):

- 100 most commonly used English/German/French/Dutch words
- 1000 most commonly used English/German/French/Dutch words
- 10000 most commonly used English/German/French/Dutch words

These lists were obtaind from the University of Leipzig, Germany.

# Contributors & contact information

Diego Assencio / diego@assencio.com
