#include <iostream>


class Rectangle {
private:
    int32_t width;
    int32_t height;

public:
    Rectangle() {
        this->height = this->width = 0;
    }

    Rectangle(int height, int width) {
        this->height = height;
        this->width = width;
    }

    Rectangle(int side) {
        this->height = this->width = side;
    }

    void setHeight(int32_t height) {
        this->height = height;
    }

    void setWidth(int32_t width) {
        this->width = width;
    }

    void setSide(int32_t side) {
        this->width = this->height = side;
    }

    int32_t getHeight() {
        return this->height;
    }

    int32_t getWidth() {
        return this->width;
    }

    int32_t square() {
        return this->height * this->width;
    }

    int32_t perimeter() {
        return 2 * (this->height + this->width);
    }

    bool isSquare() {
        if (this->height == this->width)
            return true;
        return false;
    }

    bool isRectangle() {
        if (this->height == this->width)
            return false;
        return true;
    }

    ~Rectangle() {}
};


int main(int argc, char* argv[]) {

    int32_t heightArg, widhtArg;
    heightArg = widhtArg = 0;

    heightArg = std::atoi(argv[1]);

    if (argc > 2) {
        widhtArg = std::atoi(argv[2]);
    } else {
        widhtArg = heightArg;
    }

    Rectangle A(heightArg, widhtArg);

    std::cout << /*"square: " <<*/ A.square() << std::endl;
    std::cout << /*"perimeter: " <<*/ A.perimeter() << std::endl;

    return 0;
}