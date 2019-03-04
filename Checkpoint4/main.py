import Traffic

def main():
    test = Traffic.Traffic(0.3,5)
    test.update()
    test.plotMovement()
    for x in test.avgSpeeds:
        print(x)
if __name__ == "__main__":
    main()