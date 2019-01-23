import tensorflow as tf

tf.set_random_seed(777)

# x_train = [1,2,3]
# y_train = [1,2,3]

X = tf.placeholder(tf.float32,shape = [None])
Y = tf.placeholder(tf.float32,shape = [None])

w = tf.Variable(tf.random_normal([1]),name="weight")
b = tf.Variable(tf.random_normal([1]),name="bias")

hypothesis = X*w+b

cost = tf.reduce_mean(tf.square(hypothesis-Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

#name of graph
train = optimizer.minimize(cost)


sess = tf.Session()

sess.run(tf.global_variables_initializer())

for step in range(3020):
    cost_val,W_val,b_val,_=\
    sess.run([cost,w,b,train],
             feed_dict={X:[1,2,3,4,5],Y:[2.1,3.1,4.1,5.1,6.1]})

    if step%20==0:
        print(step,cost_val,W_val,b_val)


print(sess.run(hypothesis,feed_dict={X:[10 ]}))

# for step in range(10000):
#     sess.run(train)
#     if step%20==0:
#         print(step,sess.run(cost),sess.run(w),sess.run(b))
