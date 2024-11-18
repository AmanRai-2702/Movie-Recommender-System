import pyautogui
import time
time.sleep(60)
test1 = '''
#include <iostream>
using namespace std;

bool isPrime(int num) {
if (num <= 1)
return false;
for (int i = 2; i * i <= num; i++) {
if (num % i == 0)
return false;
}
return true;
}

int main() {
int n;
cin >> n;

int primeCount = 0;
for (int i = 2; i <= n; i++) {
if (isPrime(i))
primeCount++;
}

int* primes = new int[primeCount];
int index = 0;

for (int i = 2; i <= n; i++) {
if (isPrime(i)) {
primes[index++] = i;
}
}

for (int i = 0; i < primeCount; i++) {
cout << primes[i] << " ";
}
cout << endl;

delete[] primes;

return 0;
}
'''

test2 = '''
#include <iostream>
#include <string>
using namespace std;

// Structure for Loan Record
struct LoanRecord {
int id;                      // Unique ID
string name;                 // Name of the borrower
int amount;                  // Loan amount
LoanRecord* next;            // Pointer to the next record
};

// Class Loan to manage loan records
class Loan {
private:
LoanRecord* head;            // Pointer to the first loan record
int idCounter;               // Counter to generate unique IDs

public:
// Constructor
Loan() : head(nullptr), idCounter(1) {}

// Method to insert a new Loan Record
void insertLoanRecord(const string& name, int amount) {
// Create a new LoanRecord
LoanRecord* newRecord = new LoanRecord();
newRecord->id = idCounter++;
newRecord->name = name;
newRecord->amount = amount;
newRecord->next = nullptr;

// Insert the new record at the end of the list
if (head == nullptr) {
head = newRecord;
} else {
LoanRecord* temp = head;
while (temp->next != nullptr) {
temp = temp->next;
}
temp->next = newRecord;
}
}

// Method to display all loan records
void displayList() const {
LoanRecord* temp = head;
while (temp != nullptr) {
cout << temp->name << " " << temp->amount << endl;
temp = temp->next;
}
}

// Method to calculate the total loan amount
int getTotalLoanAmount() const {
int total = 0;
LoanRecord* temp = head;
while (temp != nullptr) {
total += temp->amount;
temp = temp->next;
}
return total;
}

// Destructor to clean up memory
~Loan() {
LoanRecord* temp = head;
while (temp != nullptr) {
LoanRecord* toDelete = temp;
temp = temp->next;
delete toDelete;
}
}
};

// Main function
int main() {
int n; // Number of loan records to insert
cin >> n;

Loan loanSystem; // Create a Loan system

// Input loan records
for (int i = 0; i < n; i++) {
string name;
int amount;
cin >> name >> amount;
loanSystem.insertLoanRecord(name, amount);
}

// Display all loan records
loanSystem.displayList();

// Display total loan amount
cout << "Total: " << loanSystem.getTotalLoanAmount() << endl;

return 0;
}
'''

pyautogui.write(test1)
time.sleep(35)
pyautogui.write(test2)