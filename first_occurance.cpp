#include <iostream>
using namespace std;

int first_occorance(int arr[], int n, int key)
{
    int s = 0;
    int e = n - 1;
    int ans = -1; // Initialize as -1 to indicate the element is not found

    while (s <= e)
    {
        int mid = s + (e - s) / 2;
        if (arr[mid] == key)
        {
            ans = mid;
            e = mid - 1; // Continue searching on the left side
        }
        else if (arr[mid] > key)
        {
            e = mid - 1;
        }
        else
        {
            s = mid + 1;
        }
    }
    return ans;
}

int last_occorance(int arr[], int n, int key)
{
    int s = 0;
    int e = n - 1;
    int ans = -1;\

    while (s <= e)
    {
        int mid = s + (e - s) / 2;
        if (arr[mid] == key)
        {
            ans = mid;
            s = mid + 1;
        }
        else if (arr[mid] > key)
        {
            e = mid - 1;
        }
        else
        {
            s = mid + 1;
        }
    }
    return ans;
}

int main()
{
    int arr[5] = {1, 2, 2, 2, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 2;

    int ans = first_occorance(arr, n, key);
    int ans_1 = last_occorance(arr, n, key);

    cout << "The first occurrence of the key is: " << ans << endl;
    cout << "The last occurrence of the key is: " << ans_1 << endl;

    return 0;
}
