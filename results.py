#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


##
# @brief prints the computed results to an output file
# @param neighbors a list such that neighbors[i] contains a list of its neighbors
#        (words within the maximum specified distance)
# @param words full list of words
# @param out_file file on which the results will be written
#
def print_results(neighbors, words, out_file):

	nwords = len(neighbors)

	for i,neighbors_i in enumerate(neighbors):
		out_file.write("%s:" % words[i])
		for j in neighbors_i:
			out_file.write(" %s" % words[j])
		out_file.write("\n")
	out_file.write("\n")


##
# @brief analyzes and prints basic statistics about the results obtained
# @param neighbors a list such that neighbors[i] contains a list of its neighbors
#        (words within the maximum specified distance)
# @param min_wlan smallest word length considered (smaller words are ignored)
# @param max_dist maximum considered distance between words
#
def print_stats(neighbors, min_wlen, max_dist):

	nwords = len(neighbors)

	counters = [len(x) for x in neighbors]
	counters_sq = [x**2 for x in counters]

	# average number of neighbors
	mean = float(sum(counters)) / float(nwords)

	# compute the standard deviation
	std_dev = math.sqrt(sum(counters_sq)/float(nwords) - mean**2)

	print "Smallest word length considered: %d" % min_wlen
	print "Number of words analyzed: %d" % nwords
	print "Number of words within distance %d from any word" % max_dist
	print "\tmean    : %f" % mean
	print "\tstd.dev.: %f" % std_dev
