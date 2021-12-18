int f(int a){
    int b = 1;
    a = a + b;
    b = b * a;
    f(a+1);
    return a+1;
}

int g(int a, double b){
    return a;
}

int main(){
    int d = 1;
    f(d);
    double b = 0.0;
    g(d,b);
    return 0;
}