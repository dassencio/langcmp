################################################################################
#
#    Copyright (c) 2015, Diego Assencio (http://diego.assencio.com)
#    All rights reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################


import sys
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
