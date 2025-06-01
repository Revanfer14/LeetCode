class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        int y = words.length;
        String target = String.valueOf(x);
        
        List<Integer> result = new ArrayList<>();

        for(int i = 0; i < y; i++){
            if(words[i].contains(target)){
                result.add(i);
            }
        }

        return result;
}
}