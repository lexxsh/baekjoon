#include <iostream>
#include <vector>
using namespace std;

struct Substance {
    int index;
    int weight;
    int volume;
    double density() const {
        return static_cast<double>(weight) / volume;
    }
};

bool compare(const Substance& a, const Substance& b) {
    double densityA = a.density();
    double densityB = b.density();
    if (densityA > densityB) return true;
    if (densityA < densityB) return false;
    if (a.weight > b.weight) return true;
    if (a.weight < b.weight) return false;
    return a.index < b.index;
}

int main() {
    int n;
    cin >> n;

    vector<Substance> substances(n);

    for (int i = 0; i < n; ++i) {
        cin >> substances[i].weight >> substances[i].volume;
        substances[i].index = i;
    }

    Substance bestSubstance = substances[0];

    for (int i = 1; i < n; ++i) {
        if (compare(substances[i], bestSubstance)) {
            bestSubstance = substances[i];
        }
    }

    cout << bestSubstance.index+1 << endl;

    return 0;
}
