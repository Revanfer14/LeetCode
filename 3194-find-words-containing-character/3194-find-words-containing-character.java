class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> res = new ArrayList<>();
        String target = String.valueOf(x);

        for(int i = 0; i < words.length; i++){
            for(int j = 0; j < words.length; j++){
                if(words[i].contains(target)){
                    res.add(i);
                    break;
                }
            }
        }

        return res;
    }
}