import tensorflow as tf
c=tf.constant(1)
cluster = tf.train.ClusterSpec({"local":["localhost:2222","localhost:2223"]})
server = tf.train.Server(cluster, job_name="local",task_index=1)
with tf.Session(server.target,config=tf.ConfigProto(log_device_placement=True)) as sess:
    print(sess.run(c))
    server.join()

'''
I tensorflow/core/common_runtime/gpu/gpu_device.cc:906] DMA: 0 
I tensorflow/core/common_runtime/gpu/gpu_device.cc:916] 0:   Y 
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> 
(device: 0, name: GeForce GTX 850M, pci bus id: 0000:01:00.0)
I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:200] Initialize GrpcChannelCache for job 
local -> {0 -> localhost:2222, 1 -> localhost:2223}
I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:221] Started server with target: 
grpc://localhost:2223
I tensorflow/core/distributed_runtime/master.cc:193] CreateSession still waiting for response 
from worker: /job:local/replica:0/task:0
I tensorflow/core/distributed_runtime/master.cc:193] CreateSession still waiting for response 
from worker: /job:local/replica:0/task:0
I tensorflow/core/distributed_runtime/master.cc:193] CreateSession still waiting for response 
from worker: /job:local/replica:0/task:0
...
'''
