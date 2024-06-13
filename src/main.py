from calculator import Calculator

def main():
    calculator = Calculator()
    print(calculator.add(2, 3))  # 5
    print(calculator.subtract(5, 2))  # 3
    print(calculator.multiply(4, 5))  # 20
    print(calculator.divide(10, 2))  # 5.0

if __name__ == "__main__":
    main()