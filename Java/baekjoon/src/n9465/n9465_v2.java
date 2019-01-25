package n9465;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 한 칸 뒤의 대각선에 있는 값과 두 칸 뒤의 대각선에 있는 값 중 큰 값과 스티커에서 그 자리의 값을 더해 matrix를 구성
 * Scanner 대신 한거번에 많은 입력이 가능한 BufferedReader를 사용하였다.
 * @author JungWoo
 *
 */
public class n9465_v2 {
	static int N;
	static int[][] sticker;
	static int[][] matrix;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int times = Integer.parseInt(br.readLine());
		int answer[] = new int[times];
		for (int i = 0; i < times; i++) {
			in(br);
			matrix = new int[2][N+1];
			matrix[0][1] = sticker[0][0];
			matrix[1][1] = sticker[1][0];
			for (int j = 2; j < N+1; j++) {
				matrix[0][j] = Math.max(matrix[1][j-1], matrix[1][j-2]) + sticker[0][j-1];
				matrix[1][j] = Math.max(matrix[0][j-1], matrix[0][j-2]) + sticker[1][j-1];
			}
			answer[i] = Math.max(matrix[0][N], matrix[1][N]);
		}
		for (int temp : answer)
			System.out.println(temp);
		br.close();
	}
	
	public static void in(BufferedReader br) throws NumberFormatException, IOException {
		N = Integer.parseInt(br.readLine());
		sticker = new int[2][N];
		for (int i = 0; i < 2; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++)
				sticker[i][j] = Integer.parseInt(st.nextToken());
		}
	}
}