# Soundex
soundex algorithm python

<p>Soundex is a phonetic algorithm for indexing names by sound, as pronounced in English. The goal is for homophones to be encoded to the same representation so that they can be matched despite minor differences in spelling. The algorithm mainly encodes consonants; a vowel will not be encoded unless it is the first letter. Soundex is the most widely known of all phonetic algorithms Improvements to Soundex are the basis for many modern phonetic algorithms.</p>

<h4>Algorithm</h4>
<ul>
  <li>Retain the first letter of the term.</li>
  <li>Change all occurrences of the following letters to ’0’ (zero): A, E, I, O, U, H, W, Y</li>
  <li>Change letters to digits as follows : B, F, P, V to 1</li>
  <ul>
    <ol>hello</ol>
  </ul>
  <li>C, G, J, K, Q, S, X, Z to 2</li>
  <li>D,T to 3</li>
  <li>L to 4</li>
  <li>M, N to 5</li>
  <li>R to 6</li>
  <li>Repeatedly remove one out of each pair of consecutive identical digits</li>
  <li>Remove all zeros from the resulting string; pad the resulting string
     with trailing zeros and return the first four positions, which will
     consist of a letter followed by three digits</li>
</ul>

<p>* Using this algorithm, both "Robert" and "Rupert" return the same string "R163" while "Rubin" yields "R150".</p>










     
