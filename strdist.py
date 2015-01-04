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


"""Functions which compute distances between strings"""

import numpy


def levenshtein(s,t):
	"""
	Returns the Levenshtein distance between s and t.

	Examples:

	>>> levenshtein("kitten", "sitting")
	3
	>>> levenshtein("book", "back")
	2
	>>> levenshtein("testing", "waiting")
	3
	>>> levenshtein("", "word")
	4
	>>> levenshtein("word", "word")
	0
	"""

	# the implementation below is not the most memory efficient but is very
	# easy to understand and good enough for strings which are words of
	# a language (i.e. not so large)

	m,n = len(s),len(t)

	# D[i,j] will hold the Levenshtein distance between s[:i] and t[:j];
	D = numpy.array(numpy.zeros((m+1,n+1)), dtype=numpy.int8)

	D[0,:] = numpy.arange(n+1)
	D[:,0] = numpy.arange(m+1)

	for i in numpy.arange(1,m+1):
		for j in numpy.arange(1,n+1):
			if s[i-1] == t[j-1]:
				# characters match, nothing needs to be done
				D[i,j] = D[i-1,j-1]
			else:
				# consider deletion, insertion, substitution
				D[i,j] = min(D[i-1,j] + 1, D[i,j-1] + 1, D[i-1,j-1]+1)

	return D[m,n]


def hamming(s,t):
	"""
	Returns the Hamming distance between s and t. If len(s) != len(t),
	the distance between s[0:M] and t[0:M] is returned, where
	M = min(len(s),len(t)).

	Example:

	>>> hamming("chess", "check")
	2
	>>> hamming("participate", "collaborate")
	8
	>>> hamming("history", "mistery")
	2
	>>> hamming("function", "functionality")
	0
	"""

	if len(s) != len(t):
		M = min(len(s), len(t))
		return hamming(s[0:M], t[0:M])
	else:
		return sum(ch1 != ch2 for ch1,ch2 in zip(s,t))
