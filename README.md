# MachinLearning

## Basic ML contents
1. Hypothesis<br>
-> this is what we expect, means that we expect graph will be... and also we don't know real one yet.

2. cost function<br>
-> this is difference between H(x) and Real(X), we have to decreasse this difference

3. gradient descent<br>
-> 1,2 is in the case of linear regression, we can make shape of cost function and gradient descent algorithm can find the optimizing position by diffenretiating postion and moving left and right.


## Classification
1. binary classification<br>
-> classify the some set by 1 or 0.

2. cost function<br>
-> shape of cost function is not smooth, so we cannot use above way of gradient descent algorithm.<br>
-> graph of cost function has local minima.<br>
: we use new cost function<br>
<br>
if y = 1 -> cost(w) = -log(h(x))<br>
if y = 0 -> cost(w) = -log(1-h(x))<br>

3. gradient descent
-> like first case, we can adapt gradient descent
