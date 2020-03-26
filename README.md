# gobblet

 The goal is to show that 3X3 gobblet is dominated by the first mover.

 If we can write an engine that plays the "optimal" strategy perhaps we can prove that there
 is a dominant strategy.

 I feel confident that such a strategt exists; I've been unable to prove it manuelly hence this
 library.

 Initial thoughts are to generate a trie of all the reasonable games (like not making moves that
 will lose you the game on the next move). Each node has a value assosicated with it.

 How to compute the value?
  1. the number of winning branches under the node?
  2. the percentage of winning branches under the node 
