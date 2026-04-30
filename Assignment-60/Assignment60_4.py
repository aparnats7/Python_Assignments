# Weight and Bias Update in a Neuron

def predict(x, w, b):
    return x * w + b

def update_weight(x, w, b, y, lr):
    y_pred = predict(x, w, b)
    error = y_pred - y
    w_new = w - lr * error * x
    b_new = b - lr * error
    print("Old Weight:", w)
    print("Updated Weight:", w_new)
    print("Old Bias:", b)
    print("Updated Bias:", b_new)

def main():
    x = 2
    w = 0.5
    b = 0.1
    y = 1
    lr = 0.01

    update_weight(x, w, b, y, lr)

if __name__ == "__main__":
    main()