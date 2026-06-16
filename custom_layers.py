import tensorflow as tf

class Sampling(tf.keras.layers.Layer):
    def call(self, inputs):
        z_mean, z_log_var = inputs
        batch = tf.shape(z_mean)[0]
        dim = tf.shape(z_mean)[1]

        # Cast everything to float32 for stability
        z_mean = tf.cast(z_mean, tf.float32)
        z_log_var = tf.cast(z_log_var, tf.float32)

        # Explicit clipping
        z_log_var = tf.clip_by_value(z_log_var, -5.0, 5.0)

        # Safer sampling
        epsilon = tf.random.normal(shape=(batch, dim), dtype=tf.float32)
        sample = z_mean + tf.exp(0.5 * z_log_var) * epsilon

        # Final check
        return tf.debugging.check_numerics(sample, "NaN in sampling output")