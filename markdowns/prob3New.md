<p>Given an array <b>A</b> = (<b>A<sub>1</sub></b>, <b>A<sub>2</sub></b>, ..., <b>A<sub>N</sub></b>),you can select any two <b>consecutive</b> positive elements from the array and decrease them by one and also, increase  element next to these consecutive elements by one. if both elements are last two elements then chef adds new element to array with value one.chef can perform this operation as many times as he wishes.chef wants to know the number of different arrays possible by performing this operation multiple times. </p> 

<p>
For example,

For array <b>(2,3,1)</b>, if chef chooses first 2 positive elements and perform one operation then modified array will be <b>(1,2,2)</b>.if he chooses last two positive elements and perform one operation then modified array will be <b>(2,2,0,1)</b>.
</p>

<p>  you have to count the number of different possible arrays in the answer.since answer can be large,just print answer modulo <b>1000000007</b> in the output.
</p>


<p>Two arrays are same if they have the same number of elements and if each corresponding element is the same. For example arrays <b>(2,1,1)</b> and <b>(1,1,2)</b> are different. 
</p>

<h3>Input</h3>
<ul>
<li>The first line of the input contains a single integer <b>T</b> denoting the number of test cases.</li>
<li>The first line contains a single integer <b>N</b> denoting the initial number of elements in <b>A</b>.</li>
<li>The second line contains <b>N</b> space-separated integers: <b>A<sub>1</sub></b>, <b>A<sub>2</sub></b>, ... , <b>A<sub>N</sub></b>. </li>
</ul>

<h3>Output</h3>
<p>For each test case, output answer modulo 10<sup>9</sup>+7 in a single line. </p>


<h3>Constraints</h3>
<ul>
<li>1 ≤ <b>T</b> ≤ 5</li>
<li>1 ≤ <b>N</b> ≤ 50</li>
<li>0 ≤ <b>A<sub>i</sub></b> ≤ 50</li>
</ul>

<h3>Subtasks</h3>
<ul>
<li><b>Subtask 1</b> (20 points) : 1 ≤ <b>N</b> ≤ 8, 0 ≤ <b>A<sub>i</sub></b> ≤ 4</li>
<li><b>Subtask 2</b> (80 points) : Original constraints</li>
</ul>

<h3>Example</h3>
<pre><b>Input:</b>
3
3
2 3 1
2
2 2
3
1 2 3

<b>Output:</b>
9
4
9
</pre>

<h3>Explanation</h3>
<p><b>Example case 1.</b></p>
<p>We'll list the various single steps that you can take (ie. in one single usage of the operation):</p>
<ul>
<li>(2, 3, 1) → (2, 2, 0, 1)</li>
<li>(2, 2, 0, 1) → (1, 1, 1, 1)</li>
<li>(1, 1, 1, 1) → (1, 1, 0, 0, 1)</li>
<li>(1, 1, 0, 0, 1) → (0, 0, 1, 0, 1)</li>
<li>(1, 1, 1, 1) → (1, 0, 0, 2)</li>
<li>(1, 1, 1, 1) → (0, 0, 2, 1)</li>
<li>(2, 3, 1) → (1, 2, 2)</li>
<li>(1, 2, 2) → (0, 1, 3)</li>
</ul>
<p></p>
<p>So all the arrays you can possibly get are: </p>
<p>(2, 3, 1), (2, 2, 0, 1), (1, 1, 1, 1), (1, 1, 0, 0, 1), (0, 0, 1, 0, 1), (1, 0, 0, 2), (0, 0, 2, 1), (1, 2, 2), and (0, 1, 3)</p>
<p>Since there are 9 different arrays that you can reach, the answer is 9.</p>