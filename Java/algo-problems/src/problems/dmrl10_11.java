package problems;

import java.util.Scanner;

public class dmrl10_11 {
    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        System.out.print("행의 수: ");
        int rows = input.nextInt();
        System.out.print("열의 수: ");
        int cols = input.nextInt();
        System.out.print("난수의 최대값: ");
        int max = input.nextInt();

        int[][] table = new int[rows][cols];
        int[] rowSum = new int[rows];
        int[] colSum = new int[cols];
        int total;

        System.out.println();
        System.out.println("초기 배열");
        display(table, rows, cols);         // 초기 table 출력
        System.out.println();

        System.out.println();
        System.out.println("난수가 저장된 배열");
        random(table, rows, cols, max);     // random 메소드 호출
        display(table, rows, cols);         // 난수가 채워진 table 출력
        System.out.println();

        System.out.println();
        System.out.println("가로, 세로 합이 계산된 배열");
        calculateRowSums(table, rows, cols, rowSum);
        calculateColSums(table, rows, cols, colSum);
        total = calculateTotal(rowSum) + calculateTotal(colSum) ;

        displayAll(table, rows, cols, rowSum, colSum, total);   // 전체 출력
        System.out.println();

        input.close();

    }

    /**
     * 이차원 배열 table의 첫 rows 행, 첫 cols 열에 있는 원소들을
     * 표 형태로 출력한다.
     * 전제조건: rows는 table의 행 개수보다 작거나 같고,
     *         cols는 table의 열 개수보다 작거나 같다.
     * @param table 이차원 정수 배열
     * @param rows 출력할 행 수
     * @param cols 출력할 열 수
     */
    public static void display(int[][] table, int rows, int cols) {
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++)
                System.out.print(table[i][j]+ "   ");
            System.out.println();
        }
    }
    /**
     * 2차원 배열 table의 전부 혹은 일부에 난수를 채운다.
     * 난수는 0 이상, max "이하" 정수이어야 한다.
     * 전제 조건: rows는 table의 행 개수보다 작거나 같아야 한다.
     * 전제 조건: cols는 table의 열 개수보다 작거나 같아야 한다.
     * @param table 배열
     * @param rows 난수를 채울 행 개수
     * @param cols 난수를 채울 열 개수
     * @param max 난수의 최대값
     */
    public static void random(int[][] table, int rows, int cols, int max) {

        for(int i=0; i< rows; i++)
            for(int j = 0; j < cols; j++)
                table[i][j]=(int)(Math.random()*max);
    }

    /**
     * 2차원 배열 table의 가로 합을 구해 rowSum에 저장한다.
     * table의 0번 행의 가로 합은 rowSum[0]에,
     * table의 1번 행의 가로 합은 rowSum[1]에,
     * ...
     * table의 (rows-1)번 행의 가로 합은 rowSum[rows-1]에 저장한다.
     *
     * @param table 2차원 배열
     * @param rows table의 행 수
     * @param cols table의 열 수
     * @param rowSum 각 행의 가로 합을 저장할 배열
     */
    public static void calculateRowSums(int[][] table, int rows, int cols, int[] rowSum) {
        for (int i = 0; i<rows; i++)
            for (int j = 0; j<cols; j++) {
                rowSum[i] += table[i][j];
            }
    }

    /**
     * 2차원 배열 table의 세로 합을 구해 colSum에 저장한다.
     * table의 0번 열의 세로 합은 colSum[0]에,
     * table의 1번 열의 세로 합은 colSum[1]에,
     * ...
     * table의 (cols-1)번 열의 세로 합은 colSum[cols-1]에 저장한다.
     * @param table 2차원 배열
     * @param rows table의 행 수
     * @param cols table의 열 수
     * @param colSum 각 열의 세로 합을 저장할 배열
     */
    public static void calculateColSums(int[][]table, int rows, int cols, int[] colSum) {
        for (int i = 0; i<cols; i++)
            for (int j = 0; j<rows; j++) {
                colSum[i] += table[j][i];
            }
    }

    /**
     * 2차원 배열 table의 원소들의 총합을 구한다.
     * 2차원 배열의 원소의 총합은 가로 합들을 모두 더해서 구할 수 있다.
     * @param rowSum 가로 합 배열
     * @return 총합
     */
    public static int calculateTotal(int[] rowSum) {
        int sum = 0;
        for (int i = 0; i<rowSum.length; i++)
            sum = rowSum[i] + sum;

        return sum;
    }

    /**
     * 원래의 데이터가 들어 있는 2차원 배열, 가로 합 배열, 세로 합 배열, 총합을
     * 표 형태로 출력한다.
     * @param table 원래의 데이터가 들어 있는 2차원 배열
     * @param rows table의 행 수
     * @param cols table의 열 수
     * @param rowSum 가로 합 배열
     * @param colSum 세로 합 배열
     * @param total 총합
     */
    public static void displayAll(int[][] table, int rows, int cols, int[] rowSum, int[] colSum, int total) {
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++)
                System.out.print(table[i][j]+ "\t");
            System.out.println("\t|\t" + rowSum[i]);
        }
        System.out.println();
        for (int i = 0; i < cols; i++)
            System.out.print(colSum[i] + "\t");
        System.out.println("\t|\t" + total);
    }
}
