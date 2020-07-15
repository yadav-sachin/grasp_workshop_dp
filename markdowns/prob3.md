<p>You are given an array (<b>A<sub>1</sub></b>, <b>A<sub>2</sub></b>, ..., <b>A<sub>N</sub></b>), with size <b>N</b> initially.</p>       
   
<p>We can perform an operation on this array, that for i ≥ 1, if <b>A<sub>i</sub></b> and <b>A<sub>i+1</sub></b> are positive ( strictly greater than zero ), and <b>A<sub>i+2</sub></b> exists, then we can decrease both <b>A<sub>i</sub></b>, and <b>A<sub>i+1</sub></b> by one and increase <b>A<sub>i+2</sub></b> by one. </p>

<p>In case the <b>A<sub>i+2</sub></b> doesn't exist, but  <b>A<sub>i</sub></b> and <b>A<sub>i+1</sub></b> are positive, then we can decrease both <b>A<sub>i</sub></b>, and <b>A<sub>i+1</sub></b> ( last two elements of the current array ) by one. But here a new element with value 1 will be added at the end.</p>

<p>Given the original array <b>A</b>, find the number of different arrays which can be generated.The operationcan be performed any number of times. Output the answer in  modulo 10<sup>9</sup>+7.</p>

<p>Two arrays are same if their size is same and all the corresponding elements are same.</p>

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
