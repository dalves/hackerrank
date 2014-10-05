// Problem statement:
// https://www.hackerrank.com/contests/back2school14/challenges/xor-subsequence
// This is the my faster solution to the problem, but unfortunately I didn't have
// time to figure out why the answers are slightly different from the other one, so
// I didn't submit it.

import java.util.*;

public class Fast {
  public static void main(String[] args) {

    Scanner s = new Scanner(System.in);

    int n = s.nextInt();

    int[] xor = new int[n+2];
    int[] counts = new int[1<<16];

    for (int i = 1; i < n+1; i++){
      xor[i] = s.nextInt() ^ xor[i-1];
      counts[xor[i]]++;
    }

    int[] results = new int[1<<16];

    for (int i = 0; i < counts.length; i++) {
      for (int j = i+1; j < counts.length; j++) {
        results[i^j] += counts[i] * counts[j];
      }
    }

    int max = 0;
    int idx = -1;
    for (int i = 0; i < results.length; i++) {
      if (results[i] > max) {
        max = results[i];
        idx = i;
      }
    }
    System.out.print(idx + " " + max);
  }
}
