import java.util.*;

public class SortingInJava{
    
    // inversion count of an array
    public int inversionCount(int arr[]){
        int count = 0;
        for(int i = 0; i<arr.length-1; i++){
            for(int j=i; j<arr.length; j++){
                if(arr[i]>arr[j]){
                    count=count+1;
                }
            }
        }
        return count;
    }

    // Traverse the array from unsorted part and fetch the minimum/maximum element and swap
    public int[] selectionSort(int arr[], boolean reverse){

        for(int i=0; i<arr.length; i++){
            int minimum_index = i;
            for(int j = i; j<arr.length; j++){
                if(!reverse && arr[j]<arr[minimum_index]){
                    minimum_index = j;
                }
                else if(arr[j]>arr[minimum_index]){
                    minimum_index = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minimum_index];
            arr[minimum_index] = temp;
        }
        return arr;

    }

    // Traverse and keep swapping until the maximum element goes to the last of the array
    public int[] bubbleSort(int arr[], boolean reverse){
        
        for(int i=0; i<arr.length; i++){
            for(int j=0; j<arr.length-i-1; j++){
                if(arr[j]>arr[j+1] && !reverse){
                    int temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                }
                else if(arr[j]<arr[j+1]){
                    int temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        return arr;
    }

    //
    public int[] insertionSort(int arr[], boolean reverse){
        
        for(int i=0; i<arr.length; i++){
            int key = arr[i];

            int j = i-1;
            while(j>=0 && arr[j]>key && !reverse){
                arr[j+1] = arr[j];
                j = j -1;
            }
            while(j>=0 && arr[j]<key && reverse){
                arr[j+1] = arr[j];
                j = j -1;
            }
            
            arr[j+1] = key;
        }
        
        return arr;
    }

    public int partitionQuickSort(int arr[], int low, int high){
        int i = low-1;
        int pivot = arr[high];
        for(int j = low; j<high; j++){
            if(arr[j]<= pivot){
                i = i+1;
                int temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
        arr[high] = arr[i+1];
        arr[i+1] = pivot;
        return i+1;
    }
    public void quickSort(int arr[], int low, int high){
        if(low<high){
            int pi = partitionQuickSort(arr, low, high);
            quickSort(arr, pi+1, high);
            quickSort(arr, low, pi-1);
        }
    }

    public static void main(String args[]){
        
        System.out.println(args.length);

        // For sorting ....
        int[] array = {53,21,63,32,54,64,62,33,72,66};

        // Inversion Count
        // System.out.println("InversionCount: "+ new Untitled().inversionCount(array));
        
        // Selection sort
        // array = new Untitled().selectionSort(array, true);

        // Bubble sort
        // array = new Untitled().bubbleSort(array, true);

        // Insertion sort
        // array = new Untitled().insertionSort(array, false);

        // Quick sort
        new Untitled().quickSort(array, 0, array.length-1);
        
        // For printing .....
        for(int i: array){
            System.out.println(i);
        }
    }

}