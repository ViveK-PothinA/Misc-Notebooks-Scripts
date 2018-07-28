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

    public void merge(int arr[], int l, int m, int h){
        int leftNum = m-l+1;
        int rightNum = h-m;

        int[] left = new int[leftNum];
        int[] right = new int[rightNum];

        for(int i=0; i<leftNum; i++){
            left[i] = arr[l+i];
        }
        for(int j=0; j<rightNum; j++){
            right[j] = arr[m+1+j];
        }

        int i = 0, j = 0;
        int k = l;

        while(i<leftNum && j<rightNum){
            if(left[i]<=right[j]){
                arr[k] = left[i];
                i = i+1;
                k = k+1;
            }
            else{
                arr[k] = right[j];
                j = j+1;
                k = k+1;
            }
        }
        while(i<leftNum){
            arr[k] = left[i];
            i = i+1;
            k = k+1;
        }
        while(j<rightNum){
            arr[k] = right[j];
            j = j+1;
            k = k+1;
        }
        
    }

    public void mergeSort(int arr[], int l, int h){
        

        if(l<h){
            int m = (l+h)/2;
            mergeSort(arr, l, m);
            mergeSort(arr, m+1, h);
            merge(arr, l, m, h);
        }
    }    

    public static void main(String args[]){
        
        System.out.println(args.length);
        if(args.length!=0){
            for(String s:args){
                System.out.print(s+"  ");
            }
        }
        System.out.println("");

        int[] array;
        // For sorting ....
        if(args.length!=0){
            int i=0; 
            array = new int[args.length];
            for(String s: args){
                array[i] = Integer.parseInt(s);
                i = i+1;
            }
        }
        else{
            array = new int[]{53,21,63,32,54,64,62,33,72,66};
        }

        // Inversion Count
        // System.out.println("InversionCount: "+ new SortingInJava().inversionCount(array));
        
        // Selection sort
        // array = new SortingInJava().selectionSort(array, true);

        // Bubble sort
        // array = new SortingInJava().bubbleSort(array, true);

        // Insertion sort
        // array = new SortingInJava().insertionSort(array, false);

        // Quick sort
        // new SortingInJava().quickSort(array, 0, array.length-1);

        // Merge sort
        new SortingInJava().mergeSort(array, 0, array.length-1);
        
        // For printing .....
        for(int i: array){
            System.out.println(i);
        }
    }

}