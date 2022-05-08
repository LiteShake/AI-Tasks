<h2>
Question 4..
</h2>
..is to create a NumPy array and store some food details and sort it accroding to rating.
<br>
<br>
My first approach is the usual <b><i>ndrray.sort()</i></b> but it seemed to sort literally everything. So I researched on It for a while and found this <b><i>ndarray.argsort()</i></b> which seems to return the indices of a sorted iterative. So I cropped the Rating column out and argsort()ed it and got the sorted indices and applied it to the entire thing and that did the trick and sorted everything according to the rating.
