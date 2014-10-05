// Problem statement:
// https://www.hackerrank.com/contests/back2school14/challenges/xor-subsequence
// This solution is a brute force approach that gets about 60 points out of 100
// and times out on the other cases. I wrote a faster later but it has some bug
// where the answers are slightly wrong, so I didn't submit it.
import java.util.*;

public class BruteForce {
  public static void main(String[] args) {

    Scanner s = new Scanner(System.in);

    int n = s.nextInt();
    int[] xor = new int[n+2];
    for (int i = 1; i < n+1; i++){
      xor[i] = s.nextInt();
    }
    for (int i = 2; i < n+1; i++){
      xor[i] ^= xor[i-1];
    }

    int[] counts = new int[1<<16];

    for (int i = 0; i < n+1 ; i++){
      for (int j = i+1; j < n+1; j++){
        counts[xor[i]^xor[j]]++;
      }
    }
    int max = 0;
    int idx = -1;
    for (int i = 1; i < counts.length; i++) {
      if (counts[i] > max) {
        max = counts[i];
        idx = i;
      }
    }
    System.out.print(idx + " " + max);
  }
}
