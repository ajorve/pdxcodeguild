# Does not work with version Python3.6, downgrade to run program.



import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data", one_hot=True)

x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')

x_node_h1 = 500  # creates Node layer
x_node_h2 = 500
x_node_h3 = 500
n_classes = 10
batch_size = 100  # batching by 100, out of 55000


def neural_network_model(data):
    hidden_layer_1 = {'weights': tf.Variable(tf.random_normal([784, x_node_h1]),
                                             'biases': tf.Variable(tf.random_normal([x_node_h1]))
    }

    hidden_layer_2 = {'weights': tf.Variable(tf.random_normal([x_node_h1, x_node_h2]),
                                             'biases': tf.Variable(tf.random_normal([x_node_h2]))
    }

    hidden_layer_3 = {'weights': tf.Variable(tf.random_normal([x_node_h2, x_node_h3]),
                                             'biases': tf.Variable(tf.random_normal([x_node_h3]))
    }

    output_layer = {'weights': tf.Variable(tf.random_normal([x_node_h3, n_classes]),
                                           'biases': tf.Variable(tf.random_normal([n_classes]))
    }

    # (input * weights) + biases --> Activation function --> next layer


    layer_1 = tf.add(tf.matmul(data, hidden_layer_1['weights']), hidden_layer_1['biases'])
    layer_1 = tf.nn.relu(layer_1)

    layer_2 = tf.add(tf.matmul(layer_1, hidden_layer_2['weights']), hidden_layer_2['biases'])
    layer_2 = tf.nn.relu(layer_2)

    layer_3 = tf.add(tf.matmul(layer_2, hidden_layer_3['weights']), hidden_layer_3['biases'])
    layer_3 = tf.nn.relu(layer_3)

    output = tf.matmul(layer_3, output_layer['weights']) + output_layer['biases']

    return output


def train_neural_network(x):
    prediction = neural_network_model(x)

    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))

    optimizer = tf.train.AdamOptimizer().minimize(cost)

    num_epochs = 10

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for epoch in range(num_epochs):
            epoch_loss = 0

            for _ in range(int(mnist.train.num_examples/batch_size)):
                batch_x, batch_y = mnist.train.next_batch(batch_size)
                _ , c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})                      # c = current loss
                epoch_loss += c
            print('Epoch Number: ', epoch, 'completed out of: ', num_epochs, 'with a loss of: ', epoch_loss)

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))

        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print('Accuracy: ', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))

train_neural_network(x)
