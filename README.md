<h1><a href="https://adventofcode.com/2015">Advent of Code Python Challenges</a></h1>

<p>This is a small collection of python challenges I completed from the 2015 Advent of Code.</p>

<h2><a href="https://adventofcode.com/2015/day/3">Day 3 - Part 1</a></h2>

<p align="center"><img src="https://i.imgur.com/Sjb0HQS.png" alt="Day 3 Challenge Prompt" width="95%"></p>

<img src="https://i.imgur.com/aq5Kida.png" alt="Day 3 Part 1 Solution" width = 30% align="right">
<h3>Solution</h3>
<p>  My approach to this problem was to create an array of houses that had been visted then check if the new house was in the array or not. I started by creating the array with the coordiate of the first house "0,0" and two integers measuring the y-corodinate (NS) and the x-cordinate (EW). Then for each direction I changed the NS or EW integres by 1 or -1. I used this new co-ordinate to check if it was within the houses array already. If not, it is appended to the array. After all the directions are processed, I counted the elements in the houses array to get the number of unique houses visted, giving the correct answer of 2081.</p>
<br>

<h4><a href="https://github.com/LizziBeth7/PythonChallenges/blob/main/Day3_Inputs.txt">Input Directions</a></h4>
<h4><a href="https://github.com/LizziBeth7/PythonChallenges/blob/main/Day3_Part1.py">Part 1 Solution Code</a></h4>

<br clear="right"/>


<h2><a href="https://adventofcode.com/2015/day/3">Day 3 - Part 2</a></h2>
<p align="center"><img src="https://i.imgur.com/IktVLXH.png" alt="Day 3 Part 2 Challenge Prompt" width="95%"></p>

<h3>Solution</h3>

<img src="https://i.imgur.com/rFzstfT.png" alt="Day 3 Part 2 Solution Img2" width = 30% align="right">
<img src="https://i.imgur.com/VH3nwOk.png" alt="Day 3 Part 2 Solution Img1" width = 30% align="right">
<p>The second part of the problem I approached much like the first, except I had two co-ordinate varibles to keep track of where each santa was. I also used an integer to track whose turn it was to move then canged co-ordinated and counted up the final houses in the same way as part one. This gave me the correct result of 2341.</p>
<br>

<h4><a href="https://github.com/LizziBeth7/PythonChallenges/blob/main/Day3_Inputs.txt">Input Directions</a></h4>
<h4><a href="https://github.com/LizziBeth7/PythonChallenges/blob/main/Day3_Part2.py">Part 2 Solution Code</a></h4>

