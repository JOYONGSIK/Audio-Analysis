from keras import models, layers

model = models.Sequential()
model.add(layers.Dense(256, activation='relu', input_shape=(....shape[1],)))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(... ,
                    ... ,
                    epochs=20,
                    batch_size=128)

test_loss, test_acc = model.evaluate(... , ...)