<h1><a href="https://adventofcode.com/2015">Advent of Code Python Challenges</a></h1>

<p>This is a small collection of python challenges I completed from the 2015 Advent of Code.</p>

<h2><a href="https://adventofcode.com/2015/day/3">Day 3 - Part 1</a></h2>

<p align="center"><img src="https://i.imgur.com/Sjb0HQS.png" alt="Day 3 Challenge Prompt" width="95%"></p>

<img src="https://i.imgur.com/aq5Kida.png" alt="Day 3 Part 1 Solution" width = 30% align="right">
<h3>Solution</h3>
<p>My approach to this problem was to create an array of houses that had been visted then check if the new house was in the array or not. I started by creating the array with the coordiate of the first house "0,0" and two integers measuring the y-corodinate (NS) and the x-cordinate (EW). Then for each direction I changed the NS or EW integres by 1 or -1. I used this new co-ordinate to check if it was within the houses array already. If not, it is appended to the array. After all the directions are processed, I counted the elements in the houses array to get the number of unique houses visted, giving the correct answer of 2081.</p>
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

<br clear="right"/>

<h2>Day 5 - Part 1</h2>
<p align="center"><img src="https://i.imgur.com/fOUlARl.png" alt="Day 5 Part 1 description img" width="95%"></p>

<h3>Solution</h3>

<img src="https://i.imgur.com/UhJnMNs.png" alt="Day 5 Part 1 solution img" width="50%" align="right">
<p>The first step in solving this challenge was to split the input into seperate strings so each one could be tested. Then I created varibles for the substrings to check if any were contained within the string being checked. Then I created a for loop to go through each letter of the current string and count the number of vowels. Within this loop I also created a varible to remember the previous letter of the string. This allowed me to check if it was the same as the current letter (checking if two letters next to each other were the same). Finally if the string contained none of the substrings, at least 3 vowels and a double letter it was added to the count of nice letters. This repeated until all strings from the input were checked giving a correct final answer of 236 nice strings.</p>

<br>

<h4><a href="https://github.com/LizziBeth7/PythonChallenges/blob/main/Day3_Inputs.txt">Input Directions</a></h4>
<h4><a href="https://github.com/LizziBeth7/PythonChallenges/blob/main/Day3_Part2.py">Part 1 Solution Code</a></h4>

<br clear="right"/>

<h2>Day 5 - Part 2</h2>
<p align="center"><img src="https://i.imgur.com/4l170kT.png" alt="Day 5 Part 2 description img" width="95%"></p>

<h3>Solution</h3>

<img src="https://i.imgur.com/7XuX4QL.png" alt="Day 5 Part 2 solution img" width="60%" align="right">
<p>I began this problem by creating a varible to store the current letter, previous letter and the second last letter(two letters ago). I then created a loop that created a pair of every two letters (current and previous) then checked if it matched a perious pair by comparing it to every element in the doublestore array. If it did then it aws a repeated pair and therefore the first condition of the problem was true but if it didn't then it was appended to the doublestore array so it could be compared to later pairs. While looping through each letter I then checked if it matched the letter from two letters ago. If it did that would make the second condition true. Then once each letter in the string was checked I tested if both conditions were true and then added to the nice string count if they were. This resulted in the correct amount of 51 nice strings.</p>

<br>

<h4><a href="">Input Directions</a></h4>
<h4><a href="">Part 2 Solution Code</a></h4>

<br clear="right"/>

    

