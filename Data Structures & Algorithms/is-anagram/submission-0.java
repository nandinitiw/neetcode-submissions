class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length()!=t.length()) return false;

        char[] snew = s.toCharArray();
        char[] tnew = t.toCharArray();

        int[] alf = new int[26];
        for(int i=0; i<s.length(); i++){
            alf[snew[i]-'a']++;
            alf[tnew[i]-'a']--;
        }

        for(int letter:alf){
            if(letter!=0) return false;
        }

        return true;

        //need to check if each letter in the word is in the other word
        //split into char arrs
        //hash one of the char arrs

        //loop through length of one char array
        //for each iteration, check if that is in the hash set
        //if so, remove. if not, return false
        //at the end, if the hash set is empty, return true

        /*
        char[] snew = s.toCharArray();
        char[] tnew = t.toCharArray();

        if(s.length() != t.length()) return false;

        Set<Character> sstrs = new HashSet<>();
        for(int i=0; i<s.length(); i++){
            sstrs.add(snew[i]);
        }

        for(int i=0; i<t.length(); i++){
            if(sstrs.contains(tnew[i])) sstrs.remove(tnew[i]);
            else{
                return false;
            }
        }
        return true;
        */

        //****//

    }
}
