#!/usr/bin/env python3

"""Functions which print and analyze computed results."""

import numpy


def print_results(neighbors, words, out_file):
    """
    Prints the computed results to an output file.

    neighbors - A list of lists containing the neighbors of each word.
    words - The full list of words.
    out_file - The file on which the results will be written.
    """

    nwords = len(neighbors)

    for i, neighbors_i in enumerate(neighbors):
        out_file.write("%s: " % words[i])
        out_file.write(" ".join(sorted([words[j] for j in neighbors_i])))
        out_file.write("\n")
    out_file.write("\n")


def print_stats(neighbors, min_wlen, max_dist, stats_file):
    """
    Analyzes and prints basic statistics about the results obtained.

    neighbors - A list of lists containing the neighbors of each word.
    min_wlen - The smallest word length considered (smaller words are ignored).
    max_dist - The maximum considered distance between words.
    stats_file - The file on which the statistics data will be written.
    """

    nwords = len(neighbors)

    # counters contain the number of neighbors for each word
    counters = numpy.array([len(x) for x in neighbors], dtype=numpy.int8)

    stats_file.write("Number of words analyzed: %d\n" % nwords)
    stats_file.write("Smallest word length considered: %d\n" % min_wlen)
    stats_file.write(
        "Number of words within distance %d from any word\n" % max_dist)
    stats_file.write("\tmean    : %f\n" % numpy.mean(counters))
    stats_file.write("\tstd.dev.: %f\n\n" % numpy.std(counters))


def print_histogram(neighbors, plot_hist, hist_file):
    """
    Writes all histogram data (neighbor counter frequency) to a file.

    neighbors - A list of lists containing the neighbors of each word.
    plot_hist - True if the final histogram should be plotted, False otherwise.
    hist_file - The file on which the histogram data will be written.
    """

    nwords = len(neighbors)

    # counters contain the number of neighbors for each word
    counters = numpy.array([len(x) for x in neighbors], dtype=numpy.int8)

    # we need at least one bin (otherwise an exception will be thrown)
    nbins = max(1, max(counters) - min(counters))

    hist, bins = numpy.histogram(counters, bins=nbins, density=True)

    for x, y in zip(bins, hist):
        hist_file.write("%d %f\n" % (x, y))

    if plot_hist:
        import matplotlib.pyplot as pyplot

        width = 0.7 * (bins[1] - bins[0])
        center = (bins[:-1] + bins[1:]) / 2 - 0.5
        pyplot.bar(center, hist, align="center", width=width)
        pyplot.show()
