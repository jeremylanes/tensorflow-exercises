import keras
import numpy as np

model = keras.Sequential(
    [
        keras.layers.Dense(
        units=1,
        input_shape=[1]
        )
    ]
)

model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array(
    [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0],
    dtype=float
)

ys = np.array(
    [-2.0, 1.0, 4.0, 7.0, 10.0, 13.0],
    dtype=float
)

model.fit(xs, ys, epochs=500)

prediction = model.predict(
    np.array([10.0])
)

print(prediction)