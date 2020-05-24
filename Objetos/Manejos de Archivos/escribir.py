
def run():
    with open('empanadas.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))


if __name__ == "__main__":
    run()