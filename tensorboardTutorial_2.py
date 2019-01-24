import tensorflow as tf

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

add = tf.add(X,Y)
mul = tf.multiply(X,Y)

add_hist = tf.summary.scalar('add_scalar',add)
mul_hist = tf.summary.scalar('mul_scalar',mul)


merged = tf.summary.merge_all()


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter("./board/sample_2",sess.graph)

    for step in range(100):

        summary = sess.run(merged,feed_dict={X:step*10,Y:2.0})
        writer.add_summary(summary,step)