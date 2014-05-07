#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import strdist


##
# @brief computes distances between words
# @param distmap dictionary: (i,j) --> dist(i,j) where i and j are word indices
# @param words full list of words
# @param i_min/i_max indices defining the words for which distances will be computed
# @param max_dist maximum distance between words to consider
# @param counter global counter which will hold the number of words processed
#
def compute_distances(distmap, words, i_min, i_max, max_dist, counter):

	for i in range(i_min, i_max):
		for j in range(i+1, len(words)):
			if abs(len(words[i]) - len(words[j])) <= max_dist:
				d_ij = strdist.levenshtein(words[i],words[j])
				if d_ij <= max_dist:
					distmap[i,j] = d_ij
					distmap[j,i] = d_ij
		counter.value += 1


##
# @brief shows the progress of the computing subprocesses
# @param counter global number of words processed so far
# @param nwords total number of words which must be processed
#
def show_progress(counter, nwords):

	start = time.time()
	prev_progress = 0.0
	while True:
		progress = float(counter.value) / float(nwords)
		if progress - prev_progress >= 0.0001:
			now = time.time()
			# etc: estimated time to completion (in seconds)
			etc = (now - start) * (1 - progress) / progress
			etc_m, etc_s = divmod(etc, 60)
			etc_h, etc_m = divmod(etc_m, 60)
			sys.stderr.write("progress: %6.2f%%   time left: %02d:%02d:%02d\n" % (
						100*progress, etc_h, etc_m, etc_s
					))
			prev_progress = progress
			if counter.value == nwords: break
			time.sleep(1)
