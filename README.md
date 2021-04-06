# Soundex
soundex algorithm python

<p>Soundex is a phonetic algorithm for indexing names by sound, as pronounced in English. The goal is for homophones to be encoded to the same representation so that they can be matched despite minor differences in spelling. The algorithm mainly encodes consonants; a vowel will not be encoded unless it is the first letter. Soundex is the most widely known of all phonetic algorithms Improvements to Soundex are the basis for many modern phonetic algorithms.</p>

<h4>Algorithm</h4>
<p>1- Retain the first letter of the term.</p>
<p>2- Change all occurrences of the following letters to ’0’ (zero): A, E, I, O, U, H, W, Y</p>
<p>3- Change letters to digits as follows:
  B, F, P, V to 1
  C, G, J, K, Q, S, X, Z to 2
  D,T to 3
  L to 4
  M, N to 5
  R to 6</p>
<p>4- Repeatedly remove one out of each pair of consecutive identical digits</p>
<p>5- Remove all zeros from the resulting string; pad the resulting string
     with trailing zeros and return the first four positions, which will
     consist of a letter followed by three digits</p>
     
<p>* Using this algorithm, both "Robert" and "Rupert" return the same string "R163" while "Rubin" yields "R150". "Ashcraft" and "Ashcroft" both yield "A261". "Tymczak" yields "T522"          not "T520" (the chars 'z' and 'k' in the name are coded as 2 twice since a vowel lies in between them). "Pfister" yields "P236" not "P123" (the first two letters have the same     number and are coded once as 'P'), and "Honeyman" yields "H555".
     
</p>
<hr>









     
