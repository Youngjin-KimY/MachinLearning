import tensorflow as tf

tf.set_random_seed(777)

# x_train = [1,2,3]
# y_train = [1,2,3]

X = tf.placeholder(tf.float32,shape = [None],name="X")
Y = tf.placeholder(tf.float32,shape = [None],name="Y")

w = tf.Variable(tf.random_normal([1]),name="weight")
b = tf.Variable(tf.random_normal([1]),name="bias")

hypothesis = X*w+b

cost = tf.reduce_mean(tf.square(hypothesis-Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

#name of graph
train = optimizer.minimize(cost)

#declaring session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#summary
h_hist = tf.summary.scalar('hypothesis',hypothesis)
cost_hist = tf.summary.scalar('cost',cost)
# optimizer_hist = tf.summary.scalar('opt',optimizer)

merge = tf.summary.merge_all()


writer = tf.summary.FileWriter('./board/sample_3',sess.graph)

#training
for step in range(5000):
    cost_val,W_val,b_val,_=\
    sess.run([cost,w,b,train],
             feed_dict={X:[1,2,3,4,5,6,7,8,9,10,11,12,13],Y:[2,4,6,8,10,12,14,16,18,20,22,24,26]})

    if step%20==0:
        print(step,cost_val,W_val,b_val)
        # print("hello")
        # writer.add_summary(summary,step)

print(sess.run(hypothesis,feed_dict={X:[10]}))

# for step in range(10000):
#     sess.run(train)
#     if step%20==0:
#         print(step,sess.run(cost),sess.run(w),sess.run(b))
