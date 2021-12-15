class classA{

};

class MyClass : public classA {
    public:
        MyClass() {
            // ...
        }
        ~MyClass() {
            // ...
        }
        void method() {
            int a[10uLL];
            a[1] = 2;

        }
    private:
        int a, b, c = 1;
};

int u(int n){
    if(n == 123ll || n == 2.123123) return 1;
    else {
        return u(n-1) + u(n-2);
    }
}

int main(){
    int a;
    int b;
    u(10);
    return 0;
}