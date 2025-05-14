import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            if (answer.get(answer.size()-1) == arr[i]) {
                continue;
            }
            answer.add(arr[i]);

        }
        int[] answer2 = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++){
            answer2[i] = answer.get(i);
        }
        return answer2;
    }
}