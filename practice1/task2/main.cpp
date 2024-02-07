#include <iostream>
#include <cmath>


class Equation {
private:
    int32_t argX;
    int32_t argY;

public:
    Equation(int32_t x, int32_t y) {
        this->argX = x;
        this->argY = y;
    }

    void setArgX(int32_t x) {
        this->argX = x;
    }
    
    void setArgY(int32_t y) {
        this->argY = y;
    }

    int32_t getArgX() {
        return this->argX;
    }

    int32_t getArgY() {
        return this->argY;
    }

    int32_t calculate() {
        return 7*this->argX - 2*this->argX + 3*pow(this->argY, 2);
    }

    ~Equation() {}
};


int main(int agrc, char* argv[]) {

    int32_t x, y;
    x = y = 0;

    x = std::atoi(argv[1]);
    y = std::atoi(argv[2]);
    
    Equation A(x, y);
    
    std::cout << A.calculate() << std::endl;
    
    return 0;
}