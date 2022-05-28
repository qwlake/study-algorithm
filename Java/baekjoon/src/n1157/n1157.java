package n1157;

import java.io.IOException;
import java.util.Scanner;

public class n1157 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		// 1. 입력
		Scanner scanner = new Scanner(System.in);
		String input = scanner.nextLine();

		// 2. 가장 빈번한 알파벳의 집합 구하기
		char maxValue = findMaxValue(input);

		// 3. 출력
		System.out.println(maxValue);
	}

	private static char findMaxValue(String input) {
		String upperInput = input.toUpperCase();
		int[] counts = new int[26];

		int maxCount = -1;
		char maxValue = '?';
		for (int i = 0; i < upperInput.length(); i++) {
			char alphabet = upperInput.charAt(i); // 입력된 문자열에서 i 번째에 해당하는 문자
			int alphabetIndex = alphabet - 65; // `alphabet` 변수가 알파벳 순으로 정렬했을때 몇 번째에 위치하는지에 대한 인덱스
			counts[alphabetIndex] += 1;
			if (counts[alphabetIndex] == maxCount) { // 기존에 나왔던 카운트 최댓값과 같다면
				maxValue = '?';
			} else if (counts[alphabetIndex] > maxCount) { // 기존에 나왔던 카운트 최댓값보다 크다면
				maxValue = upperInput.charAt(i);
				maxCount = counts[alphabetIndex];
			}
		}
		return maxValue;
	}
}