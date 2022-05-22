import java.util.Scanner;

class ReverseArray {
    static int MAX = 10;

    static void Reverse(int array[], int start, int end, int n) {
        int temp;
        while (start < end) {
            temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
        for (int i = 0; i < n; i++) {
            System.out.println(array[i]);
        }
        System.out.println();
    }

    public static void main(String[] arg) {
        int array[] = new int[MAX];
        Scanner input = new Scanner(System.in);
        System.out.println("Enter Total Number of Elements to be Entered: ");
        int n = input.nextInt();
        System.out.println("Enter Elements which is to be Reversed:  ");
        for (int i = 0; i < n; i++) {
            array[i] = input.nextInt();
        }
        int start = 0;
        int size = n - 1;
        Reverse(array, start, size, n);
        input.close();
    }
}
